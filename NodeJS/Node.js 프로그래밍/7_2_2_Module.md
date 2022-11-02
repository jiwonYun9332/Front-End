## 스키마 파일을 별도의 모듈 파일로 분리하기

> 사용자 처리 함수를 별도의 모듈 파일로 분리해 보기

현재 스키마 파일을 별도 파일을 분리하였다. 

이제 사용자 처리 관련 함수을 별도의 모듈 파일로 분리한다. 

시용자 관련 함수들은 익스프레스의 라우팅 미들웨어를 사용하지만 모듈로 분리하는 방법은 일반적인 모듈로 만들어 사용할 때와 같다.

**라우팅 미들웨어**

- router.route('/process/login').post(function(...) {...});
- router.route('/process/adduser').post(function(...) {...});
- router.router('/process/listuser').post(function(...) {...});

app.post() 함수의 두 번째 파라미터로 전달되는 것이 함수이므로 이 함수를 별도의 모듈로 분리할 수 있다.


**/routes/user.js**

```

let login = function(req, res) {
    console.log('user 모듈 안에 있는 login 호출됨.');

...

let adduser = function(req, res) {
    console.log('user 모듈 안에 있는 adduser 호출됨.');

...

let listuser = function(req, res) {
    consoel.log('user 모듈 안에 있는 listuser 호출됨.');

...

module.exports.login = login;
module.exports.adduser = adduser;
module.exports.listuser = listuser;

```

app.js에 있던 라우팅 미들웨어를 **/router/user.js** 옮겨주었다. 그러나 실제로 실행할 시 오류가 발생한다.

그 이유는 해당 모듈 파일 안에서 데이터베이스 객체나 스키마 객체를 참조할 수 없기 때문이다.

**이와 같이 모듈 파일 안에서 해당 모듈을 불러들여 사용하는 곳의 변수를 참조해야 할 때가 많다.**

따라서 데이터베이스 관련 객체(데이터베이스 객체, 스키마 객체, 모델 객체)를 별도의 다른 모듈에서 만들거나 app.js 같은 메인 파일에서 만들 때

모듈 파일 쪽으로 이 객체들을 전달할 수 있어야 한다.

익스프레스는 요청 객체가 app 객체를 속성으로 가지고 있기 때문에 메인 파일에서 모듈 파일로 객체를 전달할 때 app 객체에 속성으로 추가한 후 전달할 수 있다.
이때는 app 객체의 set()과 get() 메소드를 사용하는 것이 좋다.

**app.js**

```

// user 스키마 및 모델 객체 생성
function createUserSchema() {
  // user_schema.js 모듈 불러오기
  UserSchema = require('./database/user_schema').createSchema(mongoose);

  // UserModel 모델 정의
  UserModel = mongoose.model('users3', UserSchema);
  console.log('UserModel 정의함.');

  // UserSchema와 UserModel 객체를 app에 추가
  app.set('UserSchema', UserSchema);
  app.set('UserModel', UserModel);

  // init 호출
  user.init(database, UserSchema, UserModel);
}

......

//===== 라우팅 함수 등록 =====//

// 라우터 객체 참조
let router = express.Router();

// 4.로그인 처리 함수를 라우팅 모듈을 호출하는 것으로 수정
router.route('/process/login').post(user.login);

// 5. 사용자 추가 함수를 라우팅 모듈을 호출하는 것으로 수정
router.route('/process/adduser').post(user.adduser);

// 6. 사용자 리스트 함수를 라우팅 모듈을 호출하는 것으로 수정
router.route('/process/listuser').post(user.listuser);

```

**user.js**

```

let database;
let UserSchema;
let UserModel;

// 데이터베이스 객체, 스키마 객체, 모델 객체를 이 모듈에서 사용할 수 있도록 전달함
let init = function (db, schema, model) {
  console.log('init 호출됨.');

  database = db;
  UserSchema = schema;
  UserModel = model;
};

```

**전체 코드(app.js)**

