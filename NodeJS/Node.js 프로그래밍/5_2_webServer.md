## 미들웨어 사용하기

> static 미들웨어

특정 폴더의 파일들을 특정 패스로 접근할 수 있도록 만들어 준다. 예를 들어 [public] 폴더에 있는 모든 파일을 웹 서버의 루트 패스로 접근할 수 있도록 설정할 수 있다.

해당 코드는 [public] 폴더 안에 있는 파일들을 클라이언트에서 바로 접근할 수 있게 한다.

```

let static = require('serve-static');

app.use('/public', static(path.join(__dirname, 'public')));

```

static 미들웨어는 외장 모듈로 만들어져 있어 설치가 필요하다. 

```

npm install serve-static --save

```

/public/images 폴더에 들어 있는 house.png 이미지를 웹 브라우저에서 보려면 app.js 파일 안에서 다음과 같이 응답을 보내면 된다.

```

res.end("<img src='/images/house.png' width='50%'>");

```

use() 메소드의 첫 번째 파라미터로 요청 패스를 지정했으며, 두 번째 파라미터 static() 함수로 특정 폴더를 지정했다. 이렇게 하면 요청 패스와 특정 폴더가 매핑(Mapping)된다.

```

app.use('/public', static(path.join(__dirname, 'public')));

```

> body-parser 미들웨어

POST로 요청했을 때 요청 파라미터를 확인할 수 있도록 만들어 둔 미들웨어이다.

body-parser 미들웨어는 클라이언트가 POST 방식으로 요청할 때 본문 영역에 들어 있는 요청 파라미터들을 파싱하여 요청 객체의 body 속성에 넣어 준다.

> login.html

```

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>로그인 테스트</title>
    </head>
<body>
    <h1>로그인</h1>
    <br>
    <form method="post">
        <table>
            <tr>
                <td><label>아이디</label></td>
                <td><input type="text" name="id"></td>
            </tr>
            <tr>
                <td><label>비밀번호</label></td>
                <td><input type="password" name="password"></td>
            </tr>
        </table>
        <input type="submit" value="전송" name="">
    </form>
</body>
</html>

```

> app.js

```

// Express 기본 모듈 불러오기
let express = require('express');
let http = require('http');
let path = require('path');

// Express의 미들웨어 불러오기
let bodyParser = require('body-parser');
let static = require('serve-static');

// 익스프레스 객체 생성
let app = express();

// 기본 속성 설정
app.set('port', process.env.PORT || 3000);

// body-parser를 사용해 application/x-www-form-urlencoded 파싱
app.use(bodyParser.urlencoded({ extended: false }));

// body-parser를 사용해 application/json 파싱
app.use(bodyParser.json());

app.use('/', static(path.join(__dirname, './public')));

// 미들웨어에서 파라미터 확인
app.use(function (req, res, next) {
  console.log('첫 번째 미들웨어에서 요청을 처리함.');

  let paramId = req.body.id || req.query.id;
  let paramPassword = req.body.password || req.query.password;

  res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
  res.write('<h1>Express 서버에서 응답한 결과입니다.</h1>');
  res.write('<div><p>Param id : ' + paramId + '</p></div>');
  res.write('<div><p>Param password ' + paramPassword + '</p></div>');
  res.end();
});

http.createServer(app).listen(3000, function () {
  console.log('Express 서버가 3000번 포트에서 시작됨.');
});

```

> bodyParser.urlencoded()

bodyParser.urlencoded() 메소드를 호출하면서 미들웨어를 설정하면 application/x-www-form-urlencoded 형식으로 전달된 요청 파라미터를 파싱할 수 있다.

> bodyParser.json()

bodyParser.json() 메소드를 호출하면서 미들웨어를 설정하면 application/json 형식으로 전달된 요청 파라미터를 파싱할 수 있다.


## 요청 라우팅 하기

요청 url을 일일이 확인해야 하는 번거로운 문제를 해결하는 것이 라우터 미들웨어(router middleware)이다.

