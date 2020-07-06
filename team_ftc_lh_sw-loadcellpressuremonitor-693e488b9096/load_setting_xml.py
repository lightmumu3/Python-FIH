# -*- coding: utf-8 -*-

import os
from datetime import datetime
from xml.etree import ElementTree as ET

CURRENT_PATH = os.path.dirname(__file__)
SETTING_XML='Setting.xml'
SETTING_XML_PATH = os.path.join(CURRENT_PATH, SETTING_XML)
SETTING_XML_VALUE_TYPE_UPPER_VALUE = 'UpperValue'
SETTING_XML_VALUE_TYPE_UPPER_VALUE_2SV = 'UpperValue_2SV'
SETTING_XML_VALUE_TYPE_UPPER_VALUE_3SV = 'UpperValue_3SV'
SETTING_XML_VALUE_TYPE_UPPER_VALUE_4SV = 'UpperValue_4SV'
SETTING_XML_VALUE_TYPE_LOWER_VALUE = 'LowerValue'
SETTING_XML_VALUE_TYPE_LOWER_VALUE_2SV = 'LowerValue_2SV'
SETTING_XML_VALUE_TYPE_LOWER_VALUE_3SV = 'LowerValue_3SV'
SETTING_XML_VALUE_TYPE_LOWER_VALUE_4SV = 'LowerValue_4SV'
SETTING_XML_VALUE_TYPE_CALIB_WEIGHT = 'CalibrationWeight'
SETTING_XML_VALUE_TYPE_CALIB_RAWDATA = 'CalibrationRawdata'
SETTING_XML_VALUE_TYPE_CALIB_RESULT = 'CalibrationResult'
SETTING_XML_VALUE_TYPE_CALIB_RESULT_SLOPE = 'slope'
SETTING_XML_VALUE_TYPE_CALIB_RESULT_INTERCEPT = 'intercept'
SETTING_XML_VALUE_TYPE_TOTAL_COUNT = 'TotalCount'
SETTING_XML_VALUE_TYPE_PASSWORD='Password'
SETTING_XML_VALUE_TYPE_EQUIPMENT_ID='EquipmentID'
SETTING_XML_VALUE_TYPE_CALIBRATION_COEFFICIENT="CalibrationCoefficient"
SETTING_XML_VALUE_TYPE_TCP_IP = 'TCPIP'
SETTING_XML_VALUE_TYPE_TCP_PORT = 'TCPPort'
SETTING_XML_VALUE_CHANNEL_NUM = 'channelNum'
SETTING_XML_VALUE_TIMEOUT = 'timeout'

INIT_UPPER_VALUE = '20'
INIT_UPPER_VALUE_2SV = '20'
INIT_UPPER_VALUE_3SV = '20'
INIT_UPPER_VALUE_4SV = '20'
INIT_LOWER_VALUE = '0'
INIT_LOWER_VALUE_2SV = '0'
INIT_LOWER_VALUE_3SV = '0'
INIT_LOWER_VALUE_4SV = '0'


INIT_CALIB_WEIGHT='5,10,15'
INIT_CALIB_RESULT_SLOPE='1'
INIT_CALIB_RESULT_INTERCEPT='0'

INIT_CALIB_COEFFICIENT = '2'
INIT_TCP_IP = '0.0.0.0'
INIT_TCP_PORT = '54321'
INIT_CHANNEL_NUM = '4'
INIT_TIMEOUT = '20'
INIT_EQUIPMENT_ID = 'BJPM-M-FS-001'
INIT_PASS_WORD = '0000'

LOG_FILE = 'log.txt'
LOG_FILE_PATH = os.path.join(CURRENT_PATH, LOG_FILE)
DATA_FOLDER = 'Data'
DATA_FOLDER_PATH = os.path.join(CURRENT_PATH, DATA_FOLDER)
tmp_TotaL_Count = 0

ALARM_PIC_STYLE = "border-image: url(:/image/Alarm.jpg);"
NORMAL_PIC_STYLE = "border-image: url(:/image/Normal.jpg);"

# print(dict)

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
NOISE_VALUE = 1   #0.5N
noise_count = 2
VERSION = "3.0.1"

def getXMLSettings():
    read_tree = ET.parse(SETTING_XML_PATH)
    node_root = read_tree.getroot()
    return node_root

