# Login

##### 50

>로그인 페이지인데 로그인이 안된다...
>
>로그인을 성공하고 짱해커가 되어보자!!
>
>Hint : Array, length<6
>
>Hint2 : Get으로 배열을 전송하는 방법, sql injection
>
>[Link](http://sdhsroot.kro.kr/Login/login.html)

---------

들어가면 소스를 주는데 플래그가 노출되어있다.

````php
<?php
include("dbcon.php");
$pw=$_GET['pw'];
$fpw=$_GET['pw'][1];
if(strlen($fpw)>5){
    echo "<script>alert('no hack~');location.href='login.html'</script>";
}
$query="select * from Login where pw='$fpw'";
$info=mysqli_query($con,$query);
$result=mysqli_fetch_array($info);
if($result['id']){
    setcookie("flag","VmxjeE1FNUdSbk5UV0hCclUwVmFiMWxzVm1GTlZtUnhVbFJXYVZKdGVGcFdSM0JYWWxaV1ZVMUVhejA9");
    echo "<script>location.href='flag.html'</script>";
}
highlight_file("login.php");
````

 저 플래그를 디코드해주면 답이 나온다.

-----------

FLAG는 `FLAG{jjang_easy}`이다.