```

/**
 * 데이터베이스 사용하기
 *
 * 비밀번호 암호화와 입력값 유효성 확인
 *
 * 웹브라우저에서 아래 주소의 페이지를 열고 웹페이지에서 요청
 * (먼저 사용자 추가 후 로그인해야 함)
 *    http://localhost:3000/public/login.html
 *    http://localhost:3000/public/adduser2.html
 *
 * @date 2016-11-10
 * @author Mike
 */

// Express 기본 모듈 불러오기
let express = require('express'),
  http = require('http'),
  path = require('path');

// Express의 미들웨어 불러오기
let bodyParser = require('body-parser'),
  cookieParser = require('cookie-parser'),
  static = require('serve-static');

// 에러 핸들러 모듈 사용
let expressErrorHandler = require('express-error-handler');

// Session 미들웨어 불러오기
let expressSession = require('express-session');

// mongoose 모듈 사용
let mongoose = require('mongoose');

// 사용자 정의 모듈 - 사용자 정보 처리
let user = require('./routes/user');

// 익스프레스 객체 생성
let app = express();

// 기본 속성 설정
app.set('port', process.env.PORT || 3000);

// body-parser를 이용해 application/x-www-form-urlencoded 파싱
app.use(bodyParser.urlencoded({ extended: false }));

// body-parser를 이용해 application/json 파싱
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

//===== 데이터베이스 연결 =====//

// 데이터베이스 객체를 위한 변수 선언
let database;

// 데이터베이스 모델 객체를 위한 변수 선언
let UserModel;

//데이터베이스에 연결
function connectDB() {
  // 데이터베이스 연결 정보
  let databaseUrl = 'mongodb://localhost:27017/local';

  // 데이터베이스 연결
  console.log('데이터베이스 연결을 시도합니다.');
  mongoose.Promise = global.Promise; // mongoose의 Promise 객체는 global의 Promise 객체 사용하도록 함
  mongoose.connect(databaseUrl);
  database = mongoose.connection;

  database.on(
    'error',
    console.error.bind(console, 'mongoose connection error.')
  );
  database.on('open', function () {
    console.log('데이터베이스에 연결되었습니다. : ' + databaseUrl);

    // user 스키마 및 모델 객체 생성
    createUserSchema();
  });

  // 연결 끊어졌을 때 5초 후 재연결
  database.on('disconnected', function () {
    console.log('연결이 끊어졌습니다. 5초 후 재연결합니다.');
    setInterval(connectDB, 5000);
  });
}

// user 스키마 및 모델 객체 생성
function createUserSchema() {
  // user_schema.js 모듈 불러오기
  UserSchema = require('./database/user_schema').createSchema(mongoose);

  // UserModel 모델 정의
  UserModel = mongoose.model('users3', UserSchema);
  console.log('UserModel 정의함.');

  // UserSchema와 UserModel 객체를 app에 추가
  app.set('UserSchema', UserSchema);
  app.set('UserModel', UserModel);

  // init 호출
  user.init(database, UserSchema, UserModel);
}

//===== 라우팅 함수 등록 =====//

// 라우터 객체 참조
let router = express.Router();

// 4.로그인 처리 함수를 라우팅 모듈을 호출하는 것으로 수정
router.route('/process/login').post(user.login);

// 5. 사용자 추가 함수를 라우팅 모듈을 호출하는 것으로 수정
router.route('/process/adduser').post(user.adduser);

// 6. 사용자 리스트 함수를 라우팅 모듈을 호출하는 것으로 수정
router.route('/process/listuser').post(user.listuser);

// 라우터 객체 등록
app.use('/', router);

// 404 에러 페이지 처리
let errorHandler = expressErrorHandler({
  static: {
    404: './public/404.html',
  },
});

app.use(expressErrorHandler.httpError(404));
app.use(errorHandler);

//===== 서버 시작 =====//

// 프로세스 종료 시에 데이터베이스 연결 해제
process.on('SIGTERM', function () {
  console.log('프로세스가 종료됩니다.');
  app.close();
});

app.on('close', function () {
  console.log('Express 서버 객체가 종료됩니다.');
  if (database) {
    database.close();
  }
});

// Express 서버 시작
http.createServer(app).listen(app.get('port'), function () {
  console.log('서버가 시작되었습니다. 포트 : ' + app.get('port'));

  // 데이터베이스 연결을 위한 함수 호출
  connectDB();
});

```

