# -*- coding: cp1251 -*-
slovo=input("������� ����� � �������� �������")
e=slovo.count('e') 
a=slovo.count('a') 
i=slovo.count('i') 
u=slovo.count('u')
o=slovo.count('o') 

schetglas=e+a+i+u+o 

print("����� �������",schetglas) 

print("����� ���������",len(slovo)-schetglas)  
if(e==0):

 print("������� e � ����� False")

else:

 print("e=",e)

if(u==0):

 print("������� u � ����� False")

else:

 print("u=",u)

if(o==0):

 print("������� o � ����� False")

else:

 print("o=",o)

if(a==0):

 print("������� a � ����� False")

else:

 print("a=",a)

if (i==0):

 print("������� i � ����� False")

else:

 print("i=",i)
