# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSignal,QTimer,QDateTime
from PyQt5.QtWidgets import QDesktopWidget
import TCPSocket
import socket
import sys
from PressureMonitor import *
from load_setting_xml import *
from EquipmentInfo import *
from TCPSocket import *
from setGPIO_mode import *
from Equipment_Settings import *

class MainWindow(TCPSocket,PressureMonitor):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.set_QtWidgets_position()
        self.check_and_load_Setting_xml()
        self.log_file_init()
        self.get_equipment_info()
        self.init_TCP_settings()
        self.init_Setting()
        self.start_monitor_pressure(4)
        
        self.setting = Equipment_Settings()
        self.setting.update_current_count_Signal.connect(self.update_current_count)
        self.setting.update_alarm_value_Signal.connect(self.update_alarm_value)
        self.setting.update_tcp_setting_Signal.connect(self.update_tcp_setting)
        self.init_timer()
        
    def update_tcp_setting(self):
        globalVal.global_tcp_ip, globalVal.global_tcp_port=get_TCP_settings()
    
    def update_alarm_value(self):
        self.get_alarm_value()
    
        
    def update_current_count(self):
        self.txt_CurrentCount.setText('Current: '+str(globalVal.global_currentCount))
        
    
    def init_timer(self):        
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start()
        
        
    def showtime(self):
        datetime = QDateTime.currentDateTime()
        text = datetime.toString("yyyy-MM-dd HH:mm:ss")
        self.txt_current_time.setText(text)

        
        
    def set_QtWidgets_position(self):       
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().left()
        qr.moveLeft(cp)
        self.move(qr.topLeft())


    def connect(self, ):
        """
        控件信号-槽的设置
        :param : QDialog类创建的对象
        :return: None
        """
        # 如需传递参数可以修改为connect(lambda: self.click(参数))
        super(MainWindow, self).connect()
        self.btn_connect.clicked.connect(self.connectTCPServer)
        self.sinOut.connect(self.set_Pressure)
        self.btn_setting.clicked.connect(self.slot_btn_settings)
        self.sig_setting.connect(self.sig_setting_slot)
        self.signal_write_msg.connect(self.write_msg)       
        

    def write_msg(self, msg):
        #####在这里打印接收到的信息 并处理不同的事件####
        # if isinstance(msg, unicode):
        #     msg = msg.encode("utf-8")
        self.split_msg(msg)

    def split_msg(self, msg):
        print(msg)
        PSN = self.get_str_start_isPSN(msg, '~')
        log_info=''
        if PSN != "":
            globalVal.PSN = PSN
            self.txt_PSN.setText('PSN:' + PSN)
            self.txt_PSN.setAlignment(Qt.AlignCenter)
            str_status = self.get_str_Status(msg, '~')
            if str_status == '0':
                self.txt_PSN.setStyleSheet("background-color: green;")
                self.statusBar().showMessage('PSN: ' + PSN + ' Status: OK')
                init_global_var()
                globalVal.global_isStart = True
                self.statusBar().showMessage('set Load Signal: ' + str(True))
                
                log_info='PSN: ' + PSN + ' Status: OK ,set Load Signal: ' + str(True)
                #  ###给出压合信号###
                setGPIO_LoadSignal(1)
            else:
                self.txt_PSN.setStyleSheet("background-color: red;")
                self.statusBar().showMessage('PSN: ' + PSN + ' Status: NG')
                self.statusBar().showMessage('set Load Signal: ' + str(False))
                log_info='PSN: ' + PSN + ' Status: NG, set Load Signal: ' + str(False)
                setGPIO_LoadSignal(0)
                globalVal.global_isStart = False
                
            output_log_message(log_info)
            globalVal.global_status = str(str_status)

        else:
            ###不是服务器发来的信息
            print(PSN)
            if self.link == False:
                self.btn_connect.setText('連接')

    def get_str_start_isPSN(self, val, str_check):
        PSN = ""
        if val.startswith(str_check):
            val_list = val.split(';')
            PSN = self.get_PSN(val_list)
        else:
            pass
        return PSN

    def get_str_Status(self, val, str_check):
        isOK = ""
        if val.startswith(str_check):
            val_list = val.split(';')
            isOK = self.get_IsOK(val_list)
        else:
            pass
        return isOK

    def get_PSN(self, val_list):
        val = val_list[0].replace('~', '')
        return val

    def get_IsOK(self, val_list):
        isOK = val_list[1]
        return isOK

    def connectTCPServer(self):
        if self.link == False:
            self.tcp_client_start()
            if self.link == True:
                msg = "已連接"
                self.tcp_send(msg)
                self.btn_connect.setText('斷開連接')
        else:
            self.tcp_close()
            msg = '連接'
            self.link = False
            self.btn_connect.setText(msg)


    def slot_btn_settings(self):              
        self.sig_setting.emit()
        
    
             

    def sig_setting_slot(self):
        self.setting.show()


    def set_Pressure(self, data):

        num,val = self.splitData(data)
        ####显示值到UI上，处理超限图片显示
        self.set_Pressure_By_case(num,val)
        #####把数据存到dictionary里
        self.save_Pressure_by_channel(num,val)
        #####如果接收到了PSN和OK信号，就要把数据发送回TCP server
        self.send_Pressure_value()

    def cal_press_count(self,num):
        if num == 0:
            globalVal.global_currentCount +=1
            self.txt_CurrentCount.setText('Current: '+str(globalVal.global_currentCount))
            globalVal.global_TotalCount +=1
            self.txt_TotalCount.setText('Total: '+str(globalVal.global_TotalCount))
            save_value_to_setting_xml(SETTING_XML_VALUE_TYPE_TOTAL_COUNT,str(globalVal.global_TotalCount))

    def send_Pressure_value(self):
        end_time = datetime.now()
        execute_time = end_time - globalVal.global_start_time
        is_timeout = self.check_is_timeout(execute_time)
        if self.link == True:
            if globalVal.global_isStart == True:
                isSend = False
                isAlarm = self.check_is_all_in_range(4)
                if is_timeout == False:
                    if globalVal.is_Collected == True:
                        isSend = True
                else:
                    isSend = True
                    isAlarm = True
                    globalVal.global_start_time = datetime.now()
                if isSend == True:
                    data_str = self.get_data_combine()
                    # ###传出压力值的格式
                    # ### 压合完成时候的时间 ; 1PV ; 2PV ; 3PV ; 4PV ; PSN ; 压合所用周期 ; 报警值 ; 压合机编号
                    file_str = end_time.strftime(DATE_FORMAT)+';'\
                               + data_str+globalVal.PSN \
                               +";"+str(execute_time.seconds)+'s;'\
                               +str(int(isAlarm))\
                               +';'+globalVal.Equipment_ID
                    self.tcp_send(file_str)
                    save_data(file_str)
                    globalVal.global_isStart = False
                    globalVal.is_Collected = False
                    init_global_var()

    def check_is_timeout(self,execute_time):
        is_timeout = False
        timeout = get_timeout()
        if execute_time.seconds >= int(timeout):
            is_timeout = True
        return is_timeout


    def check_is_send(self,end_time):
        ###获取timeout###
        timeout = get_timeout()
        ###执行时间###
        execute_time = end_time - globalVal.global_start_time
        ###检查一下有没有都采集完了
        channel_num = int(get_channel_num())
        isCollected,is_Over_Limit_Alarm = self.check_is_all_collected(channel_num)
        isSend = False
        isAlarm = False

        if execute_time.seconds < int(timeout):
        ###没到timeout时间，但是都采集完了 就送出去###
            if isCollected == True:
                isSend = True
                isAlarm = is_Over_Limit_Alarm
        else:
        ###达到timeout时间，也送出去###
            isSend = True
            isAlarm = True
        return isSend,isAlarm

    '''把数据拼起来'''
    def get_data_combine(self):
        data_str = ""
        for i in range(int(get_channel_num())):
            data_str += globalVal.global_dict[i][0]+';'
        return data_str

    '''还要检查每个通道有没有超限，只要有一个超限，就要给警告信号'''
    def check_is_all_in_range(self,channel_num):
        is_Over_Limit_Alarm = False
        for i in range(channel_num):
            if globalVal.global_dict[i][4] == True:
                is_Over_Limit_Alarm = True
        return is_Over_Limit_Alarm


    '''检查某个通道是否采集完'''
    def check_is_collected(self,num):
        return globalVal.global_dict[num][2]

    def save_Pressure_by_channel(self,num,val):
        ###获取通道上一次的数值###
        last_val = globalVal.global_dict[num][6]
        ###低于最高值的数值###
        ###当采集值大于标定值，并且比上一次更大时,计数清零###
        if float(val) >= NOISE_VALUE and float(val) >= float(last_val):
            globalVal.global_dict[num][6] = val
            globalVal.global_dict[num][1] = datetime.now().strftime(DATE_FORMAT)
            globalVal.global_dict[num][3] = 0
            globalVal.global_dict[num][5] = True
        ### 当采集值小于上一次的值时，开始计数###
        elif float(val) < float(last_val):
            if globalVal.global_dict[num][5] == True:
                globalVal.global_dict[num][3] += 1
            # globalVal.global_dict[num][2] = False

        ### 当计数大于标定数时，表示采集完成
        # print(num,globalVal.global_dict[num][3],val,globalVal.global_dict[num][6])
        if globalVal.global_dict[num][3] >= noise_count:
            globalVal.global_dict[num][2] = True
            globalVal.global_dict[num][3] = 0
            globalVal.global_dict[num][5] = False
            globalVal.global_dict[num][0] = globalVal.global_dict[num][6]
            globalVal.global_dict[num][6] = '0'
            self.cal_press_count(num)

    
    def set_controller_pressure(self,control_channel,control_alarm,val,num):
        control_channel.setText(str(num+1) +'PV: ' +val + ' N')
        upper_val = get_upper_value(num)
        lower_val = get_lower_value(num)
        isValid = self.judge_cross_line(float(val), float(upper_val), float(lower_val))
        if isValid == False:
            control_alarm.setStyleSheet(ALARM_PIC_STYLE)
        elif isValid == True:
            control_alarm.setStyleSheet(NORMAL_PIC_STYLE)
            setAlarm_Signal(0)
        ###当采集数据超限时就存下来超限信号
        globalVal.global_dict[num][4] = isValid

    def set_Pressure_By_case(self,num,val):

        if num == 0:
            self.set_controller_pressure(self.txt_Sensor1Pressure,self.Sensor1_Alarm,val,num)
            self.setting.txt_CurrentPressure.setText(val +' N')

        elif num == 1:
            self.set_controller_pressure(self.txt_Sensor2Pressure,self.Sensor1_Alarm_2,val,num)

        elif num == 2:
            self.set_controller_pressure(self.txt_Sensor3Pressure,self.Sensor1_Alarm_3,val,num)

        elif num == 3:
            self.set_controller_pressure(self.txt_Sensor4Pressure,self.Sensor1_Alarm_4,val,num)
        else:
            pass

    def judge_cross_line(self,val,upper,lower):
        isValid = True
        if val >= lower and val <= upper:
            pass
        else:
            isValid = False
        return isValid


    def splitData(self,data):
        val_list = data.split(':')
        return int(val_list[0]),val_list[1]



    def reset(self):
        """
        功能函数，将按钮重置为初始状态
        :return:None
        """
        self.link = False
        self.client_socket_list = list()


    def check_and_load_Setting_xml(self):
        global SETTING_XML_PATH
        if not os.path.exists(SETTING_XML_PATH):
            create_setting_xml()
            
            
    def log_file_init(self):
        print(LOG_FILE_PATH)
        if not os.path.exists(LOG_FILE_PATH):
            log_file = open(LOG_FILE_PATH,'w')
            log_file.close()


    def get_host_ip(self):
        ip = "0.0.0.0"
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
            print ('IP:%s' % ip)
        except IOError as err:
            print (err)
            output_log_message("IOError: %s" % str(err))

        finally:
            s.close()
        return ip


    def get_equipment_info(self):
        self.get_alarm_value()
        globalVal.Equipment_ID = get_equipment_id()
        globalVal.system_IP = self.get_host_ip()
        globalVal.global_calibration = get_calibration_coefficient()
        # global_TotalCount = int(get_total_count())
        globalVal.global_TotalCount = int(get_total_count())
        self.txt_TimeAndIDAndIP.setText("ID :  "+globalVal.Equipment_ID+"\nIP :  "+globalVal.system_IP)
        self.txt_TotalCount.setText("Total: "+str(globalVal.global_TotalCount))
        self.txt_CurrentCount.setText("Current: "+str(globalVal.global_currentCount))


    def get_alarm_value(self):

        upper_value_1 = get_upper_value(1)
        lower_value_1 = get_lower_value(1)
        self.txt_Sensor1AlarmValue.setText("SV: "+lower_value_1+" N ~"+upper_value_1+" N")        
        
        upper_value_2 = get_upper_value(2)
        lower_value_2 = get_lower_value(2)
        self.txt_Sensor2AlarmValue.setText("SV: "+lower_value_2+" N ~"+upper_value_2+" N")

        upper_value_3 = get_upper_value(3)
        lower_value_3 = get_lower_value(3)
        self.txt_Sensor3AlarmValue.setText("SV: "+lower_value_3+" N ~"+upper_value_3+" N")

        upper_value_4 = get_upper_value(4)
        lower_value_4 = get_lower_value(4)
        self.txt_Sensor4AlarmValue.setText("SV: "+lower_value_4+" N ~"+upper_value_4+" N")
        

    def init_Setting(self):
        channel_num = get_channel_num()
        timeout = get_timeout()
        #self.comboBox.setCurrentText(channel_num)
        #self.txt_timeout.setText(timeout)
        # self.lbl_channel_num.setVisible(False)
        # self.comboBox.setVisible(False)

    def init_TCP_settings(self):
        tcp_ip,tcp_port = get_TCP_settings()
        globalVal.global_tcp_ip = tcp_ip
        globalVal.global_tcp_port = tcp_port


    #当我们关闭一个窗口时，在PyQt中就会触发一个QCloseEvent的事件，正常情况下会直接关闭这个窗口，
    #但是我们不希望这样的事情发生，所以我们需要重新定义QCloseEvent，函数名称为closeEvent不可变
    def closeEvent(self,event):#函数名固定不可变
        reply=QtWidgets.QMessageBox.question(self,u'警告',u'确认退出?',QtWidgets.QMessageBox.Yes,QtWidgets.QMessageBox.No)
        #QtWidgets.QMessageBox.question(self,u'弹窗名',u'弹窗内容',选项1,选项2)
        if reply==QtWidgets.QMessageBox.Yes:
            # clearGPIO()
            event.accept()#关闭窗口
        else:
            event.ignore()#忽视点击X事件