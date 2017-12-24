# ROOT Ransomware

###### 991p

>해커가 c:/root_ransomware 에 있는 모든 파일을 암호화 시켜놓았다 
>
>해당 랜섬웨어 실행파일을 분석하여 파일을 복호화하자 
>
>[HINT](https://drive.google.com/file/d/1dvo3NPjEd8N1Qoiu8Z0tw5JLFsg5DHpa/view?usp=sharing)
>
>[Link](https://drive.google.com/file/d/1CyVwCb17chmubWbx2pBd1lFI_i-suWPD/view?usp=sharing)

-------

랜섬웨어인데 참 다행이도 따로 암호화되는 폴더가 있다.

우선 쫙쫙 분석해주면 0x4657E0에 암호화 함수가있다.

이 암호화 소스를 파이썬으로 만들어 보면 다음과 같다.

```python
from ctypes import *

msvcrt = CDLL("MSVCRT.DLL")
msvcrt.srand(0x3039)
tstarr = [0xFF, 0xFE, 3, 4,7,2,234]#테스트 파일
tstarr = list(map(c_byte,tstarr))
cryptarr = [0x7F]

for i in range(len(tstarr)):
    tstarr[i] = c_int32(tstarr[i].value+(msvcrt.rand() % 255 + 1))
    tstarr[i] = c_int32(tstarr[i].value ^ cryptarr[i])
    cryptarr.append(cryptarr[i] ^ tstarr[i].value)

tstarr = list(map(lambda x:x.value,tstarr))
print(list(map(hex,tstarr)))
print(cryptarr)
```

따라서 이를 역연산하는 소스를 짜면 다음과 같다.

```python
from ctypes import *
msvcrt = CDLL("MSVCRT.DLL")

def decrypt(filecontent):
    msvcrt.srand(0x3039)
    tstarr = list(map(c_ubyte, filecontent))
    cryptarr = [0x7F]
    for i in range(len(tstarr)):
        cryptarr.append(cryptarr[i] ^ tstarr[i].value)
        tstarr[i] = c_ubyte(tstarr[i].value ^ cryptarr[i])
        tstarr[i] = c_ubyte(tstarr[i].value - (msvcrt.rand() % 255 + 1))
    return bytes(map(lambda x: x.value, tstarr))
```

이를 이용해서 파일들을 일일히 복호화한후에 파일 시그니쳐에 맟춰서 확장자를 바꿔주면 한글자씩 플래그가 나온다.

사용된 소스는 다음과 같다.

````python
from ctypes import *
msvcrt = CDLL("MSVCRT.DLL")

def decrypt(filecontent):
    msvcrt.srand(0x3039)
    tstarr = list(map(c_ubyte, filecontent))
    cryptarr = [0x7F]
    for i in range(len(tstarr)):
        cryptarr.append(cryptarr[i] ^ tstarr[i].value)
        tstarr[i] = c_ubyte(tstarr[i].value ^ cryptarr[i])
        tstarr[i] = c_ubyte(tstarr[i].value - (msvcrt.rand() % 255 + 1))
    return bytes(map(lambda x: x.value, tstarr))

if __name__=="__main__":
    folderlist=["one","two","three","four","five"]
    for curfolder in folderlist:
        for curfile in range(1,5):
            with open(r'root_ransomware\%s\%d.root'%(curfolder,curfile),'rb') as k:
                tstarr = k.read()
                with open(r'root_ransomware\%s\%d.origin'%(curfolder,curfile),"w+b") as j:
                    j.write(decrypt(tstarr))
````

-------------

FLAG는 `FLAG{Danger_encrypt}`이다.