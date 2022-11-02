### 노드의 자바스크립트와 친해지기

C 언어나 자바와 같은 타입 기반의 언어 (Type based language)는 메모리를 절약하기 위해 정수와 문자열을 만들 때 다른 크기의
변수 상자를 만들고 변수 앞에 int, String과 같은 타입(Type, 자료형)을 지정한다.

그러나 자바스크립트는 자료형을 명시하지 않는다. 이 때문에 자바스크립트는 모든 변수를 let 키워드로 선언하고 사용한다.

### 배열의 모든 요소 하나씩 확인하기
>1

```
let Users = [
  { name: '소녀시대', age: 20 },
  { name: '걸스데이', age: 22 },
  { name: '티아라', age: 23 },
];

console.log("배열 요소의 수 : %d", Users.length);
for(let i = 0; i < Users.length; i++) {
  console.log("배열 요소 #" + [i] + " : %s ", Users[i].name);
}
```
>2

```
let Users = [
  { name: '소녀시대', age: 20 },
  { name: '걸스데이', age: 22 },
  { name: '티아라', age: 23 },
];

console.log('\nforEach 구문 사용하기');
Users.forEach(function(item, index){
  console.log("배열 요소 #"+ index + " : %s", item.name);
});
```

### 배열에 값 추가 및 삭제하기

