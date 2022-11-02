## 파일 업로드 기능 만들기

웹 서버는 기본적으로 서버에 저장된 문서를 조회하거나 데이터를 받아 저장할 수 있지만 파일 자체를 업로드하거나 다운로드하는 경우도 자주 있다.

특히 모바일 단말로 찍은 사진을 업로드하고 웹이나 모바일에서 사진을 다운로드하여 보는 일이 많아지면서 이미지 파일을 다루는 경우도 많다.

외장 모듈을 사용하면 익스프레스에서 파일을 업로드할 수 있다. 파일을 업로드할 때는 **멀티 파트(multipart) 포맷** 으로 된 파일 업로드 기능을 사용하며 파일 업로드 상태 등을 
확인할 수 있다.

> 멀티 파트 포맷은 웹 서버에서 파일을 업로드하기 위해 사용한다.

multipart 포맷은 음악이나 이미지 파일 등을 일반 데이터와 함께 웹 서버로 보내려고 만든 표준이다. 

**multer 미들웨어 설치해서 파일 업로드하기**

- 파일을 업로드할 때는 클라이언트에서 POST 방식으로 데이터를 전송하므로 body-parser 미들웨어를 함께 사용한다.

```

// Express 기본 모듈 불러오기
let express = require('express');
let http = require('http');
let path = require('path');

// Express의 미들웨어 불러오기
let bodyParser = require('body-parser');
let cookieParser = require('cookie-parser');
let static = require('serve-static');
let errorHandler = require('errorhandler');

// 오류 핸들러 모듈 사용
let expressErrorHandler = require('express-error-handler');

// Session 미들웨어 불러오기
let expressSession = require('express-session');

// 파일 업로드용 미들웨어
let multer = require('multer');
let fs = require('fs');

// 클라이언트에서 ajax로 요청했을 때 CORS(다중 서버 접속) 지원
let cors = require('cors');

// 익스프레스 객체 생성
let app = express();

// 기본 속성 설정
app.set('port', process.env.PORT || 3000);

// body-parser를 사용해 application/x-www-form-urlencoded 파싱
app.use(bodyParser.urlencoded({ extended: false }));

// body-parser를 사용해 application/json 파싱
app.use(bodyParser.json());

// public 폴더와 uploads 폴더 오픈
app.use('/public', static(path.join(__dirname, 'public')));
app.use('/uploads', static(path.join(__dirname, 'uploads')));

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

// 클라이언트에서 ajax로 요청했을 떄 CORS(다중 서버 접속) 지원
app.use(cors());

//multer 미들웨어 사용: 미들웨어 사용 순서 중요 body-parser -> multer -> router
// 파일 제한: 10개, 1G
let storage = multer.diskStorage({
  destination: function (req, file, callback) {
    callback(null, 'uploads');
  },
  filename: function (req, file, callback) {
    callback(null, file.originalname + Date.now());
  },
});

let upload = multer({
  storage: storage,
  limits: {
    files: 10,
    fileSize: 1024 * 1024 * 1024,
  },
});

// 라우터 사용하여 라우팅 함수 등록
let router = express.Router();

router
  .route('/process/photo')
  .post(upload.array('photo', 1), function (req, res) {
    console.log('/process/photo 호출됨');

    try {
      let files = req.files;

      console.dir('#===== 업로드된 첫번째 파일 정보 =====#');
      console.dir(req.files[0]);
      console.dir('#=====#');

      let originalname = '',
        filename = '',
        mimetype = '',
        size = 0;

      if (Array.isArray(files)) {
        // 배열에 들어가 있는 경우(설정에서 1개의 파일도 배열에 넣게 했음)
        console.log('배열에 들어있는 파일 갯수 : %d', files.length);

        for (let index = 0; index < files.length; index++) {
          originalname = files[index].originalname;
          filename = files[index].filename;
          mimetype = files[index].mimetype;
          size = files[index].size;
        }
      } else {
        // 배열에 들어가 있지 않은 경우(현재 설정에서는 해당 없음)
        console.log('파일 갯수 : 1 ');

        originalname = files[index].originalname;
        filename = files[index].name;
        mimetype = files[index].mimetype;
        size = files[index].size;
      }

      console.log(
        '현재 파일 정보 : ' +
          originalname +
          ', ' +
          filename +
          ', ' +
          mimetype +
          ', ' +
          size
      );

      // 클라이언트에 응답 전송
      res.writeHead('200', { 'Content-Type': 'text/html;charset=utf8' });
      res.write('<h3>파일 업로드 성공</h3>');
      res.write('<hr/>');
      res.write(
        '<p>원본 파일 이름 : ' +
          originalname +
          ' -> 저장 파일명 : ' +
          filename +
          '</p>'
      );
      res.write('<p>MIME TYPE : ' + mimetype + '</p>');
      res.write('<p>파일 크기 : ' + size + '</p>');
      res.end();
    } catch (err) {
      console.dir(err.stack);
    }
  });

app.use('/', router);

// Express 서버 시작
http.createServer(app).listen(app.get('port'), function () {
  console.log('익스프레스 서버를 시작했습니다 : ' + app.get('port'));
});

```


















