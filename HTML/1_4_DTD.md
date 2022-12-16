# 문서 형식 선언

- DTD(Document Type Declaration) 또는 DOCTYPE이라고 한다.

- 어떤 SGML이나 XML(SGML에서 파생된 언어) 기반 문서 내에 그 문서가 특정 문서 형식 정의(DTD)를 따름을 지정하는 것이다.

- 본래 DTD에 기반한 SGML 도구를 이용해 문서 해석 가능성과 유효성을 검사하기 위한 목적으로 문서 내에 삽입되었다.

HTML 문서의 규격 판 번호를 명시하는 데서 흔히 볼 수 있다. 웹 브라우저는 문서 형식 선언이 없는 HTML 문서를 **쿼크 모드**로 렌더링하지만
문서 형식 선언이 있는 HTML 문서를 표준 모드로 렌더링하기 때문에, 문서 형식 선언을 이용해서 어떤 웹 페이지가 모든 웹 브라우저에서 같은
레이아웃으로 제공되도록 할 수 있다.

또한 HTML5은 구조적으로 SGML가 호환될 수 없다. 따라서 HTML5로 구성된 문서에서 문서 형식 선언은 불필요하지만, 웹 브라우저들의 표준 모드를
활성화하기 위해 최소한의 형태로 유지되었다.

**쿼크 모드**

오래된 웹 브라우저를 위하여 디자인된 웹 페이지의 하위 호환성을 유지하기 위해 W3C나 IETF의 표준을 엄격히 준수하는 표준 모드(Standards Mode)를 대신하여
쓰이는 웹 브라우저 기술을 가리킨다. 같은 코드라도 웹 브라우저마다 서로 다르게 해석하므로 전혀 다른 결과물을 보여주게 된다.
