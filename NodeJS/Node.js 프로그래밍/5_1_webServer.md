### 간단한 웹 서버 만들기

노드에 기본으로 들어 있는 http 모듈을 사용하면 웹 서버 기능을 담당하는 서버 객체를 만들 수 있다. http 모듈을 로딩했을 때 반환되는 객체에는 createServer() 메소드가
정의되어 있다. 따라서 이 메소드를 호출하면 서버 객체를 만들 수 있다. 

```

let http = require('http');

// 웹 서버 객체를 만든다.
let server = http.createServer();

// 웹 서버를 시작하여 3000번 포트에서 대기한다.
let port = 3000;
server.listen(port, function() {
  console.log('웹 서버가 시작되었습니다 : %d', port);
});

```

> 서버 객체에서 사용할 수 있는 대표적인 메소드

- listen(port, [hostname], [backlog], [callback]) : 서버를 실행하여 대기시킵니다.
- close([callback]) : 서버를 종료합니다.

> 서버 객체에서 사용할 수 있는 중요 이벤트

- connection : 클라이언트가 접속하여 연결이 만들어질 때 발생하는 이벤트이다.
- request : 클라이언트가 요청할 때 발생하는 이벤트이다.
- close : 서버를 종료할 때 발생하는 이벤트이다.

```

let http = require('http');

// 웹 서버 객체를 만듭니다.
let server = http.createServer();

// 웹 서버를 시작하여 3000번 포트에서 대기하도록 설정합니다.
let port = 3000;
server.listen(port, function () {
  console.log('웹 서버가 시작되었습니다. : %d', port);
});

// 클라이언트 연결 이벤트 처리
server.on('connection', function (socket) {
  let addr = socket.address();
  console.log('클라이언트가 접속했습니다 %s, %d', addr.address, addr.port);
});

// 클라이언트 요청 이벤트 처리
server.on('request', function (req, res) {
  console.log('클라이언트 요청이 들어왔습니다.');

  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.write('<!DOCTYPE html>');
  res.write('<html>');
  res.write(' <head>');
  res.write('  <title>응답 페이지</title>');
  res.write(' </head>');
  res.write(' <body>');
  res.write('  <h1>노드제이에스로부터의 응답 페이지</h1>');
  res.write(' </body>');
  res.write('</html');
  res.end();
});

// 서버 종료 이벤트 처리
server.on('close', function () {
  console.log('서버가 종료됩니다.');
});

```

> res 객체를 사용해서 응답을 보낼 때 사용하는 주요 메소드

- writeHead : 응답으로 보낼 헤더를 만든다.
- write : 응답 본문(body) 데이터를 만든다. 여러 번 호출될 수 있다.
- end : 클라이언트로 응답을 전송한다. 파라미터에 데이터가 들어 있다면 이 데이터를 포함시켜 응답을 전송한다. 클라이언트의 요청이 있을 때 한 번은 호출되어야 응답을 보내며, 콜백
        함수가 지정되면 응답이 전송된 후 콜백 함수가 호출된다.

**서버 객체를 만들 때 응답 보내기**

```
// 클라이언트 요청 이벤트 처리
let server = http.createServer(function (req, res) {
  console.log('클라이언트 요청이 들어왔습니다.');

  res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8' });
  res.write('<!DOCTYPE html>');
  res.write('<html>');
  res.write(' <head>');
  res.write('  <title>응답 페이지</title>');
  res.write(' </head>');
  res.write(' <body>');
  res.write('  <h1>노드제이에스로부터의 응답 페이지</h1>');
  res.write(' </body>');
  res.write('</html');
  res.end();
});
```

**클라이언트에서 요청이 있을 때 파일 읽어 응답하기**

```

// 클라이언트 연결 이벤트 처리
server.on('connection', function (socket) {
  let addr = socket.address();
  console.log('클라이언트가 접속했습니다 %s, %d', addr.address, addr.port);
});

server.on('request', function (req, res) {
  let filename = 'ex01.jpg';
  fs.readFile(filename, function (err, data) {
    res.writeHead(200, { 'Content-Type': 'image/jpeg' });
    res.write(data);
    res.end();
  });
});

```

**파일을 스트림으로 읽어 응답 보내기**

```
server.on('request', function (req, res) {
  console.log('클라이언트 요청이 들어왔습니다.');

  let filename = 'ex01.jpg';
  let infile = fs.createReadStream(filename, { flags: 'r' });

  // 파이프로 연결하여 알아서 처리하도록 설정하기
  infile.pipe(res);
});
```

똑같은 기능을 더 적은 양의 코드로 만들었으나 헤더를 설정할 수 없는 등의 제약이 생긴다.

**파일을 버퍼에 담아 두고 일부분만 읽어 응답 보내기**

