### 노드의 기본 기능 알아보기

> 주소 문자열과 요청 파라미터 다루기

웹 사잍에 접속하기 위한 사이트 주소 정보는 노드에서 URL 객체로 만들 수 있다.

URL의 주소 문자열은 단순 문자열이므로 서버에서 이 정보를 받아 처리할 때 어디까지가 사이트 주소인지, 어떤 내용이 요청 파라미터인지 구별해야 한다.
이 구별을 위해서 ? 기호를 기준으로 앞에 있는 문자열과 뒤에 있는 문자열을 분리하는 경우가 많다. 이 작업을 쉽게 할 수 있도록 노드에 미리 만들어 둔 모듈이 **url 모듈**이다.

### 주소 문자열을 URL 객체로 변환하기

url 모듈에서 문자열을 객체로 만들거나 객체를 문자열로 만들기 위해 사용하는 주요 메서드는 다음과 같다.

<table>
  <tr>
    <th>메소드 이름</th>
    <th>설명</th>
  </tr>
  <tr>
    <td>parse()</td>
    <td>주소 문자열을 파싱하여 URL 객체를 만들어 준다.</td>
  </tr>
  <tr>
    <td>format()</td>
    <td>URL 객체를 주소 문자열로 변환한다.</td>
  </tr>
</table>
 
  
```
let url = require('url');

// 주소 문자열을 URL 객체로 만들기
let curURL = url.parse(
  'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=steve+jobs'
);

// URL 객체를 주소 문자열로 만들기
let curStr = url.format(curURL);

console.log('주소 문자열 : %s', curStr);
console.dir(curURL);
```

### 요청 파라미터 확인하기
  
URL 객체의 속성을 보면 주소 문자열의 여러 가지 정보가 포함되어 있다. 그중에서도 query 속성은 요청 파라미터 정보를 가지고 있는데 이 정보를 잘 살펴보면 여러 개의 요청 파라미터가
모두 들어 있다. 웹 서버에서는 클라이언트에서 요청한 요청 파라미터를 받아 처리할 때가 많으므로 이 query 속성에 들어 있는 문자열을 다시 각각의 요청 파라미터로 분리해야 한다.

요청 파라미터는 & 기호로 구분되는데 **querystring 모듈**을 사용하면 요청 파라미터를 쉽게 분리할 수 있다.

```
// 요청 파라미터 구분하기
let querystring = require('querystring');
let param = querystring.parse(curURL.query);

console.log('요청 파라미터 중 query의 값 : %s', param.query);
console.log('원본 요청 파라미터 : %s', querystring.stringify(param));
```

<table>
  <tr>
    <th>메소드 이름</th>
    <th>설명</th>
  </tr>
  <tr>
    <td>parse()</td>
    <td>요청 파라미터 문자열을 파싱하여 요청 파라미터 객체로 만들어 준다.</td>
  </tr>
  <tr>
    <td>stringify()</td>
    <td>요청 파라미터 객체를 문자열로 변환한다.</td>
  </tr>
</table>

### 이벤트 이해하기

노드는 대부분 이벤트를 기반으로 하는 비동기 방식으로 처리한다. 그리고 비동기 방식으로 처리하기 위해 서로 이벤트를 전달한다. 예를 들어,
어떤 함수를 실행한 결과물도 이벤트로 전달한다. 이벤트는 한쪽에서 다른 쪽으로 알림 메시지를 보내는 것과 비슷하다. 노드에는 이런 이벤트를 보내고 받을 수 있도록
**EventEmitter**라는 것이 만들어져 있다. 

> **이벤트**는 한쪽에서 다른 쪽으로 어떤 일이 발생했음을 알려주는 것이다. 이때 다른 한 쪽에서 이 이벤트를 받고 싶다면 이벤트 리스너를 등록할 수 있다.
**이벤트 리스너**는 특정 이벤트가 전달되었을 때 그 이벤트를 처리할 수 있도록 만들어 둔 것을 말한다.

**이벤트 보내고 받기**

