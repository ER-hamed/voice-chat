#! /usr/bin/python3

from os import popen

while True:
    popen('clear')
    popen('sudo iptables -L --line-numbers')
    command = input('Command: ').split(' ')
    if command == ['']:
        exit()
    elif command[0] == 'set':
        popen('sudo iptables -D INPUT -j DROP')
        popen('sudo iptables -D INPUT -p tcp --dport 22 -j ACCEPT')
        popen('sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT')
        popen('sudo iptables -A INPUT -j DROP')
    elif command[0] == 'open' or command[0] == 'o':
        popen('sudo iptables -D INPUT -j DROP')
        popen('sudo iptables -D INPUT -p tcp --dport ' + command[1] + ' -j DROP')
        popen('sudo iptables -D INPUT -p tcp --dport ' + command[1] + ' -j ACCEPT')
        popen('sudo iptables -A INPUT -p tcp --dport ' + command[1] + ' -j ACCEPT')
        popen('sudo iptables -A INPUT -j DROP')
    elif command[0] == 'close' or command[0] == 'c':
        popen('sudo iptables -D INPUT -j DROP')
        popen('sudo iptables -D INPUT -p tcp --dport ' + command[1] + ' -j ACCEPT')
        popen('sudo iptables -D INPUT -p tcp --dport ' + command[1] + ' -j DROP')
        popen('sudo iptables -A INPUT -p tcp --dport ' + command[1] + ' -j DROP')
        popen('sudo iptables -A INPUT -j DROP')
    elif command[0] == 'remove' or command[0] == 'r':
        popen('sudo iptables -D INPUT -p tcp --dport ' + command[1] + ' -j ACCEPT')
        popen('sudo iptables -D INPUT -p tcp --dport ' + command[1] + ' -j DROP')
    else:
        print('Command not found')
