#! /usr/bin/python3

from os import system

while True:
    command = input('Command: ').split(' ')
    if command == ['']:
        exit()
    elif command[0] == 'open' or command[0] == 'o':
        system('sudo iptables -D INPUT -j DROP')
        system('sudo iptables -A INPUT -p tcp --dport ' + command[1] + ' -j ACCEPT')
        system('sudo iptables -A INPUT -j DROP')
    elif command[0] == 'close' or command[0] == 'c':
        system('sudo iptables -D INPUT -j DROP')
        system('sudo iptables -A INPUT -p tcp --dport ' + command[1] + ' -j DROP')
        system('sudo iptables -A INPUT -j DROP')
    elif command[0] == 'show':
        system('sudo iptables -L --line-numbers')
    else:
        print('Command not found')
