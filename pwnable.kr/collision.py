from pwn import *
from struct import pack

hashcode = 0x21DD09EC

s = ssh(host='pwnable.kr',
        port=2222,
        user='col',
        password='guest')

hashbase = hashcode//5
hashleft = hashcode%hashbase+hashbase
collisionhash=pack('i',hashbase)*4+pack('i',hashleft)
sh = s.process(argv=['col',collisionhash])
print sh.recvall()