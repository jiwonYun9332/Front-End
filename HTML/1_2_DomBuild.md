# DOM

DOM(Document Object Model)은 웹 페이지에 대한 인터페이지이다. 기본적으로 여러 프로그램들이 페이지의 콘텐츠 및 구조, 그리고 스타일을 읽고 조작할 수 있도록 API를 제공한다.

**웹 페이지가 만들어지는 과정**

웹 브라우저가 원본 HTML 문서를 읽어들인 후, 스타일을 입히고 대화형 페이지로 만들어 뷰 포트에 표시하기까지의 과정을 "Critical Rendering Path"라고 한다.

**CRP(Critical Rendering Path)**

과정

1. DOM 트리 구성
2. CSSOM 트리 구성
3. 자바스크립트 실행
4. 렌더 트리 만들기
5. 레이아웃 생성
6. 페인트

**1. Dom 트리 구성**

DOM(문서 개체 모델)트리는 완전히 구문 분석된 HTML 페이지의 개체 표현이다.

루트 요소부터 시작하여 페이지의 각 요소/텍스트에 대해 노드가 생성된다. 다른 요소 내에 중첩된 요소는 자식 노드로 표시되며 각 노드에는 해당 요소에 대한
전체 속성이 포함된다

**Example)** 

```
<html>
<head>
  <title>Understanding the Critical Rendering Path</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header>
      <h1>Understanding the Critical Rendering Path</h1>
  </header>
  <main>
      <h2>Introduction</h2>
      <p>Lorem ipsum dolor sit amet</p>
  </main>
  <footer>
      <small>Copyright 2017</small>
  </footer>
</body>
</html>
```
<br>

![DOM 트리](https://github.com/openstack9332/web_roadmap/blob/509d9dfe6c22d879cd6171366d2cf05134efb7d7/HTML/images/image9.png)
  
**2. CSSOM 트리 구성**

CSSOM(CSS Object Model)은 DOM과 관련된 스타일의 객체 표현이다. DOM과 유사한 방식으로 표현되지만 명시적으로 선언되거나 암시적으로 상속되는지 여부에 관계없이 각 노드에
대한 관련 스타일이 포함된다.

**Example)**

```
body { font-size: 18px; }

header { color: plum; }
h1 { font-size: 28px; }

main { color: firebrick; }
h2 { font-size: 20px; }

footer { display: none; }
```

<br>

![CSSOM 트리](https://github.com/openstack9332/web_roadmap/blob/d747b352690c40de6ea1bb2c38c6829341158fc4/HTML/images/image10.png)

CSS는 "렌더링 차단 리소스"로 간주된다. 이는 리소스를 완전히 파싱하지 않고는 렌더 트리를 구성할 수 없음을 의미한다.

CSS는 **스크립트 차단**일 수도 있다. JavaScript 파일은 CSSOM이 구성될 때까지 기다려야 실행할 수 있기 때문이다.

CSS, JavaScript는 **렌더링 차단 리소스**로 간주된다.

**3. JavaScript**

JavaScript는 세 번째 단계로 정리되어 있지만, 사실 JavaScript는 첫 번째 단계인 DOM 구성 중에 일어날 수 있다. 

웹 브라우저는 CRP 과정을 거치며, DOM Tree를 구성하는데 이때 script 태그 또는 외부 script 참조 구문을 만나면, DOM Tree를 구성하던 작업이 중지되고 script가 먼저 실행된다.

이러한 특성 때문에 JavaScript는 '렌더링 차단 리소스'로 분류되며, HTML 작성 시 script 태그는 각 엘리먼트에 대한 정의가 모두 끝난 뒤 마지막에 작성하는 것이 권장된다.

**4. 렌더 트리 생성**

렌더 트리는 DOM과 CSSOM의 조합이다. 페이지에 최종적으로 렌더링될 내용을 나타내는 트리이다. 

즉, 보이는 콘텐츠만 캡처하고 예를 들어 CSS를 사용하여 숨겨진 요소는 포함하지 않는다. **display: none**

![렌더 트리 생성](https://github.com/openstack9332/web_roadmap/blob/261d9c628de69ab3e9b0e873917737504111eb84/HTML/images/image11.png)

**5. 레이아웃 생성**

레이아웃은 뷰포트의 크기를 결정하는 것으로 이에 종속된 CSS 스타일에 대한 컨텍스트를 제공한다. (예: 백분율 또는 뷰포트 단위)

표시 영역 크기는 문서 헤드에 제공된 메타 표시 영역 태그에 의해 결정되며, 태그가 제공되지 않으면 기본 표시 영역 너비인 980PX가 적용된다.

예를 들어, 가장 일반적인 메타 뷰포트 값은 장치 너비에 해당하도록 뷰포트 크기를 설정하는 것이다.

```
<meta name="viewport" content="width=device-width,initial-scale=1">
```

**6. 페인팅**

마지막으로 페인팅 단계에서 페이지의 보이는 내용을 화면에 표시할 픽셀로 변환할 수 있다.

페인트 단계에 걸리는 시간은 DOM의 크기와 적용되는 스타일에 따라 다르다.

<참고 자료>

[1](https://wit.nts-corp.com/2019/02/14/5522)