def get_upper_value(num):
    node_root = getXMLSettings()
    global node_son_upper_value
    if num == 1:
        node_son_upper_value = node_root.find(SETTING_XML_VALUE_TYPE_UPPER_VALUE)
    elif num == 2:
        node_son_upper_value = node_root.find(SETTING_XML_VALUE_TYPE_UPPER_VALUE_2SV)
    elif num == 3:
        node_son_upper_value = node_root.find(SETTING_XML_VALUE_TYPE_UPPER_VALUE_3SV)
    elif num == 4:
        node_son_upper_value = node_root.find(SETTING_XML_VALUE_TYPE_UPPER_VALUE_4SV)

    return node_son_upper_value.text

def get_lower_value(num):
    node_root = getXMLSettings()
    global node_son_lower_value
    if num == 1:
        node_son_lower_value = node_root.find(SETTING_XML_VALUE_TYPE_LOWER_VALUE)
    elif num == 2:
        node_son_lower_value = node_root.find(SETTING_XML_VALUE_TYPE_LOWER_VALUE_2SV)
    elif num == 3:
        node_son_lower_value = node_root.find(SETTING_XML_VALUE_TYPE_LOWER_VALUE_3SV)
    elif num == 4:
        node_son_lower_value = node_root.find(SETTING_XML_VALUE_TYPE_LOWER_VALUE_4SV)
    return node_son_lower_value.text

def get_calib_weight():
    node_root = getXMLSettings()
    node_son_calib_weight = node_root.find(SETTING_XML_VALUE_TYPE_CALIB_WEIGHT)
    return node_son_calib_weight.text

def get_calib_rawdata():
    node_root = getXMLSettings()
    node_son_calib_rawdata = node_root.find(SETTING_XML_VALUE_TYPE_CALIB_RAWDATA)
    return node_son_calib_rawdata.text

def get_calib_result():
    node_root = getXMLSettings()
    node_son_calib_result = node_root.find(SETTING_XML_VALUE_TYPE_CALIB_RESULT)
    return node_son_calib_result.text

def get_total_count():
    node_root = getXMLSettings()
    node_son_total_count = node_root.find(SETTING_XML_VALUE_TYPE_TOTAL_COUNT)
    return node_son_total_count.text

def get_password():
    node_root = getXMLSettings()
    node_son_password=node_root.find(SETTING_XML_VALUE_TYPE_PASSWORD)
    return node_son_password.text

def get_calibration_coefficient():
    node_root = getXMLSettings()
    node_son_cal_coefficient=node_root.find(SETTING_XML_VALUE_TYPE_CALIBRATION_COEFFICIENT)
    return node_son_cal_coefficient.text

def get_equipment_id():
    node_root = getXMLSettings()
    node_son_equipment_id = node_root.find(SETTING_XML_VALUE_TYPE_EQUIPMENT_ID)
    return node_son_equipment_id.text

def get_TCP_settings():
    node_root = getXMLSettings()
    node_son_tcp_ip = node_root.find(SETTING_XML_VALUE_TYPE_TCP_IP)
    node_son_tcp_port = node_root.find(SETTING_XML_VALUE_TYPE_TCP_PORT)
    return node_son_tcp_ip.text,node_son_tcp_port.text

def get_channel_num():
    node_root = getXMLSettings()
    node_son_channel_num = node_root.find(SETTING_XML_VALUE_CHANNEL_NUM)
    return node_son_channel_num.text

def get_timeout():
    node_root = getXMLSettings()
    node_son_timeout = node_root.find(SETTING_XML_VALUE_TIMEOUT)
    return node_son_timeout.text

def output_log_message(msg):
    log_file = open(LOG_FILE_PATH,'a+')
    log_file.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]+" ")
    log_file.write(msg+"\n")
    log_file.close()

def save_value_to_setting_xml(value_type, str_value):
    print(str_value)
    read_tree = ET.parse(SETTING_XML_PATH)
    node_root = read_tree.getroot()
    node_son = node_root.find(value_type)
    node_son.text=str_value        
    read_tree.write(SETTING_XML_PATH)

