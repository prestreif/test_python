#!/usr/bin/env python3.6

import pexpect
import argparse
from getpass import getpass
import re
from pprint import pprint

## lib telnet with pexpect

def login_telnet(t, login, passwd, with_login="login"):
    '''
    Производит авторизацию
    на вход ожидает:
        t - handle объекта с сессией pexpect.spawn
        login - username
        passwd - pasword для username
    '''
    t.expect(with_login)
    t.sendline(login)
    t.expect('[Pp]ass')
    t.sendline(passwd)
    if t.expect(['[Ff]ailed', 'incorrect', '[>#]']) < 2:
        print("Неверный логин или пароль!")
        return False
    else:
        #t.sendline('terminal length 0')
        t.sendline('configure terminal length 0')
        t.expect('[>#]')
        t.sendline('exit')
        t.expect('[>#]')
        t.sendline('exit')
        t.expect('[>#]')
        return True

def cmd_telnet(t, cmd, end):
    '''
    Отсылает команду и считывает до указанного вырожения
    на вход ожидает:
        t - handle объекта с сессией pexpect.spawn
        cmd - команда которую нужно выполнить
        end - считывает до этих символов
    '''
    istr = ""
    t.sendline(cmd)
    t.expect('\r\n')

    line = t.before.decode("utf-8")

    regex = ['>', '#']

    while not re.search(end, line):
        istr += line
        i = t.expect(regex)
        line = t.before.decode('utf-8') + regex[i]

    istr += line

    return istr

####

def str_to_dict(istr):
    return {line for line in istr.split("\r\n")}#{line.split()[:1]: line.split()[1:] 
           # for lines in istr.split("\r\n") for line in lines } 

def telnet(ip, port, command):
    login = input('login as: ')
    passwd = getpass(prompt="password: ")
    print("Подключение к устройству {}:{}".format(ip, port))
    with pexpect.spawn("telnet {} {}".format(ip, port)) as t:
        if not login_telnet(t, login, passwd):
            print("Неверный логи/пароль")
            return False
        print("Авторизация прошла успешно")
        print(cmd_telnet(t, command, '\r\n\S+[>#]'))

        

if __name__ == "__main__":
    parser =  argparse.ArgumentParser(description='telnet test')
    parser.add_argument('ip', action="store", help="ip distination address")
    parser.add_argument('command', action="store", help="command")
    parser.add_argument('-p', action="store", help="port", dest='port', default=23, type=int)

    args = parser.parse_args()

    telnet(args.ip, args.port, args.command)

