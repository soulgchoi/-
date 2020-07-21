# 15_this, call, apply, bind

Created: Jun 21, 2020 11:17 PM

# this

## 자바스크립트의 `this`

`this` 는 `실행 컨텍스트` 이다. == 호출자가 누구인가 하는 것이다.

## 전역 컨텍스트

브라우저의 최상위 객체 `window` 를 context 객체로 갖는다.

전역 스코프에서 정의한 변수들은 전역 객체에 등록된다.

## 함수 컨텍스트

자바스크립트에서 `this` 는 함수 호출 방식에 따라 바인딩되는 객체가 달라진다.

함수를 선언할 때 X,

함수를 호출할 때 어떻게 호출되었느냐에 따라 `this` 에 바인딩할 객체가 동적으로 결정된다.

렉시컬 스코프와는 다르다.

### **암시적 바인딩**

어떤 객체를 통해 함수가 호출된다면 그 객체가 `this` 의 context 객체이다.

쉽게는 `.` 왼쪽을 참조한다고도 볼 수 있다.

```jsx
const bar = function () { console.log(this) };
const foo = {};
foo.bar = bar;

bar(); // window
foo.bar(); // bar, 객체를 통해 호출
```

함수가 전역 컨텍스트 내에서 호출되면 `this` 도 전역 실행 컨텍스트를 참조한다.

```jsx
const bar = function () { console.log(this) };
bar(); // window
```

`strict` 를 사용하면 전역 개체가 되지 않는다.

```jsx
const foo = function () { console.log(this) };
const bar = function () { 'use strict'; console.log(this); };

foo(); // window
bar(); // undefined
```

### 명시적 바인딩

`call` , `apply` , `bind` 메서드의 첫번째 인자가 `this` 컨텍스트 객체가 된다.

### new 바인딩

```jsx
function Person(name, age) {
	this.name = name;
	this.age = age;
}

var solji = new Person('최솔지', 28);
console.log(solji.name, solji.age);  // 최솔지, 28
```

생성자(constructor)로 사용하면 다른 객체지향 언어와 비슷한 방식으로 생성된 객체를 참조한다.

✔ **new 바인딩의 동작 순서**

1. 새 객체가 만들어진다.

2. 새로 생성된 객체의 Prototype 체인이 호출 함수의 프로토타입과 연결된다.

3. 1에서 생성된 객체를 `this` 컨텍스트객체로 사용(명시적으로)하여 함수가 실행된다.

4. 이 함수가 객체를 반환하지 않는 한 1에서 생성된 객체가 반환된다.

**프로토타입 객체로 정의할 때도 동일하다.**

new 바인딩 ≥ 명시적 바인딩 > 암시적 바인딩 ≥ 기본 바인딩

### Arrow Function

화살표 함수가 선언된 부분 스코프의 `this` 컨텍스트를 그대로 사용한다.

상위 컴포넌트의 `this` 를 하위에서 사용하기 위해 쓰인다.

# call, apply, bind

모든 함수 객체의 프로토타입 객체인 Function.prototype 객체의 메서드이다.

## call

즉시 함수를 호출한다.

첫 번째 인자가 `this` 를 대체한다. (== 호출될 컨텍스트를 지정한다.)

```jsx
var example = function (a, b, c) {
  return a + b + c;
};
example(1, 2, 3);
example.call(<컨텍스트 지정>, 1, 2, 3);
```

## apply

즉시 함수를 호출한다.

첫 번째 인자가 `this` 를 대체한다.

`call` 과 유사하지만 인수 배열을 사용할 수 있다.

```jsx
var example = function (a, b, c) {
  return a + b + c;
};
example(1, 2, 3);
example.apply(<컨텍스트 지정>, [1, 2, 3]);
```

즉, 여러 개의 인수가 있는 가변적인 함수를 만들 수 있다.

함수의 `arguments` 는 배열처럼 생겼지만 유사 배열이기 때문에 배열의 메서드는 쓸 수 없다.

하지만 `call` 이나 `apply` 를 쓰면 배열 메서드를 모두 사용할 수 있다.

## bind

함수가 가리키는 `this` 만 바꾸고, 함수를 호출하지는 않는다.

---

참고

[https://yuddomack.tistory.com/entry/자바스크립트-this의-4가지-동작-방식](https://yuddomack.tistory.com/entry/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-this%EC%9D%98-4%EA%B0%80%EC%A7%80-%EB%8F%99%EC%9E%91-%EB%B0%A9%EC%8B%9D)

[https://poiemaweb.com/js-this](https://poiemaweb.com/js-this)

[https://beomy.tistory.com/6](https://beomy.tistory.com/6)

[https://hyunseob.github.io/2016/03/10/javascript-this/](https://hyunseob.github.io/2016/03/10/javascript-this/)

[https://www.zerocho.com/category/JavaScript/post/5b0645cc7e3e36001bf676eb](https://www.zerocho.com/category/JavaScript/post/5b0645cc7e3e36001bf676eb)