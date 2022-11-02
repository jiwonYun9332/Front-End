## 데이터베이스 사용하기 ( MySql )

app.js

```

// Express 모듈 불러오기
let express = require('express');
let http = require('http');
let path = require('path');

// Express 미들웨어 불러오기
let bodyParser = require('body-parser');
let cookieParser = require('cookie-parser');
let static = require('serve-static');

// 오류 핸들러 사용
let expressErrorHandler = require('express-error-handler');

// Session 미들웨어 불러오기
let expressSession = require('express-session');

// crypto 모듈 불러들이기
let crypto = require('crypto');

let app = express();

app.set('port', process.env.PORT || 3000);

// body-parser를 사용해 application/x-www-form-urlenceded 파싱
app.use(bodyParser.urlencoded({ extended: false }));

// body-parsr를 사용해 application/json 파싱
app.use(bodyParser.json());

// public 폴더를 static으로 오픈
app.use('/public', static(path.join(__dirname, 'public')));

// cookie-parser 설정
app.use(cookieParser());

// 세션 설정
app.use(
  expressSession({
    secret: 'my key',
    resave: true,
    saveUninitialized: true,
  })
);

//===== MySQL 데이터베이스를 사용할 수 있는 mysql 모듈 불러오기 =====//
let mysql = require('mysql');

//===== MySQL 데이터베이스 연결 설정 =====//
let pool = mysql.createPool({
  connectionLimit: 10,
  host: 'localhost',
  user: 'root',
  password: 'ghddlr3839!',
  database: 'test',
  debug: false,
});

// 사용자를 인증하는 함수 : 아이디로 먼저 찾고 비밀번호를 그다음에 비교
let authUser = function (id, password, callback) {
  console.log('authUser 호출됨');

  // 커넥션 풀에서 연결 객체를 가져옵니다.
  pool.getConnection(function (err, conn) {
    if (err) {
      if (conn) {
        conn.release(); // 반드시 해제해야 합니다.
      }
      callback(err, null);
      return;
    }
    console.log('데이터베이스 연결 스레드 아이디 : ' + conn.threadId);

    let columns = ['id', 'name', 'age'];
    let tablename = 'users';

    // SQL문을 실행합니다.
    let exec = conn.query(
      'select ?? from ?? where id = ? and password = ? ',
      [columns, tablename, id, password],
      function (err, rows) {
        conn.release(); // 반드시 해제해야 합니다.
        console.log('실행 대상 SQL : ' + exec.sql);

        if (rows.length > 0) {
          console.log(
            '아이디 [%s], 패스워드 [%s] 가 일치하는 사용자 찾음.',
            id,
            password
          );
          callback(null, rows);
        } else {
          console.log('일치하는 사용자를 찾지 못함.');
          callback(null, null);
        }
      }
    );
  });
};

// 사용자를 추가하는 함수
let addUser = function (id, name, age, password, callback) {
  console.log('addUser 호출됨.');

  // 커넥션 풀에서 연결 객체를 가져옵니다.
  pool.getConnection(function (err, conn) {
    if (err) {
      if (conn) {
        conn.release(); // 반드시 해제해야 합니다.
      }

      callback(err, null);
      return;
    }
    console.log('데이터베이스 연결 스레드 아이디 : ' + conn.threadId);

    // 데이터를 객체로 만듭니다.
    let data = { id: id, name: name, age: age, password: password };

    // SQL문을 실행합니다.
    let exec = conn.query(
      'insert into users set ?',
      data,
      function (err, result) {
        conn.release(); // 반드시 해제해야 합니다.
        console.log('실행 대상 SQL : ' + exec.sql);

        if (err) {
          console.log('SQL 실행 시 오류 발생함.');
          console.log(err);

          callback(err, null);

          return;
        }

        callback(null, result);
      }
    );
  });
};

// 라우팅 객체 참조
let router = express.Router();

// 로그인 라우팅 함수 - 데이터베이스의 정보와 비교
router.route('/process/login').post(function (req, res) {
  console.log('/process/login 호출됨.');
});

app.post('/process/login', function (req, res) {
  console.log('/process/login 호출됨.');

  // 요청 파라미터 확인
  let paramId = req.body.id || req.query.id;
  let paramPassword = req.body.password || req.query.password;

  console.log('요청 파라미터 : ' + paramId + ', ' + paramPassword);

  // pool 객체가 초기화된 경우, authUser 함수 호출하여 사용자 인증
  if (pool) {
    authUser(paramId, paramPassword, function (err, rows) {
      // 오류가 발생했을 때 클라이언트로 오류 전송
      if (err) {
        console.log('사용자 로그인 중 오류 발생 : ' + err.stack);
        res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
        res.write('<h2>사용자 로그인 중 오류 발생</h2>');
        res.write('<p>' + err.stack + '</p>');
        res.end();
        return;
      }

      if (rows) {
        console.dir(rows);

        let username = rows[0].name;

        res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
        res.write('<h1>로그인 성공</h1>');
        res.write('<div><p>사용자 아이디 : ' + paramId + '</p></div>');
        res.write('<div><p>사용자 이름 : ' + username + '</p></div>');
        res.write("<br><br><a href='/public/login.html'>다시 로그인하기</a>");
        res.end();
      }
    });
  } else {
    res.wrtieHead('200', { 'Content-Type': 'text/html;charset=utf8' });
    res.write('<h2>데이터베이스 연결 실패</h2>');
    res.write('<div><p>데이터베이스에 연결하지 못했습니다.</p></div>');
    res.end();
  }
});

// 사용자 추가 라우팅 함수 - 클라이언트에서 보내온 데이터를 이용해 데이터베이스에 추가
router.route('/process/adduser').post(function (req, res) {
  console.log('/process/adduser 호출됨.');

  let paramId = req.body.id || req.query.id;
  let paramPassword = req.body.password || req.query.password;
  let paramName = req.body.name || req.query.name;
  let paramAge = req.body.age || req.query.age;

  console.log(
    '요청 파라미터 : ',
    paramId + ', ' + paramPassword + ' ' + paramName + ', ' + paramAge
  );

  // 결과 객체 있으면 성공 응답 전송
  if (pool) {
    addUser(
      paramId,
      paramName,
      paramAge,
      paramPassword,
      function (err, addedUser) {
        // 동일한 id로 추가할 때 오류 발생 - 클라이언트 오류 전송
        if (err) {
          console.error('사용자 추가 중 오류 발생 : ' + err.stack);

          res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
          res.write('<h2>사용자 추가 중 오류 발생</h2');
          res.write('<p>' + err.stack + '</p>');
          res.end();

          return;
        }

        // 결과 객체 있으면 성공 응답 전송
        if (addedUser) {
          console.dir(addedUser);

          console.log('inserted ' + addedUser.affectedRows + ' rows');

          let insertId = addedUser.insertId;
          console.log('추가한 레코드의 아이디 : ' + insertId);

          res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
          res.write('<h2>사용자 추가 성공</h2>');
          res.end();
        } else {
          // 결과 객체가 없으면 실패 응답 전송
          res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
          res.write('<h2>사용자 추가 실패</h2>');
          res.end();
        }
      }
    );
  } else {
    // 데이터베이스 객체가 초기화되지 않은 경우 실패 응답 전송
    res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
    res.write('<h2>데이터베이스 연결 실패</h2>');
    res.end();
  }
});

// 사용자 리스트 함수
router.route('/process/listuser').post(function (req, res) {
  console.log('/process/listuser 호출됨.');

  // 데이터베이스 객체가 초기화된 경우, 모델 객체의 findAll 메소드 호출
  if (database) {
    // 1. 모든 사용자 검색
    UserModel.findAll(function (err, results) {
      // 오류가 발생했을 때 클라이언트로 오류 전송
      if (err) {
        console.error('사용자 리스트 조회 중 오류 발생 : ' + err.stack);

        res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
        res.write('<h2>사용자 리스트 조회 중 오류 발생</h2>');
        res.write('<p>' + err.stack + '</p>');
        res.end();

        return;
      }

      if (results) {
        // 결과 객체 있으면 리스트 전송
        console.dir(results);

        res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
        res.write('<h2>사용자 리스트</h2>');
        res.write('<div><ul>');

        for (let i = 0; i < results.length; i++) {
          let curId = results[i]._doc.id;
          let curName = results[i]._doc.name;
          res.write('   <li>#' + i + ' : ' + curId + ', ' + curName + '</li>');
        }

        res.write('</ul></div>');
        res.end();
      } else {
        // 결과 객체가 없으면 실패 응답 전송
        res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
        res.write('<h2>사용자 리스트 조회 실패</h2>');
        res.end();
      }
    });
  } else {
    // 데이터베이스 객체가 초기화되지 않았을 때 실패 응답 전송
    res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
    res.write('<h2>데이터베이스 연결 실패</h2>');
    res.end();
  }
});

// 라우터 객체 등록
app.use('/', router);

//===== 404 오류 페이지 처리 =====//
let errorHandler = expressErrorHandler({
  static: {
    404: './public/404.html',
  },
});

app.use(expressErrorHandler.httpError(404));
app.use(errorHandler);

//===== 서버 시작 =====//
http.createServer(app).listen(app.get('port'), function () {
  console.log('서버가 시작되었습니다. 포트: ' + app.get('port'));
});

```

adduser.html

```

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>사용자 추가</h1>
    <form method="post" action="/process/adduser">
        <table>
            <tr>
                <td><label>아이디</label></td>
                <td><input type="text" name="id"></td>
            </tr>
            <tr>
                <td><label>비밀번호</label></td>
                <td><input type="password" name="password"></td>
            </tr>
            <tr>
                <td><label>나이</label></td>
                <td><input type="text" name="age"></td>
            </tr>
            <tr>
                <td><label>사용자명</label></td>
                <td><input type="text" name="name"></td>
            </tr>
        </table>
        <input type="submit" value="전송" name="">
    </form>
</body>
</html>

```

