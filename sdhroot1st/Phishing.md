# Phishing

###### 600p

>문제에 오류가 있을수도...
>
>Hint1 : 꺠진 문자열이 플레그일수도,,,
>
>[Link](http://sdhsroot.kro.kr/Phishing/)

-----------

링크에 준 웹사이트를 좀 뒤적거리다보면 `http://sdhsroot.kro.kr/Phishing/asd.php`에서  JS로 플래그는 소스속에 있다고 알려준다. 

JS가 obfuscate 되어있어서 deobfuscate시켜주어야 한다.

http://deobfuscatejavascript.com/이 사이트에서 했다.

```javascript
var b = 200;
for (a = 0; a <= 20; a++) {
    b = b + ((a * b) - (a / b));
    if (a == 0) b = 70;
    else if (a == 1) b = 76;
    else if (a == 3) b = 71;
    else if (a == 2) b = 65;
    else if (a == 4) b = 123;
    else if (a == 20) b = 125;
    else if (a == 5) {
        continue
    } else if (a == 6) {
        alert("코");
        continue
    } else if (a == 7) {
        alert("드");
        continue
    } else if (a == 8) {
        alert("속");
        continue
    } else if (a == 9) {
        alert("에");
        continue
    } else if (a == 10) {
        alert(".");
        continue
    } else if (a == 11) {
        alert(".");
        continue
    } else if (a == 12) {
        alert(".");
        continue
    } else if (a >= 4 && a <= 20) {
        continue
    }
    alert(String.fromCharCode(b))
}
```

deobfuscate한 코드는 저리생겼고 그걸 수정한 코드는

```javascript
var b = 200;
var flfl="";
for (a = 0; a <= 20; a++) {
    b = b + ((a * b) - (a / b));
    if (a == 0) b = 70;
    else if (a == 1) b = 76;
    else if (a == 3) b = 71;
    else if (a == 2) b = 65;
    else if (a == 4) b = 123;
    else if (a == 20) b = 125;
    flfl+=(String.fromCharCode(b))
}
var els=document.getElementsByName("answer");
for (var i=0;i<els.length;i++) {
    els[i].value = flfl;
}
```

위 코드를 플래그 제출하는곳에서 실행시키고 제출하면 된다.

---

FLAG는 `FLAG{ˡᐭꅭ곚삍䘐䣇눛뵼ᩎꓨᶐㆰ}`이다.