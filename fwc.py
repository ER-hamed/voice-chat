#! /usr/bin/python3

from os import system

while True:
    system('clear')
    system('sudo iptables -L --line-numbers')
    print('Press enter to exit')
    command = input('Command: ').split(' ')
    if command == ['']:
        exit()
    elif command[0] == 'set':
        system('sudo iptables -D INPUT -j DROP')
        system('sudo iptables -D INPUT -p tcp --dport 22 -j DROP')
        system('sudo iptables -D INPUT -p tcp --dport 22 -j ACCEPT')
        system('sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT')
        system('sudo iptables -D INPUT -p tcp --dport 80 -j DROP')
        system('sudo iptables -D INPUT -p tcp --dport 80 -j ACCEPT')
        system('sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT')
        system('sudo iptables -D INPUT -p tcp --dport 443 -j DROP')
        system('sudo iptables -D INPUT -p tcp --dport 443 -j ACCEPT')
        system('sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT')
        system('sudo iptables -A INPUT -j DROP')
    elif command[0] == 'unset':
        system('sudo iptables -D INPUT -j DROP')
        system('sudo iptables -D INPUT -p tcp --dport 22 -j DROP')
        system('sudo iptables -D INPUT -p tcp --dport 22 -j ACCEPT')
        system('sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT')
        system('sudo iptables -D INPUT -p tcp --dport 80 -j DROP')
        system('sudo iptables -D INPUT -p tcp --dport 80 -j ACCEPT')
        system('sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT')
        system('sudo iptables -D INPUT -p tcp --dport 443 -j DROP')
        system('sudo iptables -D INPUT -p tcp --dport 443 -j ACCEPT')
        system('sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT')
    elif command[0] == 'open' or command[0] == 'o':
        system('sudo iptables -D INPUT -j DROP')
        system('sudo iptables -D INPUT -p tcp --dport ' + command[1] + ' -j DROP')
        system('sudo iptables -D INPUT -p tcp --dport ' + command[1] + ' -j ACCEPT')
        system('sudo iptables -A INPUT -p tcp --dport ' + command[1] + ' -j ACCEPT')
        system('sudo iptables -A INPUT -j DROP')
    elif command[0] == 'close' or command[0] == 'c':
        system('sudo iptables -D INPUT -j DROP')
        system('sudo iptables -D INPUT -p tcp --dport ' + command[1] + ' -j ACCEPT')
        system('sudo iptables -D INPUT -p tcp --dport ' + command[1] + ' -j DROP')
        system('sudo iptables -A INPUT -p tcp --dport ' + command[1] + ' -j DROP')
        system('sudo iptables -A INPUT -j DROP')
    elif command[0] == 'remove' or command[0] == 'r':
        system('sudo iptables -D INPUT -p tcp --dport ' + command[1] + ' -j ACCEPT')
        system('sudo iptables -D INPUT -p tcp --dport ' + command[1] + ' -j DROP')
    elif command[0] == 'help':
        system('clear')
        print('''------------------------------------------------
Opening port:
    open <port>
    o <port>
        
------------------------------------------------
Closing port:
    close <port>
    c <port>
        
------------------------------------------------
Remove rule:
    remove <port>
    r <port>
        
------------------------------------------------
set: open 22, 80, 443 and close all port
        
------------------------------------------------
unset: open 22, 80, 443 and open all port
        ''')
        input('Press enter to back')
    else:
        print('Command not found')