def create_setting_xml():
    
    global SETTING_XML_PATH
    print ('create %s...'%SETTING_XML_PATH)
    
    #创建xml文件
    #创建根节点
    node_root = ET.Element("Setting")
    
    #创建子节点，并添加属性

    node_son_equipment_id = ET.SubElement(node_root, SETTING_XML_VALUE_TYPE_EQUIPMENT_ID)
    node_son_equipment_id.text = INIT_EQUIPMENT_ID

    node_son_password = ET.SubElement(node_root, SETTING_XML_VALUE_TYPE_PASSWORD)
    node_son_password.text = INIT_PASS_WORD

    #1
    node_son_upper_value = ET.SubElement(node_root, SETTING_XML_VALUE_TYPE_UPPER_VALUE)
    node_son_upper_value.text = INIT_UPPER_VALUE

    node_son_upper_value_2sv = ET.SubElement(node_root, SETTING_XML_VALUE_TYPE_UPPER_VALUE_2SV)
    node_son_upper_value_2sv.text = INIT_UPPER_VALUE_2SV

    node_son_upper_value_3sv = ET.SubElement(node_root, SETTING_XML_VALUE_TYPE_UPPER_VALUE_3SV)
    node_son_upper_value_3sv.text = INIT_UPPER_VALUE_3SV

    node_son_upper_value_4sv = ET.SubElement(node_root, SETTING_XML_VALUE_TYPE_UPPER_VALUE_4SV)
    node_son_upper_value_4sv.text = INIT_UPPER_VALUE_4SV

    #2
    node_son_lower_value = ET.SubElement(node_root, SETTING_XML_VALUE_TYPE_LOWER_VALUE)
    node_son_lower_value.text = INIT_LOWER_VALUE

    node_son_lower_value_2sv = ET.SubElement(node_root, SETTING_XML_VALUE_TYPE_LOWER_VALUE_2SV)
    node_son_lower_value_2sv.text = INIT_LOWER_VALUE_2SV

    node_son_lower_value_3sv = ET.SubElement(node_root, SETTING_XML_VALUE_TYPE_LOWER_VALUE_3SV)
    node_son_lower_value_3sv.text = INIT_LOWER_VALUE_3SV

    node_son_lower_value_4sv = ET.SubElement(node_root, SETTING_XML_VALUE_TYPE_LOWER_VALUE_4SV)
    node_son_lower_value_4sv.text = INIT_LOWER_VALUE

    node_son_calib_coefficient = ET.SubElement(node_root, SETTING_XML_VALUE_TYPE_CALIBRATION_COEFFICIENT)
    node_son_calib_coefficient.text = INIT_CALIB_COEFFICIENT

    #3
    node_son_calib_weight = ET.SubElement(node_root, SETTING_XML_VALUE_TYPE_CALIB_WEIGHT)
    init_calib_weight_list = INIT_CALIB_WEIGHT.split(",")
    for i in range(len(init_calib_weight_list)):
        child = ET.Element('c%d'%(i+1))
        child.text = init_calib_weight_list[i]
        node_son_calib_weight.append(child)

    #4
    node_son_calib_rawdata = ET.SubElement(node_root,SETTING_XML_VALUE_TYPE_CALIB_RAWDATA)
    for i in range(len(init_calib_weight_list)):
        child = ET.Element('c%d'%(i+1))
        child.text = '0'
        node_son_calib_rawdata.append(child)

    #5
    node_son_calib_result = ET.SubElement(node_root,SETTING_XML_VALUE_TYPE_CALIB_RESULT)
    child_slope = ET.Element(SETTING_XML_VALUE_TYPE_CALIB_RESULT_SLOPE)
    child_slope.text = INIT_CALIB_RESULT_SLOPE
    child_intercept = ET.Element(SETTING_XML_VALUE_TYPE_CALIB_RESULT_INTERCEPT)
    child_intercept.text = INIT_CALIB_RESULT_INTERCEPT
    node_son_calib_result.append(child_slope)
    node_son_calib_result.append(child_intercept)

    #6
    node_son_total_count = ET.SubElement(node_root, SETTING_XML_VALUE_TYPE_TOTAL_COUNT)
    node_son_total_count.text = "0"

    node_son_tcp_ip = ET.SubElement(node_root, SETTING_XML_VALUE_TYPE_TCP_IP)
    node_son_tcp_ip.text = INIT_TCP_IP

    node_son_tcp_port = ET.SubElement(node_root, SETTING_XML_VALUE_TYPE_TCP_PORT)
    node_son_tcp_port.text = INIT_TCP_PORT

    node_son_channel_num = ET.SubElement(node_root, SETTING_XML_VALUE_CHANNEL_NUM)
    node_son_channel_num.text = INIT_CHANNEL_NUM

    node_son_timeout = ET.SubElement(node_root, SETTING_XML_VALUE_TIMEOUT)
    node_son_timeout.text = INIT_TIMEOUT

    #创建elementtree对象，写文件
    new_tree = ET.ElementTree(node_root)
    new_tree.write(SETTING_XML_PATH, xml_declaration=True)
    output_log_message("create_setting_xml......done!")


