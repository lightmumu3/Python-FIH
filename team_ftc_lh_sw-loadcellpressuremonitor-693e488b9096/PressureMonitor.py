from GUI_Settings import *
from hx711_3 import *
from load_setting_xml import *
from EquipmentInfo import *


class PressureMonitor(GUI_Settings):

    def __init__(self,parent=None):
        super(PressureMonitor,self).__init__(parent)
        self.monitor_th = None
        self.HX_711_DT_list = [5, 19, 16, 17]
        self.HX_711_SCK_list =[6, 26, 20, 27]

    def start_monitor_pressure(self,num):
        threads = []
        print("start_monitor")
        # self.monitor_th = threading.Thread(target=self.get_hx711_pressure,args=(num,))
        # self.monitor_th.start()
        self.input_th = threading.Thread(target=readInputValue)
        self.input_th.start()

        for i in range(num):
            threads.append(threading.Thread(target=self.get_hx711_pressure_by_num,args=(i,)))
            threads[i].start()

    def get_hx711_pressure_by_num(self,num):
        sensor_dt = self.HX_711_DT_list[num]
        sensor_sck = self.HX_711_SCK_list[num]
        _hx = HX711(sensor_dt, sensor_sck)
        self.HX711_init(_hx)
        while True:
            file_str=str(num)+" : " + str(self.get_Pressure(_hx))
            self.sinOut.emit(str(file_str))
            time.sleep(0.3)


    def get_hx711_pressure(self,num):
        _hx_sensor_list = []
        for i in range(num):
            sensor_dt = self.HX_711_DT_list[i]
            sensor_sck = self.HX_711_SCK_list[i]
            _hx = HX711(sensor_dt, sensor_sck)
            self.HX711_init(_hx)
            _hx_sensor_list.append(_hx)

        while True:
            for i in range(num):
                file_str=str(i)+" : " + str(self.get_Pressure(_hx_sensor_list[i]))
                self.sinOut.emit(str(file_str))
                time.sleep(0.3)


    def HX711_init(self, _hx):
        _hx.set_reading_format("MSB","MSB")
        _hx.set_reference_unit(63)
        _hx.reset()
        _hx.tare()

    def get_Pressure(self, _hx):
        weight = round(_hx.get_weight(5)/1000.0,2)
        pressure = round(weight*9.8*float(globalVal.global_calibration),2)
        _hx.power_down()
        _hx.power_up()
        return pressure

