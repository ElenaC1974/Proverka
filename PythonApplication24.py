# -*- coding: cp1251 -*-
class Transport:
    def __init__(self, name, max_speed, mileage):
        
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Transport):
          
     def __init__(self, name, max_speed, mileage):
            
            super().__init__(name, max_speed, mileage)
            
     def __str__(self):
            return "�������� ����������: "+self.name+" ��������: "+str(self.max_speed)+" ������: "+str(self.mileage)
bus=Bus("Renault Logan", 180, 12)
print(bus)
