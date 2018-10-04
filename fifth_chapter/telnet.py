#!/usr/bin/env python3.6

import pexpect
from getpass import getpass

base_tel = ['\r\n\s*\S#', '\r\n\s*\S>']
dev_tel = {'luminato': "Login incorrect"}


def telnet(ip, port, login, passwd, commands, exp, exp_falure=2):
    with pexpect.spawn("telnet {} {}".format(ip, port)) as t:
        try:
            t.expect('[Ll]ogin\s*a?s?:')
            print('Ввод логина: {}'.format(login))
            t.sendline(login)
            t.expect('[Pp]assword:')
            print("Ввод пароля")
            t.sendline(passwd)
            iD = t.expect('\r\n *\w#')
            print("Совпало вырожение: {}".format(exp[iD]))
            t.sendline(commands)
            iD = t.expect(exp)
            print("Совпало вырожение: {}".format(exp[iD]))
            print("Вывод комманды {}:".format(commands))
            print(t.before.decode('utf-8'))

        except pexpect.TIMEOUT:
            print("Время ожидания отклюика от сервера истекло")
            return

if __name__ == "__main__":
    telnet("192.168.30.37", "23", input("Введите логин: "), getpass(prompt='Введите пароль: '), "sh ver", base_tel) 