**사용 예시**

```

//라우터 객체 참조
let router = express.Router();

//라우터 함수 등록
router.route('/process/login').get(...);
router.route('/process/login').post(...);

//라우터 객체를 app 객체에 등록
app.use('/', router);

```

**실제 사용 예시**

```

//라우터 객체 참조
let router = express.Router();

//라우팅 함수 등록
router.route('/process/login').post(function (req, res) {
  console.log('/process/login 처리함');

  let paramId = req.body.id || req.query.id;
  let paramPassword = req.body.password || req.query.password;

  res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
  res.write('<h1>Express 서버에서 응답한 결과입니다.</h1>');
  res.write('<div><p>Param id : ' + paramId + '</p></div>');
  res.write('<div><p>Param password : ' + paramPassword + '</p></div>');
  res.write("<br><br><a href='/login2.html'>로그인 페이지로 돌아가기</a>");
  res.end();
});

// 라우터 객체를 app 객체에 등록
app.use('/', router);

```

**URL 파라미터 사용하기**

클라이언트에서 요청할 때 URL 뒤에 ? 기호를 붙이면 요청 파라미터(query string)를 추가하여 보낼 수 있다. 클라이언트에서 서버로 데이터를 전달하는 방식은 이것 이외에도 
URL 파라미터를 사용하기도 한다. URL 파라미터는 요청 파라미터와 달리 URL 주소의 일부로 들어간다.

login3.html

```

<form method="post" action="/process/login/mike">

```

app.js

```

//라우팅 함수 등록
router.route('/process/login/:name').post(function (req, res) {
  console.log('/process/login/:name 처리함');

  let paramName = req.params.name;

  let paramId = req.body.id || req.query.id;
  let paramPassword = req.body.password || req.query.password;

  res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
  res.write('<h1>Express 서버에서 응답한 결과입니다.</h1>');
  res.write('<div><p>Param name : ' + paramName + '</p></div>');
  res.write('<div><p>Param id : ' + paramId + '</p></div>');
  res.write('<div><p>Param password : ' + paramPassword + '</p></div>');
  res.write("<br><br><a href='/login3.html'>로그인 페이지로 돌아가기</a>");
  res.end();
});

```

app.post 메소드를 호출할 때 전달하는 파라미터 값이 /process/login/:name 이다. 이것은 /process/login/ 뒤에 오는 값을 파라미터로 처리하겠다는 의미이다.

이렇게 지정한 파라미터는 req.params 객체 안에 들어간다. 따라서 :name으로 표시된 부분에 넣어 전달된 값은 req.params.name 속성으로 접근할 수 있다.

이것을 **(Token)** 라고도 부른다.

**오류 페이지 보여 주기**

```

// 등록되지 않은 패스에 대해 페이지 오류 응답
app.all('*', function(req, res) {
  res.status(404).send('<h1>ERROR - 페이지를 찾을 수 없습니다.</h1>');
});

```

**express-error-handler 미들웨어로 오류 페이지 보내기**

예상하지 못한 오류가 발생했을 때 그 오류를 처리할 수 있는 미들웨어를 사용할 수 있다. 

express-error-handler 미들웨어를 사용해 404.html 페이지를 응답 보냘 수 있다.

```

// 오류 핸들러 모듈 사용
let expressErrorHandler = require('express-error-handler');

// 모든 router 처리 끝난 후 404 오류 페이지 처리
let errorHandler = expressErrorHandler({
  static: {
    '404': './public/404.html'
  }
});

app.use(expressErrorHandler.httpError(404) );
app.use(errorHandler);

```

express-error-handler 모듈은 특정 오류 코드에 따라 클라이언트로 응답을 보내 줄 때 미리 만들어 놓은 웹 문서를 보내 줄 수 있다.

오류 페이지는 모든 라우터 처리가 끝난 후 처리되어야 한다.

