#!/usr/bin/env python3
fahrenheit = 0
print("Fahrenheut Celsius")
while fahrenheit <= 250:
    celsius = (fahrenheit - 32) / 1.8   # 转换为摄氏度
    print("{:5d}{:7.2f}".format(fahrenheit,celsius))
    fahrenheit += 1
