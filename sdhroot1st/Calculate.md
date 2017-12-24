# Calculate

######167p

>누가 내 패스워드좀 알려줘!
>hint : 역연산
>
>[Link](https://drive.google.com/file/d/1HnAD-pRQx9AvveLmckZ1qjCuBkMJ3cam/view)

-----------

```python
def one(num, size):
    r = num + size
    r += 915
    return r


def two(num, size):
    r = num - size
    r -= 372
    return r


def three(num, size):
    r = num ^ size
    r ^= 826
    return r


def four(num, size):
    size %= 32
    r = num >> (32 - size)
    b = (num << size) - (r << 32)
    return b + r


if __name__ == "__main__":
    result = [5040, 4944, 5088, 4992, 7232, 4848, 7584, 7344, 4288, 7408, 7360, 7584, 4608, 4880, 4320, 7328, 7360,
              4608, 4896, 4320, 7472, 7328, 7360, 4608, 4752, 4368, 4848, 4608, 4848, 4368, 4944, 7200]
    string = raw_input("Input String : ")
    Number = []
    tmp = 0

    for i in string:
        Number.append(ord(i))

    for i in Number:
        Number[tmp] = one(i, 100)
        tmp += 1
    tmp = 0

    for i in Number:
        Number[tmp] = two(i, 100)
        tmp += 1
    tmp = 0

    for i in Number:
        Number[tmp] = three(i, 100)
        tmp += 1
    tmp = 0

    for i in Number:
        Number[tmp] = four(i, 100)
        tmp += 1

    print Number
    if Number == result:
        print "Correct!!"
    else:
        print "Incorrect.."
```

라는 소스코드를 준다.

실행해보면 입력받은 문자열을 각각 one,two,three,four로 연산후 result랑 비교하는데 나는 게으르기 때문에 역연산코드를 안짜고 그냥 한글자씩 맟추게하는 소스를 짜서 풀었다.

풀이소스는 다음과 같다.

```python
def one(num, size):
    r = num + size
    r += 915
    return r
def two(num, size):
    r = num - size
    r -= 372
    return r
def three(num, size):
    r = num ^ size
    r ^= 826
    return r
def four(num, size):
    size %= 32
    r = num >> (32 - size)
    b = (num << size) - (r << 32)
    return b + r

if __name__ == "__main__":
    result = [5040, 4944, 5088, 4992, 7232, 4848, 7584, 7344, 4288, 7408, 7360, 7584, 4608, 4880, 4320, 7328, 7360,
              4608, 4896, 4320, 7472, 7328, 7360, 4608, 4752, 4368, 4848, 4608, 4848, 4368, 4944, 7200]
    tmp = 0
    answer=""
    for i in result:
        for j in range(0,256):
            if four(three(two(one(j, 100),100),100),100)==i:
                answer+=chr(j)
    print(answer)
```

실행하게되면 `FLAG{Rev3rse_P1us_M1nus_X0R_R0L}`라고 나온다.

--------------

FLAG는 `FLAG{Rev3rse_P1us_M1nus_X0R_R0L}`이다.