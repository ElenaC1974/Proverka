# -*- coding: cp1251 -*-
pets ={}
pets2={}
while (True):
 k=input("������� ��� �������(������� enter - �����):")
 if k =='':
  break
 else:
  k1=input('��� �������:')
  k2=int(input('������� �������:'))
  year_case = ''
 if k2 % 10 == 1 and k2 != 11 and k2 % 100 != 11:
  year_case = '���'
 elif 1 < k2 % 10 <= 4 and k2 != 12 and k2 != 13 and k2 != 14:
  year_case = '����'
 else:
  year_case = '���'
 k3=input('��� ���������:')
 pets2={'��� �������:':k1, '������� �������:':k2, '��� ���������:':k3}
 pets[k]=pets2
 for key in pets.keys():
  print("���", pets2['��� �������:'], "�� ������", key,". ������� �������:", pets2['������� �������:'], year_case, "��� ���������:", pets2['��� ���������:'])