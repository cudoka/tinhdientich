import math

a = float(input("Nhập vào độ dài cạnh thứ nhất : "))
b = float(input("Nhập vào độ dài cạnh thứ hai : "))
c = float(input("Nhập vào độ dài cạnh thứ ba : "))

s = (a+b+c)/2

dien_tich = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Diện tích của tam giác: " + str(dien_tich))