**전체코드(user.js)**

```

/**
 * @date 2022-03-18
 * @author Jiwon
 */

let database;
let UserSchema;
let UserModel;

// 데이터베이스 객체, 스키마 객체, 모델 객체를 이 모듈에서 사용할 수 있도록 전달함
let init = function (db, schema, model) {
  console.log('init 호출됨.');

  database = db;
  UserSchema = schema;
  UserModel = model;
};

let login = function (req, res) {
  console.log('user 모듈 안에 있는 login 호출됨.');

  // 데이터베이스 객체가 필요한 경우 req.app.get('database')로도 참조 가능

  // 요청 파라미터 확인
  let paramId = req.body.id || req.query.id;
  let paramPassword = req.body.password || req.query.password;

  console.log('요청 파라미터 : ' + paramId + ', ' + paramPassword);

  // 데이터베이스 객체가 초기화된 경우, authUser 함수 호출하여 사용자 인증
  if (database) {
    authUser(database, paramId, paramPassword, function (err, docs) {
      // 에러 발생 시, 클라이언트로 에러 전송
      if (err) {
        console.error('로그인 중 에러 발생 : ' + err.stack);

        res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
        res.write('<h2>로그인 중 에러 발생</h2>');
        res.write('<p>' + err.stack + '</p>');
        res.end();

        return;
      }

      // 조회된 레코드가 있으면 성공 응답 전송
      if (docs) {
        console.dir(docs);

        // 조회 결과에서 사용자 이름 확인
        let username = docs[0].name;

        res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
        res.write('<h1>로그인 성공</h1>');
        res.write('<div><p>사용자 아이디 : ' + paramId + '</p></div>');
        res.write('<div><p>사용자 이름 : ' + username + '</p></div>');
        res.write("<br><br><a href='/public/login.html'>다시 로그인하기</a>");
        res.end();
      } else {
        // 조회된 레코드가 없는 경우 실패 응답 전송
        res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
        res.write('<h1>로그인  실패</h1>');
        res.write('<div><p>아이디와 패스워드를 다시 확인하십시오.</p></div>');
        res.write("<br><br><a href='/public/login.html'>다시 로그인하기</a>");
        res.end();
      }
    });
  } else {
    // 데이터베이스 객체가 초기화되지 않은 경우 실패 응답 전송
    res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
    res.write('<h2>데이터베이스 연결 실패</h2>');
    res.write('<div><p>데이터베이스에 연결하지 못했습니다.</p></div>');
    res.end();
  }
};

let adduser = function (req, res) {
  console.log('user 모듈 안에 있는 adduser 호출됨.');

  // 필요한 경우 req.app.get('database')로도 참조 가능

  let paramId = req.body.id || req.query.id;
  let paramPassword = req.body.password || req.query.password;
  let paramName = req.body.name || req.query.name;

  console.log(
    '요청 파라미터 : ' + paramId + ', ' + paramPassword + ', ' + paramName
  );

  // 데이터베이스 객체가 초기화된 경우, addUser 함수 호출하여 사용자 추가
  if (database) {
    addUser(
      database,
      paramId,
      paramPassword,
      paramName,
      function (err, addedUser) {
        // 동일한 id로 추가하려는 경우 에러 발생 - 클라이언트로 에러 전송
        if (err) {
          console.error('사용자 추가 중 에러 발생 : ' + err.stack);

          res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
          res.write('<h2>사용자 추가 중 에러 발생</h2>');
          res.write('<p>' + err.stack + '</p>');
          res.end();

          return;
        }

        // 결과 객체 있으면 성공 응답 전송
        if (addedUser) {
          console.dir(addedUser);

          res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
          res.write('<h2>사용자 추가 성공</h2>');
          res.end();
        } else {
          // 결과 객체가 없으면 실패 응답 전송
          res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
          res.write('<h2>사용자 추가  실패</h2>');
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
};

let listuser = function (req, res) {
  console.log('user 모듈 안에 있는 listuser 호출됨.');

  // 필요한 경우 req.app.get('database')로도 참조 가능

  // 데이터베이스 객체가 초기화된 경우, 모델 객체의 findAll 메소드 호출
  if (database) {
    // 1. 모든 사용자 검색
    UserModel.findAll(function (err, results) {
      // 에러 발생 시, 클라이언트로 에러 전송
      if (err) {
        console.error('사용자 리스트 조회 중 에러 발생 : ' + err.stack);

        res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
        res.write('<h2>사용자 리스트 조회 중 에러 발생</h2>');
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
          res.write('    <li>#' + i + ' : ' + curId + ', ' + curName + '</li>');
        }

        res.write('</ul></div>');
        res.end();
      } else {
        // 결과 객체가 없으면 실패 응답 전송
        res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
        res.write('<h2>사용자 리스트 조회  실패</h2>');
        res.end();
      }
    });
  } else {
    // 데이터베이스 객체가 초기화되지 않은 경우 실패 응답 전송
    res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
    res.write('<h2>데이터베이스 연결 실패</h2>');
    res.end();
  }
};

// 사용자를 인증하는 함수 : 아이디로 먼저 찾고 비밀번호를 그 다음에 비교하도록 함
var authUser = function (database, id, password, callback) {
  console.log('authUser 호출됨 : ' + id + ', ' + password);

  // 1. 아이디를 이용해 검색
  UserModel.findById(id, function (err, results) {
    if (err) {
      callback(err, null);
      return;
    }

    console.log('아이디 [%s]로 사용자 검색결과', id);
    console.dir(results);

    if (results.length > 0) {
      console.log('아이디와 일치하는 사용자 찾음.');

      // 2. 패스워드 확인 : 모델 인스턴스를 객체를 만들고 authenticate() 메소드 호출
      var user = new UserModel({ id: id });
      var authenticated = user.authenticate(
        password,
        results[0]._doc.salt,
        results[0]._doc.hashed_password
      );
      if (authenticated) {
        console.log('비밀번호 일치함');
        callback(null, results);
      } else {
        console.log('비밀번호 일치하지 않음');
        callback(null, null);
      }
    } else {
      console.log('아이디와 일치하는 사용자를 찾지 못함.');
      callback(null, null);
    }
  });
};

//사용자를 추가하는 함수
var addUser = function (database, id, password, name, callback) {
  console.log('addUser 호출됨 : ' + id + ', ' + password + ', ' + name);

  // UserModel 인스턴스 생성
  var user = new UserModel({ id: id, password: password, name: name });

  // save()로 저장 : 저장 성공 시 addedUser 객체가 파라미터로 전달됨
  user.save(function (err, addedUser) {
    if (err) {
      callback(err, null);
      return;
    }

    console.log('사용자 데이터 추가함.');
    callback(null, addedUser);
  });
};

// module.exports 객체에 속성으로 추가

module.exports.init = init;
module.exports.login = login;
module.exports.adduser = adduser;
module.exports.listuser = listuser;

```

