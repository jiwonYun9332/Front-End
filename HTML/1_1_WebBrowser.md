# WebBrowser

개요

**월드 와이드 웹**

월드 와이드 웹(World Wide Web, WWW, W3)은 인터넷에 연결된 컴퓨터를 이용해 사람들과 정보를 공유할 수 있는 거미줄(Web)처럼 얼기설기 엮인 공간을 뜻하는 용어다. HTTP 프로토콜을 기반으로 HTML로 작성된 하이퍼텍스트 페이지를 웹 브라우저라는 특정한 프로그램으로 읽을 수 있게 하도록 구성되어 있다

WWW, W3, Web

**인터넷**

인터넷 프로토콜 스위트(TCP/IP)를 기반으로 하여 전 세계적으로 연결되어있는 컴퓨터 네트워크 통신망을 일컫는 말이다.

**브라우저**

HTML 문서와 이미지, 멀티미디어 파일 등 월드 와이드 웹을 기반으로 한 인터넷의 컨텐츠를 검색 및 열람하기 위한 응용 프로그램의 총칭

![인터넷 브라우저 이미지](https://github.com/openstack9332/web_roadmap/blob/cfd7f872663606fc2ac963bce26c9e446746ef98/HTML/images/image1.jpg)

브라우저는 인터넷에서 특정 정보로 이동할 수 있는 주소 입력창(=인터페이스)이 있고, 서버와 HTTP로 정보를 주고 받을 수 있는 네트워크 모듈도 포함하고 있다.

서버에서 받은 문서(HTML, CSS, JavaScript)를 해석하고 실행하여 화면에 표현하기 위한 해석기(Parser)들을 가지고 있다.

**브라우저 역할**

![브라우저 역할](https://github.com/openstack9332/web_roadmap/blob/855c13a901d6850935f02064d468839471e74fb5/HTML/images/image2.png)

1. 사용자가 입력한(원하는) 웹페이지, 이미지, 동영상 등의 자원을 서버에게 요청하는 역할
2. 서버로부터 전달(응답)받은 자원을 화면에 출력하는 역할

**브라우저 구성 요소**

![브라우저 구성 요소](https://github.com/openstack9332/web_roadmap/blob/612202ccb12e0f352f0963410b3b19c714c1220d/HTML/images/image3.png)

<table style="border-collapse: collapse; width: 100%; height: 180px;" border="1">
    <tbody>
        <tr style="height: 60px;">
         <td style="width: 16.5116%; text-align: center; height: 60px;"><b><span style="color: #333333;">User<br>Interface</span></b></td>
         <td style="width: 83.4884%; text-align: justify; height: 60px;"><span style="color: #333333;">&nbsp;- 사용자가 접근할 수 있는 영역이다.<br>&nbsp;- 예를 들어, 검색창, 뒤로가기/앞으로가기 버튼, 새로 고침 버튼 등 브라우저 프로그램 자체의 GUI를 구성하는 부분이다.</span></td>
        </tr>
        <tr style="height: 20px;">
         <td style="width: 16.5116%; text-align: center; height: 20px;"><b>Browser<br>Engine</b></td>
         <td style="width: 83.4884%; text-align: justify; height: 20px;"><span style="color: #333333;"><span style="color: #333333;">&nbsp;- User Interface</span>와 Rendering Engine 사이의 동작을 제어해주는 엔진이다.<br>&nbsp;- 브라우저라는 프로그램의 비즈니스 로직, 핵심 중추 부분이다. <br></span><span style="color: #333333;"><b>&nbsp;- </b>Data Storage를</span><span style="color: #333333;"><span style="color: #333333;"> 참조하며 로컬에 데이터를 쓰고 읽으면서 다양한 작업을 한다.</span></span></td>
        </tr>
        <tr style="height: 20px;">
         <td style="width: 16.5116%; text-align: center; height: 20px;"><b>Rendering Engine</b></td>
         <td style="width: 83.4884%; text-align: justify; height: 20px;"><b>&nbsp;- 요청한 콘텐츠를 화면에 출력하는 역할이다.</b><br><b>&nbsp;- <span style="color: #333333;"> HTML, CSS 등을 파싱하여 최종적으로 화면에 그린다.</span></b></td>
        </tr>
        <tr style="height: 20px;">
         <td style="width: 16.5116%; text-align: center; height: 20px;"><b>Networking</b></td>
         <td style="width: 83.4884%; text-align: justify; height: 20px;">&nbsp;- <span>http 요청을 할 수 있으며 네트워크를 호출할 수 있다.</span></td>
        </tr>
        <tr style="height: 20px;">
         <td style="width: 16.5116%; text-align: center; height: 20px;"><b>JS Engine</b></td>
         <td style="width: 83.4884%; text-align: justify; height: 20px;">&nbsp;- <span>javascript 코드를 해석하고 실행한다.</span></td>
        </tr>
        <tr style="height: 20px;">
         <td style="width: 16.5116%; text-align: center; height: 20px;"><b>UI Backend</b></td>
         <td style="width: 83.4884%; text-align: justify; height: 20px;">&nbsp;- <span>기본적인 위젯을 그리는 인터페이스이다.</span></td>
        </tr>
        <tr style="height: 20px;">
         <td style="width: 16.5116%; text-align: center; height: 20px;"><b>Data Storage</b></td>
         <td style="width: 83.4884%; text-align: justify; height: 20px;">&nbsp;- <span>Local Storage, Indexed DB, 쿠키 등 브라우저 메모리를 활용하여 저장하는 영역이다.</span>&nbsp;</td>
        </tr>
    </tbody>
</table>

<br>

**렌더링 엔진의 동작 원리**

![렌더링 엔진의 동작 원리](https://github.com/openstack9332/web_roadmap/blob/b045d66cfb53a391994176e3f12639354773efa3/HTML/images/image4.png)

1. 브라우저는 서버로부터 HTML 문서를 모두 전달 받는다.

2. 렌더링 엔진은 전달받은 HTML 문서 파싱하여 DOM 트리를 구축한다.

3. 외부 CSS 파일과 함께 포함된 스타일 요소를 파싱한다.

4. DOM 트리와 3의 결과물을 합쳐 렌더 트리를 구축한다.

5. 렌더 트리의 각 노드에 대해서 화면 상에서 어디에 배치할 지 결정한다.

6. UI백엔드에서 렌더 트리를 그리게 되고, 화면에 우리가 볼 수 있도록 출력된다.

<br>

**렌더링 엔진의 동작 과정 예시(웹킷)**

![렌더링 엔진의 동작 과정 예시](https://github.com/openstack9332/web_roadmap/blob/2fc7c77fa61c4d989b621817cf2d8177df3d04bf/HTML/images/image5.png)

<br>

<h3>1. DOM 트리 구축<h3>

![DOM 트리 구축](https://github.com/openstack9332/web_roadmap/blob/a47cae8329edba9a8a8be659aa27c4b5b669fb47/HTML/images/image6.png)

 - 브라우저는 서버로부터 HTML 문서를 모두 전달 받는다.
  
 - 어휘와 구문을 분석하여 HTML 문서를 파싱하고, 파싱 트리를 생성한다. 문서 파싱은 브라우저가 코드를 이해하고 사용할 수 있는 구조로 변환하는 것을 의미한다.
 
 - 파싱 트리를 기반으로 DOM 요소와 속성 노드를 가지는 DOM 트리를 생성한다.
  
<br>

<h3>2. CSSOM(CSS Object Model) 생성 </h3>

![CSSOM 생성](https://github.com/openstack9332/web_roadmap/blob/a47cae8329edba9a8a8be659aa27c4b5b669fb47/HTML/images/image7.png)

- 1의 DOM을 생성할 때 거쳤던 과정을 그대로 CSS에 반복한다.

- 그 결과로 브라우저가 이해하고 처리할 수 있는 형식(Style Rules)으로 변환된다.

<br>
  
<h3>3. 렌더 트리(DOM + CSSOM) 생성

![렌더 트리(DOM + CSSOM) 생성](https://github.com/openstack9332/web_roadmap/blob/a47cae8329edba9a8a8be659aa27c4b5b669fb47/HTML/images/image8.png)

- DOM Tree가 구축이 되어가는 동안 브라우저는 DOM Tree를 기반으로 렌더 트리를 생성한다. 문서를 시각적인 구성 요소로 만들어주는 역할을 한다.
  
<h3>4. 렌더 트리 배치</h3>
  
- 렌더링 트리는 위치와 크기를 가지고 있지 않기 때문에, 객체들에게 위치와 크기를 결정해준다.
  
<h3>5. 렌더 트리 그리기</h3>

- 렌더 트리의 각 노드를 화면의 픽셀로 나타낸다.

- 렌더 트리 그리기가 완료되면, 화면에 콘텐츠가 표현된다.

<참고 자료>
    
[1](https://all-young.tistory.com/22)

[2](https://baegofda.tistory.com/207)

[3](https://velog.io/@exljhun307/%EC%9B%B9-%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%EC%9D%98-%EC%9D%B4%ED%95%B4#13-%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%EC%9D%98-%EA%B5%AC%EC%84%B1-%EC%9A%94%EC%86%8C)














