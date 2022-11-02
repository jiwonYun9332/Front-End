# 싱글 페이지 애플리케이션

> SPA 란?
Single Page Appliaction(이하 SPA)은 전통적인 Multi Page Appliaction(이하 MPA)과 다르다. 가장 큰 차이점은 SPA 내비게이션은 단 하나의 웹 페이지에서 이루어진다는 점이다.

기존 웹 서비스는 요청 시마다 서버로부터 리소스들과 데이터를 해석하고 화면에 렌더링하는 방식이다.

SPA형태는 브라우저에 최초에 한 번 페이지 전체를 로드하고, 이후부터는 특정 부분만 Ajax를 통해 데이터를 바인딩하는 방식이다.

> 전통적인 페이지 vs 단일 페이지 애플리케이션 비교

<p align="center">
  <img src="https://github.com/openstack9332/web_roadmap/blob/55db19040113de62125e4751c3b7eafde65403c2/HTML/images/image14.png">
</p>

예전부터 개발자들은 지속적으로 웹 서비스와 개발 방식을 발전시켜왔다. CSS, JS 리소스 등을 CDN 형태로 캐싱 및 압축하고, View에서 **템플릿엔진** 들을 사용하고, 초기의 SPA 개념인 
Backbone.js, Angular.js 라이브러리들이 나왔고, 지금은 템플릿 개념을 지나 컴포넌트 개념인 React.js, Vue.js, Angular2 등 다양한 라이브러리와 프레임워크가 등장하였다.

> 컴포넌트 개념

<p align="center">
  <img src="https://github.com/openstack9332/web_roadmap/blob/55db19040113de62125e4751c3b7eafde65403c2/HTML/images/image15.png">
</p>

위의 이미지 처럼 컴포넌트들이 모여 한 페이지를 작성하고, 특정 부분만 데이터를 바인딩하는 개념이다.

> SPA 구현을 쉽게 말하면 jsp 파일 없이 index.html 파일 하나에서 js, css 등 리소스 파일들과 모듈들을 로드해서 페이지 이동 없이 특정 영역만 새로 모듈을 호출하고 데이터를 바인딩하는
> 개념이다.

<참고 자료>

[1](https://linked2ev.github.io/devlog/2018/08/01/WEB-What-is-SPA/)