## 설정 파일 만들기

웹 서버 안의 각 기능을 별도의 파일로 분리하여 모듈로 만들면 기능 수정이 필요할 때 웹 서버의 메인 파일을 수정하지 않고 모듈 부분만 수정해도 됩니다.

또 새로운 모듈을 추가할 때도 메인 파일을 수정하지 않아도 되기 때문에 서버의 유지관리에 아주 좋은 구성이 된다.

이때 새로운 모듈을 추가했을 때 메인 파일을 수정하지 않고 어떤 모듈이 추가되었는지 어떻게 알 수 있을까?

**설정 파일을 만들고 메인 파일이 설정 파일을 불러오도록 하면 된다.** 왜냐하면 새로운 모듈을 추가했을 때 파일 설정 파일만 수정해도 메인 파일에서 변경된 내용을 알 수
있기 때문이다. 

즉, 새로운 설정 파일의 이름이 config.js라면 이 파일을 모듈 파일로 만들고 이 파일 안에 설정 정보를 넣어 둔 후 서버가 실행될 때 메인 파일에서 이 설정 파일에 있는 정보를
읽어 들이도록 만들면 된다.

config.js 파일 안에 들어 있는 설정 정보에는 서버를 실행하는 데 필요한 정보와 데이터베이스 정보 등을 담아 둔다.