<table>
  <tr>
    <th>메소드 이름</th>
    <th>설명</th>
  </tr>
  <tr>
    <td>on(event, listener)</td>
    <td>지정한 이벤트의 리스너를 추가한다.</td>
  </tr>
  <tr>
    <td>once(event, listener)</td>
    <td>지정한 이벤트의 리스너를 추가하지만 한 번 실행한 후에는 자동으로 리스너가 제거된다.</td>
  </tr>
  <tr>
    <td>removeListener(event, listener)</td>
    <td>지정한 이벤트에 대한 리스너를 제거한다.</td>
  </tr>  
</table>

```
process.on('exit', function () {
  console.log('exit 이벤트 발생함.');
});

setTimeout(function () {
  console.log('2초 후에 시스템 종료 시도함.');

  process.exit();
}, 2000);
```

process 객체는 노드에서 언제든지 사용할 수 있는 객체인데 이미 내부적으로 EventEmitter 를 상속받도록 만들어져 있어서 on() 과 emit() 메소드를 바로 사용할 수 있다.

그렇다면 미리 정의되어 있는 이벤트가 아니라 우리가 직접 만든 이벤트는 어떻게 처리할 수 있을까?

```
process.on('tick', function (count) {
  console.log('tick 이벤트 발생함 : %s', count);
});

setTimeout(function () {
  console.log('2초 후에 tick 이벤트 전달 시도함');

  process.emit('tick', '2');
}, 2000);
```

tick 이벤트를 직접 만들고 2초 후에 setTimeout() 메소드를 사용해 process.emit() 메소드를 호출하면서 tick 이벤트를 process 객체로 전달했다. process.on() 메소드를 호출하여
이벤트를 등록하면 이 메소드를 호출하면서 파라미터로 전달한 tick 이벤트가 발생했을 때 그다음에 나오는 콜백 함수가 실행된다. 


### 계산기 객체를 모듈로 만들어 보기

> ch01.js

```
let util = require('util');
let EventEmitter = require('events').EventEmitter;

let Calc = function() {
  let self = this;
  
  this.on('stop', function() {
    console.log('Calc에 stop event 전달됨.');
  });
};

util.inherits(Calc, EventEmitter);

Calc.prototype.add = function(a, b) {
  return a + b;
}

module.exports = Calc;
module.exports.title = 'calculator';
```

> ch02.js

```
let Calc = require('./ch01');

let calc = new Calc();
calc.emit('stop');

console.log(Calc.title + '에 stop 이벤트 전달함.');
```

### 파일 다루기

> 동기식 IO

```
let fs = require('fs');

// 파일을 동기식 IO로 읽어 들인다.
let data = fs.readFileSync('./package.json', 'utf8');

// 읽어 들인 데이터를 출력한다.
console.log(data);
```

> 비동기식 IO

```
let fs = require('fs');

// 파일을 비동기식 IO로 읽어 들인다.
fs.readFile('./package.json', 'utf8', function(err, data) {
    // 읽어 들인 데이터를 출력한다.
    console.log(data);
});

console.log('프로젝트 폴더 안의 package.json 파일을 읽도록 요청했다.');
```

> 스트림 단위로 파일 읽고 쓰기

```

let fs = require('fs');

let infile = fs.createReadStream('./output.txt', { flags: 'r' });
let outfile = fs.createWriteStream('./output2.txt', { flags: 'w' });

infile.on('data', function (data) {
  console.log('읽어 들인 데이터', data);
  outfile.write(data);
});

infile.on('end', function () {
  console.log('파일 읽기 종료');
  outfile.end(function () {
    console.log('파일 쓰기 종료');
  });
});

```

> pipe() 메소드로 두 개의 스트림 연결

```

let fs = require('fs');

let inname = './output.txt';
let outname = './output2.txt';

fs.exists(outname, function (exists) {
  if (exists) {
    fs.unlink(outname, function (err) {
      if (err) throw err;
      console.log('기존 파일 [' + outname + '] 삭제함.');
    });
  }
  let infile = fs.createReadStream(inname, { flags: 'r' });
  let outfile = fs.createWriteStream(outname, { flags: 'w' });
  infile.pipe(outfile);
  console.log('파일 복사 [' + inname + '] -> [' + outname + ']');
});

```





  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