def save_value_to_setting_xml(value_type, str_value):
    global SETTING_XML_PATH
    ##    print 'save {value_type} to {path}......'.format(value_type=value_type,path=SETTING_XML_PATH)
    read_tree = ET.parse(SETTING_XML_PATH)
    node_root = read_tree.getroot()
    node_son = node_root.find(value_type)
    node_son.text=str_value
    read_tree.write(SETTING_XML_PATH)

def save_data(file_content):
    cur_data_file_path = get_current_data_file_path()
    data_file = open(cur_data_file_path, 'a+')
    # file_content = str(current_datetime) + ' ' +str_tmp_EquipmentID+' '+ '%.2f'%current_pressure + ' N ' + '  TotalCount:%d'%tmp_TotaL_Count
    data_file.write(file_content + '\n')
    data_file.close()

def get_current_data_file_path():
    return DataFile_Init()


def DataFile_Init():
    cur_year, cur_month, cur_day = get_current_datetime_Year_Month_Day()

    second_folder = DATA_FOLDER_PATH + '/' + str(cur_year)
    third_folder = second_folder + '/' + str(cur_month)
    data_file_name = datetime.now().strftime('%Y%m%d') + ".txt"
    data_file_path = third_folder + '/' + str(data_file_name)

    check_data_folders_exists(DATA_FOLDER_PATH, second_folder, third_folder)
    if not os.path.exists(data_file_path):
        data_file = open(data_file_path, 'w')
        data_file.close()

    return data_file_path

def get_current_datetime_Year_Month_Day():
    cur_datetime = datetime.now()
    cur_year = cur_datetime.year
    cur_month = cur_datetime.month
    cur_day = cur_datetime.day

    return cur_year, cur_month, cur_day

def check_data_folders_exists(root_folder,second_folder,third_folder):
    if not os.path.exists(root_folder):
        os.mkdir(root_folder)

    if not os.path.exists(second_folder):
        os.mkdir(second_folder)

    if not os.path.exists(third_folder):
        os.mkdir(third_folder)

def init_global_var():
    globalVal.global_start_time = datetime.now()
    ## first:value;second:time;third:isCollected;fourth:count;fifth:isAlarm;six:is_Start;seven:temp ###
    globalVal.global_dict = {0: ['0', datetime.now().strftime(DATE_FORMAT), False, 0, False , False, '0'],
                   1: ['0', datetime.now().strftime(DATE_FORMAT), False, 0, False, False, '0'],
                   2: ['0', datetime.now().strftime(DATE_FORMAT), False, 0, False, False, '0'],
                   3: ['0', datetime.now().strftime(DATE_FORMAT), False, 0, False, False, '0']}
    # globalVal.global_dict = globalVal.global_dict_bak

class globalVal:
    global_start_time = datetime.now()
    ### first:value;second:time;third:isCollected;fourth:count;fifth:isAlarm；six:isStartSignal;seven:temp###
    global_dict = {0: ['0', datetime.now().strftime(DATE_FORMAT), False, 0, False, False, '0'],
                   1: ['0', datetime.now().strftime(DATE_FORMAT), False, 0, False, False, '0'],
                   2: ['0', datetime.now().strftime(DATE_FORMAT), False, 0, False, False, '0'],
                   3: ['0', datetime.now().strftime(DATE_FORMAT), False, 0, False, False, '0']}
    # global_dict_bak = {0: ['0', datetime.now().strftime(DATE_FORMAT),False,0,False,False, '0'],
    #                1: ['0', datetime.now().strftime(DATE_FORMAT),False,0,False,False, '0'],
    #                2: ['0', datetime.now().strftime(DATE_FORMAT),False,0,False,False, '0'],
    #                3: ['0', datetime.now().strftime(DATE_FORMAT),False,0,False,False, '0']}

    global_status = ""
    global_isStart = False
    global_currentCount = 0
    global_TotalCount = 0
    global_calibration = 0.0
    global_tcp_ip = '0.0.0.0'
    global_tcp_port = '54321'
    is_Collected = False
    PSN = ''
    Equipment_ID = ''
    system_IP=""