# -*- coding: cp1251 -*-
class Transport:

 def __init__(self, name, max_speed, mileage):

  self.name = name

  self.max_speed = max_speed

  self.mileage = mileage

 def seating_capacity(self, capacity):

  return f"����������� ������ �������� {self.name} {capacity} ����������"

class Autobus(Transport):

 def seating_capacity(self, capacity = 50):
  return super ().seating_capacity (capacity = 50)
  
School_bus = Autobus("School Volvo", 180, 12)

print(School_bus.seating_capacity())