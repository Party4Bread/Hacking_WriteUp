from pwn import *
#U need to unpack by upx first
e = ELF('./flag')
print e.string(0x496628)#there is var named flag you can find it by gdb