<table>
  <thead>
    <tr>
      <th>속성 / 메소드 이름</th>
      <th>설명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>push(object)</td>
      <td>배열의 끝에 요소를 추가한다.</td>
    </tr>
    <tr>
      <td>pop()</td>
      <td>배열의 끝에 요소를 삭제한다.</td>
    </tr>
    <tr>
      <td>unshift()</td>
      <td>배열의 앞에 요소를 추가한다.</td>
    </tr>
    <tr>
      <td>shift()</td>
      <td>배열의 앞에 있는 요소를 삭제한다.</td>
    </tr>
    <tr>
      <td>splice(index, removeCount, [Object]</td>
      <td>여러 개의 객체를 요소로 추가하거나 삭제한다.</td>
    </tr>
    <tr>
      <td>slice(index, copyCount)</td>
      <td>여러 개의 요소를 잘라내어 새로운 배열 객체로 만든다.</td>
    </tr>
  </tbody>
</table>

### 배열 중간 요소 삭제

delete 키워드를 사용하여 인덱스를 이용해 배열 요소를 삭제할 수 있다. 그러나 삭제 후에도 배열의 갯수가 그대로인 것을
볼 수 있다. 삭제된 인덱스에 해당하는 배열 요소는 undefined로 남아 있는다.

따라서 배열 요소를 담는 공간까지 없애 주는 splice() 메소드를 사용하는 것이 좋다.

splice() 메소드는 배열 요소 여러 개를 한꺼번에 추가하거나 삭제할 수 있는 방법이다.

```
let Users = [
  { name: '소녀시대', age: 20 },
  { name: '트와이스', age: 22 },
];

Users.splice(1, 0, { name: '애프터스쿨', age: 25 });
console.log('splice()로 요소를 인덱스 1에 추가한 후');
console.dir(Users);
```

### slice() 메소드로 배열 일부 요소 복사하여 새로운 배열 만들기

```
let Users = [
  { name: '소녀시대', age: 20 },
  { name: '트와이스', age: 22 },
];

let Users2 = Users.slice(0, 1);

console.dir(Users2);
```

### 콜백 함수 이해하기

함수를 파라미터로 전달하는 경우는 대부분 비동기 프로그래밍(Non-Blocking Programming) 방식으로 코드를 만들 때이다.
예를 들어, 더하기 함수를 실행한 후 결과 값이 반환될 때까지 기다리지 않고 그다음 코드를 실행하려면 비동기 방식으로
코드를 만들어야 한다. 

즉 더하기 함수를 실행하는 데 시간이 걸릴 수 있기 때문에 그다음 코드를 바로 실행한다. 그러고 나서 연산이 끝났을 때
파라미터로 전달한 함수가 실행될 수 있다면 그 시점에 결과를 처리할 수 있으므로 효율적인 프로그램을 만들 수 있다.

이때 파라마터로 전달되는 함수를 **콜백 함수(Callback function)** 이라고 한다.

콜백 함수는 함수가 실행되는 중간에 호출되어 상태 정보를 전달하거나 결과 값을 처리하는 데 사용된다.

```
function add(a, b, callback) {
  let result = a + b;
  callback(result);
}

add(10, 10, function(result) {
  console.log('파라미터로 전달된 콜백 함수 호출됨.');
  console.log('더하기 (10, 10)의 결과 : %d', result);
});
```

더하기 함수를 정의할 때는 더 이상 값을 반환하지 않도록 return 키워드를 사용하는 코드 부분을 삭제한다.
그 대신 더하기 연산을 한 결과 값은 파라미터로 전달된 콜백 함수를 호출하면서 그 콜백 함수로 전달한다.

콜백 함수는 미리 변수에 할당해 두었다가 add() 함수를 호출할 때 파라미터로 전달할 수도 있지만, add() 함수를 호출할 때
익명 함수로 만들어서 파라미터로 바로 전달할 수도 있다. 콜백 함수는 더하기 연산을 하는 코드 아래에서 호출되는데 이때
콘솔 창에 메시지를 출력한다. 

### 함수 안에서 값을 반환할 때 새로운 함수를 만들어 반환하는 방법

```
function add(a, b, callback) {
  let result = a + b;
  callback(result);

  let history = function () {
    return a + ' + ' + b + ' = ' + result;
  };
  return history;
}

let add_history = add(10, 10, function (result) {
  console.log('파라미터로 전달된 콜백 함수 호출됨');
  console.log('더하기 (10, 10)의 결과 : %d', result);
});

console.log('결과 값으로 받은 함수 실행 결과 : ' + add_history());
```

### 프로토타입 객체 만들기

자바스크립트의 객체를 만들 때는 중괄호를 이용한다. 그런데 자바스크립트 객체는 함수를 이용해서 만들 수도 있다. 그 이유는 함수도 객체이기 때문이다.
함수에 여러 가지 기능과 속성이 추가되면서 객체 지향(Object oriented) 언어에서 객체의 원형(Prototype)인 클래스를 만들고, 그 클래스에서 새로운 인스턴스 객체를
여러 개 만들어내듯이 자바스크립트에서도 객체의 원형을 정의한 후 그 원형에서 새로운 인스턴스 객체를 만들어 낼 수 있다.

```
function Person(name, age) {
  this.name = name;
  this.age = age;
}

Person.prototype.walk = function (speed) {
  console.log(speed + 'km 속도로 걸어간다.');
};

let person01 = new Person('소녀시대', 20);
let person02 = new Person('걸스데이', 22);

console.log((person01.name = '객체의 walk(10)을 호출한다.'));
person01.walk(10);
```

Person 객체는 name과 age 속성을 갖게 되었다. 이제 이 객체에 walk 함수를 속성으로 추가하고 싶다면 Person.walk = function() {...}과 같은 형태가 아니라 
Person.prototype.walk = function() {...}과 같은 형태로 만든다. 이것은 Person 객체가 실제 데이터를 담기 위해 만들어진 게 아니라 다른 인스턴스 객체를 만들기 위한
원형 틀로 만들어졌기 때문이다. Person 객체 안에 있는 prototype 속성에 데이터나 함수를 속성으로 추가하면 실제 인스턴스 객체를 만들 때 메모리를 효율적으로 관리할 수 있다.

> 두 코드는 같은 결과를 보여준다.

```
Person.walk = function() {...}
Person.prototype.walk = function() {...}
```

> This
 
**this**는 함수를 호출한 객체이다.

자바스크립트에서 객체 지향 방식으로 코드를 구성하기 위해 생성자 함수로 객체를 만들면, 그 객체 안에서 사용하는 this 키워드는 그 함수를 호출하는 객체를 가리킨다.

**prototype 속성으로 추가하면 인스턴스 객체를 만들 때 메모리를 효율적으로 관리할 수 있다.**






