서버 정보는, 서버를 실행할 때 필요한 포트 등의 정보를 말하는 것으로 환경 변수로 설정하여 읽어 들일 수 있으며, config.js 파일에 넣어 둘 수도 있다.

데이터베이스 정보는 데이터베이스 연결에 필요한 URL이나 인증 정보를 말한다.

mongoose를 사용하는 데이터베이스는 스키마를 생성한 후에 데이터베이스에 접근하므로 스키마 생성 부분을 별도 파일로 분리해 두고 
스키마 파일의 로딩 정보를 config.js 파일에 넣어 둘 수 있다.

**config.js**

```

module.exports = {
  server_port: 3000,
  db_url: 'mongodb://localhost:27017/local',
  db_schema: [
    {
      file: './user_schema',
      collection: 'user3',
      schemaName: 'UserSchema',
      modelName: 'UserModel',
    },
  ],
};

```

**app.js**

```

let config = require('./config');

......

//===== 서버 변수 설정 및 static으로 [public] 폴더 설정 =====//
console.log('config.server_port : %d', config.server_port);
app.set('port', process.env.PORT || config.server_port);

......

//데이터베이스에 연결
function connectDB() {
  // 데이터베이스 연결 정보
  let databaseUrl = config.db_url;

```

**database.js**

```

let mongoose = require('mongoose');

// database 객체에 db, schema, model 모두 추가
let database = {};

database.init = function (app, config) {
  console.log('init() 호출됨');

  connect(app, config);
};

// config에 정의한 스키마 및 모델 객체 생성
function createSchema(app, config) {
  let schemaLen = config.db_schemas.length;
  console.log('설정에 정의된 스키마의 수 : %d', schemaLen);

  for (let i = 0; i < schemaLen; i++) {
    let curItem = config.db_schema[i];

    // 모듈 파일에서 모듈 불러온 후 createSchema() 함수 호출하기
    let curSChema = require('curItem.file').createSchema(mongoose);
    console.log('%s 모듈을 불러들인 후 스키마 정의함.', curItme.file);

    // User 모델 정의
    let curModel = mongoose.model(curItem.collection, curSchema);
    console.log('%s 컬렉션을 위해 모델 정의함.', curItem.collection);

    // database 객체에 속성으로 추가
    database[curItem.schemaName] = curSchema;
    database[curItem.modelName] = curModel;
    console.log(
      '스키마 이름 [%s], 모델 이름 [%s]이 database 객체의 속성으로 추가됨.',
      curItem.schemaName,
      curItem.modelName
    );
  }

  app.set('database', database);
  console.log('database 객체가 app 객체의 속성으로 추가됨.');
}

// database 객체를 module.exports에 할당
module.exports = databaes;

```

**user_schema.js**

```

// crypto 모듈 불러들이기
let crypto = require('crypto');

// 데이터베이스 스키마 객체를 위한 변수 선언
let UserSchema;

let Schema = {};

Schema.createSchema = function (mongoose) {
  // 스키마 정의

  ...

  console.log('UserSchema 정의함.');

  return UserSchema;
};

// module.exports에 UserSchema 객체 직접 할당
module.exports = Schema;

```


