```

// 오류 핸들러 모듈 사용
let expressErrorHandler = require('express-error-handler');

// 모든 router 처리 끝난 후 404 오류 페이지 처리
let errorHandler = expressErrorHandler({
  static: {
    404: './public/404.html',
  },
});

app.use(expressErrorHandler.httpError(404));
app.use(errorHandler);

```

**쿠키와 세션 관리하기**

쿠키는 클라이언트 웹 브라우저에 저장되는 정보이며 세션은 웹 서버에 저장되는 정보이다.

> 쿠키 처리하기

쿠키는 클라이언트 웹 브라우저에 저장되는 정보로서 일정 기간 동안 저장하고 싶을 때 사용한다. 익스프레스에서는 cookie-parser 미들웨어를 사용하면 쿠키를 설정하거나 확인할 수 있다.

use() 메소드를 사용해 cookie-parser 미들웨어를 사용하도록 만들면 요청 객체에 cookies 속성이 추가된다.

```

// 쿠키 사용
let cookieParser = require('cookie-parser');

// 쿠키 미들웨어 등록
app.use(cookieParser());

router.route('/process/showCookie').get(function (req, res) {
  console.log('/process/showCookie 호출됨.');

  res.send(req.cookies);
});

router.route('/process/setUserCookie').get(function (req, res) {
  console.log('/process/setUserCookie 호출됨.');

  // 쿠키 설정
  res.cookie('user', {
    id: 'mike',
    name: '소녀시대',
    authorized: true,
  });

  // redirect로 응답
  res.redirect('/process/showCookie');
});

```

> 세션 처리하기

express-session 모듈 설치

```

npm install express-session --save

```

```

// 쿠키 사용
let cookieParser = require('cookie-parser');
// 세션 사용
let expressSession = require('express-session');

// 세션 미들웨어 등록
app.use(
  expressSession({
    secret: 'my key',
    resave: true,
    saveUninitialized: true,
  })
);

// 상품정보 라우팅 함수
router.route('/process/product').get(function (req, res) {
  console.log('/process/product 호출됨.');

  if (req.session.user) {
    res.redirect('/product.html');
  } else {
    res.redirect('/login2.html');
  }
});

// 로그인 라우팅 함수 - 로그인 후 세션 저장함
router.route('/process/login').post(function (req, res) {
  console.log('/process/login 호출됨.');

  let paramId = req.body.id || req.query.id;
  let paramPassword = req.body.password || req.query.password;

  if (req.session.user) {
    // 이미 로그인된 상태
    console.log('이미 로그인되어 상품 페이지로 이동합니다.');

    res.redirect('/public/product.html');
  } else {
    // 세션저장
    req.session.user = {
      id: paramId,
      name: '소녀시대',
      authorized: true,
    };

    res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
    res.write('<h1>로그인 성공</h1>');
    res.write('<div><p>Param id : ' + paramId + '</p></div>');
    res.write('<div><p>Param password : ' + paramPassword + '</p></div>');
    res.write("<br><br><a href='/process/product'>상품 페이지로 이동하기</a>");
    res.end();
  }
});

// 로그아웃 라우팅 함수 - 로그아웃 후 세션 삭제함
router.route('/process/logout').get(function (req, res) {
  console.log('/process/logout 호출됨.');

  if (req.session.user) {
    // 로그인된 상태
    console.log('로그아웃합니다.');

    req.session.destroy(function (err) {
      if (err) {
        throw err;
      }

      console.log('세션을 삭제하거 로그아웃되었습니다.');
      res.redirect('/login2.html');
    });
  } else {
    // 로그인 안된 상태
    console.log('아직 로그인되어 있지 않습니다.');
    res.redirect('/public/login2.html');
  }
});

```

> product.html

```

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>상품 페이지</title>
    </head>
    <body>
        <h3>상품정보 페이지</h3>
        <hr/>
        <p>로그인 후 볼 수 있는 상품정보 페이지입니다.</p>
        <br><br>
        <a href="/process/logout">로그아웃</a>
    </body>
</html>

```

































