# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow, QAction, qApp, QApplication, QMessageBox, QVBoxLayout, QSizePolicy, QWidget,QInputDialog, QLineEdit
from PyQt5.QtCore import pyqtSignal
from settingsUI import *
from load_setting_xml import *

class Equipment_Settings(QMainWindow, Ui_MainWindow):
    
    update_current_count_Signal = pyqtSignal()
    update_alarm_value_Signal = pyqtSignal()
    update_tcp_setting_Signal = pyqtSignal()
    

    def __init__(self,parent=None):
        super(QMainWindow,self).__init__(parent)
        self.set_QtWidgets_position()
        self.setupUi(self)
        self.initSettings()
        self.init_button_click_event()
        self.set_setting_edit_status(False)
        
        
        
        
    def set_QtWidgets_position(self):       
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().left()
        qr.moveLeft(cp)
        self.move(qr.topLeft())
        
        
    def init_button_click_event(self):
        self.btn_SaveAlarmValue.clicked.connect(self.btn_SaveAlarmValue_Onclick)
        self.btn_SaveCalibrationCoefficient.clicked.connect(self.btn_SaveCalibrationCoefficient_Onclick)
        self.btn_tcp_settings.clicked.connect(self.btn_tcp_settings_Onclick)
        self.btn_ClearCurrentCount.clicked.connect(self.btn_ClearCurrentCount_Onclick)
        self.btn_unlock.clicked.connect(self.btn_unlock_Onclick)
        self.btn_lock.clicked.connect(self.btn_lock_Onclick)
        
        
    def btn_unlock_Onclick(self):    
        is_password_correct=self.input_password()
        if is_password_correct:
            self.set_setting_edit_status(True)
            self.btn_unlock.setEnabled(False)
            self.btn_lock.setEnabled(True)
        else:
            self.set_setting_edit_status(False)
            
            
    def btn_lock_Onclick(self):
        self.set_setting_edit_status(False)
        self.btn_lock.setEnabled(False)
        self.btn_unlock.setEnabled(True)
        self.statusBar().showMessage('')
        
               
    def btn_ClearCurrentCount_Onclick(self):                     
        self.clearCurrentCount()
        self.statusBar().showMessage('清零當前壓合次數成功')
               
        
    def btn_tcp_settings_Onclick(self):
        self.save_tcp_setting()
        self.update_tcp_setting_Signal.emit()
        self.statusBar().showMessage('TCP設置成功')
        
        
    def btn_SaveCalibrationCoefficient_Onclick(self):
        save_value_to_setting_xml(SETTING_XML_VALUE_TYPE_CALIBRATION_COEFFICIENT,self.txt_CalibrationCoefficient.text())
        self.statusBar().showMessage('校準係數設置成功')
       
    def btn_SaveAlarmValue_Onclick(self):       
        self.save_alarm_values()
        self.statusBar().showMessage('報警上下線值設置成功')
    
    def clearCurrentCount(self):
        globalVal.global_currentCount = 0
        self.update_current_count_Signal.emit() 

        
    def set_setting_edit_status(self,status):
        
        self.btn_ClearCurrentCount.setEnabled(status)
        self.btn_lock.setEnabled(status)
        
        self.txt_Sensor_1SV_Upper.setEnabled(status)
        self.txt_Sensor_1SV_Lower.setEnabled(status)
        self.txt_Sensor_2SV_Upper.setEnabled(status)
        self.txt_Sensor_2SV_Lower.setEnabled(status)
        self.txt_Sensor_3SV_Upper.setEnabled(status)
        self.txt_Sensor_3SV_Lower.setEnabled(status)
        self.txt_Sensor_4SV_Upper.setEnabled(status)
        self.txt_Sensor_4SV_Lower.setEnabled(status)
        self.txt_CurrentPressure.setEnabled(status)
        self.btn_SaveAlarmValue.setEnabled(status)
        self.btn_SaveCalibrationCoefficient.setEnabled(status)
        self.btn_tcp_settings.setEnabled(status)
       
        self.txt_CalibrationCoefficient.setEnabled(status)

        self.txt_tcp_server_IP.setEnabled(status)
        self.txt_tcp_server_port.setEnabled(status)

        self.comboBox.setEnabled(status)
        self.txt_timeout.setEnabled(status)
        
        
        
    def input_password(self):
        is_password_correct=False
        tips='Input Password:'
        password=get_password()
        while True:
            text, okPressed = QInputDialog.getText(self, "Input Dialog",tips, QLineEdit.Password, "")
            if okPressed:            
                if  text == '':
                    tips='Password can not be empty'
                elif text==password:
                    return True
                    break
                else:
                    tips="Password isn't correct"
                    is_password_match=False               
            else:
                return False
                break  
        
        
    def save_tcp_setting(self):
        tcp_ip = self.txt_tcp_server_IP.text()
        tcp_port = self.txt_tcp_server_port.text()
        channel_num = self.comboBox.currentText()
        timeout = self.txt_timeout.text()       
        
        save_value_to_setting_xml(SETTING_XML_VALUE_TYPE_TCP_IP , tcp_ip)
        save_value_to_setting_xml(SETTING_XML_VALUE_TYPE_TCP_PORT , tcp_port)
        save_value_to_setting_xml(SETTING_XML_VALUE_CHANNEL_NUM, channel_num)
        save_value_to_setting_xml(SETTING_XML_VALUE_TIMEOUT,timeout)
        
        
        
        print("jhbgkgk")
        
        
    def save_alarm_values(self):
        alarm_lower_1sv = self.txt_Sensor_1SV_Lower.text()
        alarm_upper_1sv = self.txt_Sensor_1SV_Upper.text()
        alarm_lower_2sv = self.txt_Sensor_2SV_Lower.text()
        alarm_upper_2sv = self.txt_Sensor_2SV_Upper.text()
        alarm_lower_3sv = self.txt_Sensor_3SV_Lower.text()
        alarm_upper_3sv = self.txt_Sensor_3SV_Upper.text()
        alarm_lower_4sv = self.txt_Sensor_4SV_Lower.text()
        alarm_upper_4sv = self.txt_Sensor_4SV_Upper.text()

        save_value_to_setting_xml(SETTING_XML_VALUE_TYPE_LOWER_VALUE,alarm_lower_1sv)
        save_value_to_setting_xml(SETTING_XML_VALUE_TYPE_LOWER_VALUE_2SV,alarm_lower_2sv)
        save_value_to_setting_xml(SETTING_XML_VALUE_TYPE_LOWER_VALUE_3SV,alarm_lower_3sv)
        save_value_to_setting_xml(SETTING_XML_VALUE_TYPE_LOWER_VALUE_4SV,alarm_lower_4sv)
        save_value_to_setting_xml(SETTING_XML_VALUE_TYPE_UPPER_VALUE,alarm_upper_1sv)
        save_value_to_setting_xml(SETTING_XML_VALUE_TYPE_UPPER_VALUE_2SV,alarm_upper_2sv)
        save_value_to_setting_xml(SETTING_XML_VALUE_TYPE_UPPER_VALUE_3SV,alarm_upper_3sv)
        save_value_to_setting_xml(SETTING_XML_VALUE_TYPE_UPPER_VALUE_4SV,alarm_upper_4sv)
        
        
        self.update_alarm_value_Signal.emit()
        
        #self.init_equipment_info()
        
        

        
    def init_equipment_info(self):

        upper_value_1 = get_upper_value(1)
        lower_value_1 = get_lower_value(1)
        self.txt_Sensor_1SV_Upper.setText(upper_value_1)
        self.txt_Sensor_1SV_Lower.setText(lower_value_1)       
        
        upper_value_2 = get_upper_value(2)
        lower_value_2 = get_lower_value(2)
        self.txt_Sensor_2SV_Upper.setText(upper_value_2)
        self.txt_Sensor_2SV_Lower.setText(lower_value_2)

        upper_value_3 = get_upper_value(3)
        lower_value_3 = get_lower_value(3)
        self.txt_Sensor_3SV_Upper.setText(upper_value_3)
        self.txt_Sensor_3SV_Lower.setText(lower_value_3)

        upper_value_4 = get_upper_value(4)
        lower_value_4 = get_lower_value(4)
        self.txt_Sensor_4SV_Upper.setText(upper_value_4)
        self.txt_Sensor_4SV_Lower.setText(lower_value_4)


    def initSettings(self):
        self.setUpLowerValue(self.txt_Sensor_1SV_Upper,self.txt_Sensor_1SV_Lower,1)
        self.setUpLowerValue(self.txt_Sensor_2SV_Upper,self.txt_Sensor_2SV_Lower,2)
        self.setUpLowerValue(self.txt_Sensor_3SV_Upper,self.txt_Sensor_3SV_Lower,3)
        self.setUpLowerValue(self.txt_Sensor_4SV_Upper,self.txt_Sensor_4SV_Lower,4)

        globalVal.global_calibration = get_calibration_coefficient()
        self.txt_CalibrationCoefficient.setText(globalVal.global_calibration)
        tcp_ip,tcp_port = get_TCP_settings()

        self.txt_tcp_server_IP.setText(tcp_ip)
        self.txt_tcp_server_port.setText(tcp_port)
        channel_num = get_channel_num()
        timeout = get_timeout()
        self.comboBox.setCurrentText(channel_num)
        self.txt_timeout.setText(timeout)
        

    def setUpLowerValue(self,upper_control,lower_control,num):
        upper_value = get_upper_value(num)
        lower_value = get_lower_value(num)
        upper_control.setText(upper_value)
        lower_control.setText(lower_value)
        

    def save_tcp_setting(self):
        tcp_ip = self.txt_tcp_server_IP.text()
        tcp_port = self.txt_tcp_server_port.text()
        channel_num = self.comboBox.currentText()
        timeout = self.txt_timeout.text()
        # print(tcp_ip,tcp_port)
        save_value_to_setting_xml(SETTING_XML_VALUE_TYPE_TCP_IP , tcp_ip)
        save_value_to_setting_xml(SETTING_XML_VALUE_TYPE_TCP_PORT , tcp_port)
        save_value_to_setting_xml(SETTING_XML_VALUE_CHANNEL_NUM, channel_num)
        save_value_to_setting_xml(SETTING_XML_VALUE_TIMEOUT,timeout)