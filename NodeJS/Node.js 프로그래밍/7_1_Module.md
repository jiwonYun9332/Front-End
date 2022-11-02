## 익스프레스 프로젝트를 모듈화하기

> 객체의 속성으로 함수, 객체 추가하기

**user1.js**

```

// exports 객체 속성으로 함수 추가
exports.getUser = function() {
  return {id : 'test01', name : '소녀시대'};
}

// exports 객체 속성으로 객체 추가
exports.group = {id : 'group01' name : '친구'};

```

**module_test1.js**

```

// require() 메소드는 exports 객체를 반환함
let user1 = require('./user1');

function showUser() {
  return user1.getUser().name + ', ' + user1.group.name;
}

console.log('사용자 정보 : %s', showUser();

```

> exports에 객체 할당하기

**user2.js**

```

// Reason : exports는 속성으로, exports에 속성을 추가하면 모듈에서 접근하지만
//          exports에 객체를 지정하면 자바스크립트에서 새로운 변수로 처리함
exports = {
  getUser: function () {
    return { id: 'test01', name: '소녀시대' };
  },
  group: { id: 'group01', nmae: '친구' },
};

```

**module_test2.js**

```

// Reason : user2.js 파일에서 exports에 객체를 할당하였으므로,
// require()를 호출할 때 자바스크립트에서 새로운 변수로 처리함
// 결국 아무 속성도 없는 { } 객체가 반환됨
let user = require('./user2');

console.dir(user);

function showUser() {
  return user.getUser().name + ', ' + user.group.name;
}

console.log(showUser());

```

**결과 : user 변수에 어떤 속성도 들어 있지 않으므로 getUser() 메소드 호출 시 에러 발생**

> module.exports를 사용해서 객체를 그대로 할당하기

**user3.js**

```

// module.exports에는 객체를 그대로 할당할 수 있음
let user = {
  getUser: function () {
    return { id: 'test01', name: '소녀시대' };
  },
  group: { id: 'group01', name: '친구' },
};

module.exports = user;

```

**module_test3.js**

```

// require() 메소드는 객체를 반환함
let user = require('./user3');

function showUser() {
  return user.getUser.name + ', ' + user.group.name;
}

console.log('사용자 정보 : %s', showUser());

```

> module.exports에 함수만 할당하기

**user4.js**

```

// 인터페이스(함수 객체)를 그대로 할당할 수 있음

module.exports = function () {
  return { id: 'test01', name: '소녀시대' };
};


```

**module_test4.js**

```

// require() 메소드는 함수를 반환함
let user = require('./user4');

function showUser() {
  return user().name + ', ' + 'No Group';
}

console.log('사용자 정보 : %s', showUser());

```

> exports와 module.exports를 함께 사용하기

**user5.js**

```

// module.exports가 사용되면 exports는 무시됨
module.exports = {
  getUser: function () {
    return { id: 'test01', name: '소녀시대' };
  },
  group: { id: 'group01', name: '친구' },
};

exports.group = { id: 'group02', name: '가족' };

```

**module_test5.js**

```

// require() 메소드는 export가 아닌 module.exports로 설정된 속성을 반환함
let user = require('./user5');

function showUser() {
  return user.getUser().name + ', ' + user.group.name;
}

console.log('사용자 정보 : %s', showUser());

```

exports와 module.exports를 함께 사용하면 module.exports가 우선으로 적용되며 exports 전역 변수는 무시된다.

> require() 메소드의 동작 방식 이해하기

**module_test6.js**

```

// 가상으로 require() 함수를 정의해 보면 require() 함수가 내부적으로 처리되는 방식을 이해할 수 있음
let requireTest = function (path) {
  let exports = {
    getUser: function () {
      return { id: 'test01', name: '소녀시대' };
    },
    group: { id: 'group01', name: '친구' },
  };
  return exports;
};

let user = requireTest('...');

function showUser() {
  return user.getUser().name + ', ' + user.group.name;
}

console.log('사용자 정보 : %s', showUser());

```

## 모듈을 분리할 때 사용하는 전형적인 코드 패턴

> 함수를 할당하는 코드 패턴

**user7.js**

```

// 사용 패턴 : exports에 속성으로 추가된 함수 객체를 그대로 참조한 후 호출함
exports.printUser = function () {
  console.log('user 이름은 소녀시대입니다.');
};

```

**module_test7.js**

```

// 사용 패턴 : exports에 속성으로 추가된 함수 객체를 그대로 참조한 후 호출함
let printUser = require('./user7').printUser;

printUser();

```

> 인스턴스 객체를 할당하는 코드 패턴

**user8.js**

```

// 사용 패턴: module.exports에 인스턴스 객체를 만들어 할당함

// 생성자 함수
function User(id, name) {
  this.id = id;
  this.name = name;
}

User.prototype.getUser = function () {
  return { id: this.id, name: this.name };
};

User.prototype.group = { id: 'group01', name: '친구' };

User.prototype.printUser = function () {
  console.log('user 이름 : %s group 이름 : %s', this.name, this.group.name);
};
module.exports = new User('tesd01', '소녀시대');

```

**module_test8.js**

```

// 사용 패턴: new 연산자로 만든 인스턴스 객체를 module.exports에 할당한 후 그 인스턴스 객체의 함수를 호출함

let user = require('./user8');

user.printUser();

```

> 프로토타입 객체를 할당하는 코드 패턴

**user10.js**

```

// 사용 패턴: module.exports에 인스턴스 객체를 만들어 할당함

// 생성자 함수
function User(id, name) {
  this.id = id;
  this.name = name;
}

User.prototype.getUser = function () {
  return { id: this.id, name: this.name };
};

User.prototype.group = { id: 'group01', name: '친구' };

User.prototype.printUser = function () {
  console.log('user 이름 : %s group 이름 : %s', this.name, this.group.name);
};
module.exports = User;

```

**module_test10.js**

```

// 사용 패턴: module.exports에 프로토타입 객체를 정의한 후 할당함

let User = require('./user10');
let user = new User('test01', '소녀시대');

user.printUser();

```
