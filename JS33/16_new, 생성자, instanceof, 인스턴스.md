# 16_new, 생성자, instanceof, 인스턴스

Created: Jun 23, 2020 6:50 PM

# new, 생성자

생성자 함수의 인스턴스를 만들고 변수에 할당한다.

`new` 로 객체를 생성하면 프로토타입 체인을 형성한다. → 프로퍼티 상속

`new` 오퍼레이터를 사용할 때 동작 순서

1. 새로운 빈 객체를 만들어낸다.
2. this를 새로 만들어진 객체에 bind한다.
3. 새로 만들어진 객체에 `__proto__`라 불리는 property를 더한다. 이것은 `constructor` 함수의 `prototype 객체`를 의미한다.
4. return this를 함수의 끝에 추가한다. 때문에 객체는 함수로부터 return되어 만들어진 것이다.

```jsx
function Student(name, age) {
	// this = {};

  this.name = name;
  this.age = age;

	// return this
}

var first = new Student('John', 26);
```

1. 새로운 객체를 만들어낸다 ― first 객체
2. `this`는 `first` 객체에 bound된다. 때문에 `this`에 대한 참조는 `first`를 향할 것이다.
3. `__proto__`가 추가된다. `first.__proto__`는 이제 `student.prototype`을 가리킨다.
4. 모든 것이 완료된 후에 새로운 `first` 객체는 새로운 `first` 변수에 `return`된다.

### 장점

매번 리터럴을 사용하는 것보다 짧고 쉽다.

(`Object.create` 를 매번 생성해서 프로퍼티를 전달하지 않고..)

생성자를 사용함으로써 재사용 가능한 객체 생성 코드를 구현할 수 있다.

# instanceof

생성자의 prototype 속성이 객체의 프로토타입 체인 어딘가 존재하는지 판별한다.

`typeof` 는 값이 원시타입 요소인지 확인한다.

```jsx
if (typeof value === 'string')
```

`instanceof` 는 값이 클래스 또는 생성자 함수의 인스턴스인지 확인한다.

```jsx
object instanceof constructor
```

`.constructor` 으로도 인스턴스의 constructor 속성을 볼 수 있다.

즉 `instanceof` 는 `object` 의 프로토타입 체인에 `constructor.prototype` 이 존재하는지 판별한다.

```jsx
// 생성자 정의
function C(){}
function D(){}

var o = new C();

// true, 왜냐하면 Object.getPrototypeOf(o) === C.prototype
o instanceof C;

// false, 왜냐하면 D.prototype이 o 객체의 프로토타입 체인에 없음
o instanceof D;

o instanceof Object; // true, 왜냐하면
C.prototype instanceof Object // true

C.prototype = {};
var o2 = new C();

o2 instanceof C; // true

// false, 왜냐하면 C.prototype이
// 더 이상 o의 프로토타입 체인에 없음
o instanceof C; 

D.prototype = new C(); // C를 D의 [[Prototype]] 링크로 추가
var o3 = new D();
o3 instanceof D; // true
o3 instanceof C; // true, 왜냐하면 이제 C.prototype이 o3의 프로토타입 체인에 존재
```

`instanceof` 의 값은 생성자 `prototype` 프로퍼티의 변화에 따라 바뀔 수 있다.