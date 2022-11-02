# BOM

브라우저 객체 모델(Browser Object Model)

Brower 객체

- Window : 모든 객체가 소속된 객체이며, 브라우저 창을 의미한다.

- document : 현재 문서에 대한 정보를 갖고 있는 객체이다.

- history : 현재의 브라우저가 접근했던 URL history를 제어할 수 있다.

- location : 문서의 주소와 관련된 객체로 window 객체의 프로퍼티인 동시에 document의 프로퍼티이다. 이 객체를 이용하여 윈도우의 문서 URL을 변경할 수 있고, 
문서의 위치와 관련해서 다양한 정보를 얻을 수 있다.
 
- screen : 사용자의 디스플레이 화면에 대한 다양한 정보를 갖고 있는 객체이다.

- navigator : 실행 중인 애플리케이션(브라우저)에 대한 정보를 알 수 있다. 크로스 브라우징 이슈를 해결할 때 사용할 수 있다. 

  EX) Chrome -> addEventListener, IE -> attachEvent

**Example)**

**window**

네이버 웹 사이트 새 창 열기

```
window.open("http://naver.com") 

or 

open("http://naver.com") 
```

현재 브라우저 닫기

```
window.close()

or

close()
```

알림 발생

```
window.alert("경고!")

or

alert("경고!")
```

**document**

**id**에 해당하는 객체 가져오기

```
document.querySelector('#id')
```

**history**

이전 사이트 or 이후 사이트 이동 

```
history.back()

or

history.forward()
```

**location**

현재 호스트 네임 가져오기

```
location.host
```

구글 웹 사이트로 이동

```
location.href = 'http://google.com'
```

**screen**

현재 디스플레이 정보를 가져옴

```
console.dir(screen)
```

출력결과

```
Screen
  availHeight: 1032
  availLeft: 1920
  availTop: 0
  availWidth: 1920
  colorDepth: 24
  height: 1080
 orientation: ScreenOrientation {angle: 0, type: 'landscape-primary', onchange: null}
 pixelDepth: 24
 width: 1920
 [[Prototype]]: Screen
```

**navigator**

```
navigator.geolocation.getCurrentPosition(function(pos){
var crd = pos.coords;

  console.log('Your current position is:');
  console.log(`Latitude : ${crd.latitude}`);
  console.log(`Longitude: ${crd.longitude}`);
  console.log(`More or less ${crd.accuracy} meters.`);
})
```

<참고 자료>

[1](https://www.youtube.com/watch?v=3c4xp8U3jjM)


