### 노드 간단하게 살펴보기

**전역 객체**

- console 
  : 콘솔에 로그를 보여주는 객체
- process
  : 프로세스의 실행에 대한 정보를 다루는 객체
- exports
  : 모듈을 다루는 객체

### console 객체  메소드
  
- dir(object)
  : 자바스크립트 객체의 속성들을 출력한다.
- time(id)
  : 실행 시간을 측정하기 위한 시작 시간을 기록한다.
- timeEnd(id)
  : 실행 시간을 측정하기 위한 끝 시간을 기록한다.

**Example**

코드 실행시간 구하기

```
let result = 0;

console.time('duration_sum');

for (let i = 1; i <= 1000; i++) {
  result += 1;
}

console.timeEnd('duration_sum');
console.log('1 부터 1000 까지 더한 결과물 : %d', result);
```

파일 이름, 파일 path 구하기

```
console.log('현재 실행한 파일의 이름 : %s', __filename);
console.log('현재 실행한 파일의 패스 : %s', __dirname);
```

### process 객체 메소드

- argv : 프로세스를 실행할 때 전달되는 파라미터(매개변수) 정보
- env : 환경 변수 정보
- exit() : 프로세스를 끝내는 메소드

```
if (process.argv.length > 2) {
  console.log('세 번째 파라미터의 값 : %s', process.argv[2]);
}

process.argv.forEach(function(item, index) {
  console.log(index + ' : ', item);
});
```

### 노드에서 모듈 사용하기

main.js <- module1.js

main.js
```
let module1 = require('module1');
module1.함수이름();
```

module1.js
```
exports.함수이름 = 함수정의;
```

모듈을 만들 때 module1.js 처럼 별도의 자바스크립트 파일을 만든 후 그 코드에서 exports 객체를 사용한다.
exports 객체의 속성으로 변수나 함수를 지정하면 그 속성을 main.js 와 같은 메인 자바스크립트 파일에서 불어와 사용할 수 있다.

모듈을 불러올 때는 require() 메소드를 사용하면, 모듈로 만들어 둔 파일의 이름을 이 메소드의 파라미터로 전달한다.
require() 메소드를 호출하면 모듈 객체가 반환되고, 모듈에서 exports 객체에 설정한 속성들은 이 모듈 객체를 통해 접근할 수 있다.

### exports vs module.exports

exports 외에 module.exports 를 사용할 수도 있다. exports 에는 속성을 추가할 수 있어 여러 개의 변수나 함수를 각각의 속성으로 추가할 수 있다. 이에 반해 module.exports 에는
하나의 변수나 함수 또는 객체를 직접 할당한다. 일반적으로 객체를 그대로 할당하며, 이렇게 할당한 객체 안에 넣어 둔 변수나 함수를 메인 파일에서도 사용할 수 있다.

















