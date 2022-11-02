## JavaScript Library 

> jQuery

제이쿼리는 웹사이트에 자바스크립트를 쉽게 활용할 수 있도록 도와주는 오픈소스 기반의 자바스크립트 라이브러리이다. 

"write less, do more(적게 작성하고, 많은 것을 하자)"라는 모토로 2006년 미국의 SW 개발자 존 레시(John Resig)이 발표하였다.

- 웹페이지 상에서 엘리먼트(Element)를 쉽게 찾고 조작할 수 있다.

- 네트워크, 애니메이션 등 다양한 기능을 제공한다.

- 메소드 체이닝(Method chaining) 등 짧고 유지 관리가 용이한 코드 작성을 지원한다.

제이쿼리는 마이크로소프트의 ASP.NET 프레임워크, 워드프레스 등 다양한 라이브러리와 프레임워크에 포함되면서 웹 프론트엔드 분야에서 점유율이 지속적으로 상승했다.

웹 기술 조사 서비스인 [W3Techs](https://w3techs.com/)에 따르면 2022년 1월 1일 현재 78.2% 사용률을 차지하고 있다.

![W3Techs](https://github.com/openstack9332/web_roadmap/blob/fe24bbc3034b673fcc1433b21cb1dfdd39f1f958/JavaScript/images/image1.png)

그러나 시간이 지나면서 다양한 라이브러리의 등장으로 제이쿼리을 사용하지 않는 추세이다.

과거 웹 브라우저 간의 호환성이 좋지 않았던 시절 모든 웹 브라우저가 호환되며 짧은 코드로 다양한 기능을 다룰 수 있는 jQuery는 매우 인기 있었다.

특히 DOM을 쉽게 다를 수 있다는 점과 jQuery를 기반으로 한 다양한 라이브러리를 사용할 수 있다는 점이 큰 장점이었다.

그러나 최근 웹 브라우저 환경의 변화와 가상 DOM을 사용하는 라이브러리의 인기로(리액트 등) 더는 jQuery를 사용하지 않게 되었으며, 이제는 '읽을 수 있을 정도만 배우면 되는' 취급을 받고 있다.

<br>

<blockquote>
<p><a href="https://twitter.com/jeresig/status/590206003309891584">Sad this needs to be said but jQuery doesn't 'replace' JS, it papers over the DOM. jQuery's success is proof of the failings of the DOM API.</a><br>
슬프지만 jQuery는 JS를 '대체'하는 것은 아니며, DOM을 감출 뿐이다. jQuery의 성공은 DOM API가 실패했다는 증거이다. </p>
</blockquote>

<br>

더는 jQuery를 사용하지 않는 이유

- 사용할 이유가 딱히 없다. 과거와 달리 현재는 크로스 브라우징 이슈도 적어졌고, virtual DOM의 인기로 DOM을 직접 조작할 필요가 없어졌다. 또한, jQuery로 할 수 있는 대부분 기능은 바닐라 JS나 TypeScript 등으로 똑같이 구현할 수 있다.

- 무겁다. jQuery는 기존 코드를 래핑(wrapping)해서 새롭게 만든 패키지이다. 문제는 이러한 래핑이 지나치게 많고, 애초에 최적화를 위해 설계되지도 않았다는 점이다.

[Moon - Why I decided to Break up With jQuery](https://velog.io/@sy3783/jQuery1.-%EB%8D%94-%EC%9D%B4%EC%83%81-%EC%A0%9C%EC%9D%B4%EC%BF%BC%EB%A6%AC%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EC%A7%80-%EC%95%8A%EB%8A%94-%EC%9D%B4%EC%9C%A0)

- 좋은 대안이 많이 생겼다. 리액트만 해도 재사용성을 높이는 컴포넌트를 기반으로 jQuery보다 훨씬 가독성이 높은 코드를 작성할 수 있다. 또한 더는 DOM을 직접 조작하지 않고 virtual DOM을 이용하는 프레임워크가 널리 사용되고 있다. 이러한 패러다임의 변화는 jQuery의 입지를 더욱 좁게 만들고 있다.

[참고 자료]

[1](https://velog.io/@sy3783/jQuery1.-%EB%8D%94-%EC%9D%B4%EC%83%81-%EC%A0%9C%EC%9D%B4%EC%BF%BC%EB%A6%AC%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EC%A7%80-%EC%95%8A%EB%8A%94-%EC%9D%B4%EC%9C%A0)

[2](https://www.tokyobranch.net/archives/6598)
