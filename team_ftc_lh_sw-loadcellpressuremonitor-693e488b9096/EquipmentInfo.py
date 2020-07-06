
class EquipmentInfo:
    
    def __init__(self):
        self.EquipmentID=""
        self.IP=""
        self.PSN=""
        self.TotalCount=0
        self.PressureUpper="00"
        self.PressureLower="00"
        self.CalibrationCoefficient=1
        
    def set_CalibrationCoefficient(self,CalibrationCoefficient):
        self.CalibrationCoefficient=CalibrationCoefficient
    
    def set_EquipmentID(self,EquipmentID):
        self.EquipmentID=EquipmentID
        
    def set_IP(self,IP):
        self.IP=IP
        
    def set_PSN(self,PSN):
        self.PSN=PSN
        
    def set_TotalCount(self,TotalCount):
        self.TotalCount=TotalCount
        
    def set_PressureLower(self,PressureLower):
        self.PressureLower=PressureLower
        
    def set_PressureUpper(self,PressureUpper):
        self.PressureUpper=PressureUpper
        
    def get_EquipmentID(self):
        return self.EquipmentID

    def get_IP(self):
        return self.IP

    def get_TotalCount(self):
        return self.TotalCount

    def get_PSN(self):
        return self.PSN

    def get_TPressureUpper(self):
        return self.PressureUpper

    def get_PressureLower(self):
        return self.PressureLower
    
    def get_CalibrationCoefficient(self):
        return self.CalibrationCoefficient
    
    equipmentID=property(set_EquipmentID,get_EquipmentID)
