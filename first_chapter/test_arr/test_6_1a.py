#!/usr/bin/env python3.6

word_ip = ""
while 1:
    ip = input("Введите ip адрес{}: ".format(word_ip))
    
    ip = ip.split('.')

    try:
        ip = [int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])]
    except:
        pass
    else:
        if 255 >= ip[0] >= 0 and 255 >= ip[1] >= 0 and 255 >= ip[2] >= 0 and 255 >= ip[3] >= 0:
            break 

    print("Неверный формат ввода\nвводите пожалуйста только цифры разделяя их точками\nВот так: 8.8.8.8\n")
    word_ip = " еще раз"


if ip[0] == ip[1] == ip[2] == ip[3] == 0:
    print("ip => unassigned")
elif ip[0] == ip[1] ==  ip[2] == ip[3] == 255:
    print("ip => local broadcast")
elif 239 >=  ip[0] >= 224:
    print("ip => multicast")
elif 223 >= ip[0] >= 1:
    print("ip => unicast")
else:
    print("ip => unused")
        

