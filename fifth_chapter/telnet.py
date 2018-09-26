#!/usr/bin/env python3.6

import pexpect
from getpass import getpass
from pprint import pprint
import re
import argparse



def valid_end(line, stop_re):
    return True if re.search(stop_re, line) else False

def telnet_rstr(t, stop_re, exp = ['#', '>']):
    iD = t.expect(exp)
    line = t.before.decode('utf-8') + exp[iD]
    istr = ""
    while not valid_end(line, stop_re):
        istr = istr + line
        iD = t.expect(exp)
        line = t.before.decode('utf-8') + exp[iD]

    print('-' * 30)
    return istr + line

def telnet(ip, port, command, LOGIN, PASSWD):
    regex_host = '\r\n\s*\S+[#>]'
    with pexpect.spawn("telnet {} {}".format(ip, port)) as t:
        print(telnet_rstr(t, '[Ll]ogin.*:', [':']))
        t.sendline(LOGIN)
        print(telnet_rstr(t, '[Pp]ass.*:', [':']))
        t.sendline(PASSWD)
        print(telnet_rstr(t, regex_host))
        t.sendline(command)

        lines = telnet_rstr(t, regex_host).split('\r\n')

        for key, line in enumerate(lines):
            print(str(key) + ": " + line)
        


if __name__ == "__main__":
    

    print('login: ', end='')
    LOGIN = input()
    PASSWD = getpass()
    telnet('192.168.30.37', 23, 'sh all-command', LOGIN, PASSWD)