```
server.on('request', function (req, res) {
  console.log('클라이언트 요청이 들어왔습니다.');

  let filename = 'ex01.jpg';
  let infile = fs.createReadStream(filename, { flags: 'r' });
  let filelength = 0;
  let curlength = 0;

  fs.stat(filename, function (err, stats) {
    filelength = stats.size;
  });

  // 헤더 쓰기
  res.writeHead(200, { 'Content-Type': 'image/jpg' });

  // 파일 내용을 스트림에서 읽어 본문 쓰기
  infile.on('readable', function () {
    let chunk;
    while (null !== (chunk = infile.read())) {
      console.log('읽어 들인 데이터 크기 : %d 바이트', chunk.length);
      curlength += chunk.length;
      res.write(chunk, 'utf8', function (err) {
        console.log(
          '파일 부분 쓰기 완료 : %d, 파일 크기 : %d',
          curlength,
          filelength
        );
        if (curlength >= filelength) {
          // 응답 전송하기
          res.end();
        }
      });
    }
  });
});
```

**서버에서 다른 웹 사이트의 데이터를 가져와 응답하기 - get 방식**

```
let options = {
  host: 'www.google.com',
  port: 80,
  path: '/',
};

let req = http.get(options, function (res) {
  // 응답 처리
  let resData = '';
  res.on('data', function (chunk) {
    resData += chunk;
  });

  res.on('end', function () {
    console.log(resData);
  });
});

req.on('error', function (err) {
  console.log('오류 발생 : ' + err.message);
});

```

**서버에서 다른 웹 사이트의 데이터를 가져와 응답하기 - post 방식**

```
let opts = {
  host: 'www.google.com',
  port: 80,
  method: 'POST',
  path: '/',
  headers: {},
};

let resData = '';
let req = http.request(opts, function (res) {
  // 응답 처리
  res.on('data', function (chunk) {
    resData += chunk;
  });

  res.on('end', function () {
    console.log(resData);
  });
});

opts.headers['Content-Type'] = 'application/x-www-form-urlencoded';
req.data = 'q=actor';
opts.headers['Content-Length'] = req.data.length;

req.on('error', function (err) {
  console.log('오류 발생 : ' + err.message);
});

// 요청 전송
req.write(req.data);
req.end();
```

**익스프레스로 웹 서버 만들기**

```

// Express 기본 모듈 불러오기
let express = require('express');
let http = require('http');

// 익스프레스 객체 생성
let app = express();

// 기본 포트를 app 객체에 속성으로 설정
app.set('port', process.env.PORT || 3000);

// Express 서버 시작
http.createServer(app).listen(app.get('port'), function () {
  console.log('익스프레스 서버를 시작했습니다 : ' + app.get('port'));
});

```

http 모듈로 웹 서버를 만들 때와 달리 createServer() 메소드에 전달되는 파라미터로 app 객체를 전달한다.

해당 app 객체는 **express() 메소드 호출로 만들어지는 익스프레스 서버 객체**이다.

> 익스프레스 서버 객체 메소드
- set(name, value) : 서버 설정을 위한 속성을 지정한다. set() 메소드로 지정한 속성은 get() 메소드로 꺼내어 확인할 수 있다.
- get(name) : 서버 설정을 위해 지정한 속성을 꺼내 온다.
- use([path], function[, function...]) : 미들웨어 함수를 사용한다.
- get([path], function) : 특정 패스로 요청된 정보를 처리한다.

> 서버 설정을 위해 미리 정해진 app 객체의 주요 속성
- env : 서버 모드를 설정한다.
- views : 뷰들이 들어 있는 폴더 또는 폴더 배열을 설정한다.
- view engine : 디폴트로 사용할 뷰 엔진을 설정한다.


**미들웨어로 클라이언트에 응답 보내기**

```

let express = require('express');
let http = require('http');

let app = express();

app.use(function (req, res, next) {
  console.log('첫 번째 미들웨어에서 요청을 처리함.');

  res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
  res.end('<h1>Express 서버에서 응답한 결과입니다.</h1>');
});

http.createServer(app).listen(3000, function () {
  console.log('Express 서버가 3000번 포트에서 시작됨.');
});

```

**여러 개의 미들웨어를 등록하여 사용하는 방법 알아보기**

```

let express = require('express');
let http = require('http');

let app = express();

app.use(function (req, res, next) {
  console.log('첫 번째 미들웨어에서 요청을 처리함.');

  req.user = 'mike';

  next();
});

app.use(function (req, res, next) {
  console.log('두 번째 미들웨어에서 요청을 처리함.');

  res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
  res.end('<h1>Express 서버에서 ' + req.user + '가 응답한 결과입니다.</h1>');
});

http.createServer(app).listen(3000, function () {
  console.log('Express 서버가 3000번 포트에서 시작됨.');
});

```

**익스프레스의 요청 객체와 응답 객체 알아보기**

- send([body]) : 클라이언트에 응답 데이터를 보낸다. 전달할 수 있는 데이터는 HTML 문자열, Buffer 객체, JSON 객체, JSON 배열이다.
- status(code) : HTTP 상태 코드를 반환한다. 상태 코드는 end()나 send() 같은 전송 메소드를 추가로 호출해야 전송할 수 있다.
- sendStatus(statusCode) : HTTP 상태 코드를 반환한다. 상태 코드는 상태 메시지와 함께 전송된다.
- redirect([status,] path) : 웹 페이지 경로를 강제로 이동시킨다.
- render(view [, locals][, callback]) : 뷰 엔진을 사용해 문서를 만든 후 전송한다.













