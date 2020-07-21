# 18_Object.create와 Object.assign

Created: Jun 24, 2020 2:20 PM

# Object.create

`Object.create()` 메서드는 지정된 프로토타입 객체 및 속성(property)을 갖는 새 객체를 만든다.

```jsx
Object.create(proto[, propertiesObject])
```

✔ `proto`

새로만든 객체의 프로토타입이어야 할 객체.

✔ `propertiesObject`

선택사항. 지정되고 `undefined` 가 아니면, 자신의 속성(자체에 정의되어 프로토타입 체인에서 열거가능하지 않은 속성)이 열거 가능한 객체는 해당 속성명으로 새로 만든 객체에 추가될 속성 설명자(descriptor)를 지정한다.

`Object.defineProperties()` 의 두 번째 인수에 해당한다.

✔ 지정된 프로토 타입 개체와 속성을 갖는 새로운 개체를 반환한다.

✔ `proto` 매개변수가 `null` 또는 객체가 아닌 경우 `TypeError` 발생.

✔ `null` 인 경우 빈 객체를 생성한다.

`Object.create` 와 `new` 는 모두 새로운 객체를 만들고 프로토타입을 상속받는다.

하지만 `new` 가 실제로 생성자 코드를 실행하는 반면,

`Object.create` 는 생성자 코드를 실행하지 않는다.

그렇기 때문에 아래처럼 `Object.create()` 로 객체를 생성한 뒤,

`.prototype.constructor` 로 원래 생성자를 찾아갈 수 있도록 만든다.

(`생성자.prototype.constructor === 생성자`)

```jsx
// Shape - 상위클래스
function Shape() {
  this.x = 0;
  this.y = 0;
}

// 상위클래스 메서드
Shape.prototype.move = function(x, y) {
  this.x += x;
  this.y += y;
  console.info('Shape moved.');
};

// Rectangle - 하위클래스
function Rectangle() {
  Shape.call(this); // super 생성자 호출.
}

// 하위클래스는 상위클래스를 확장
Rectangle.prototype = Object.create(Shape.prototype);
Rectangle.prototype.constructor = Rectangle;

var rect = new Rectangle();

console.log('Is rect an instance of Rectangle?', rect instanceof Rectangle); // true
console.log('Is rect an instance of Shape?', rect instanceof Shape); // true
rect.move(1, 1); // Outputs, 'Shape moved.'
```

`mixin` 으로 여러 객체에서 상속할 수 있다.

`Object.create` 로 생성한 객체는 `instanceof` 를 쓸 수 없고 대신 `isPrototypeOf` 를 사용한다.

# Object.assingn

`Object.assign()` 메소드는 열거할 수 있는 하나 이상의 출처 객체로부터 대상 객체로 속성을 복사할 때 사용한다.. 대상 객체를 반환한다.

```jsx
Object.assing(target, ...sources)
```

✔ `target`

대상 객체

✔ `sources`

하나 이상의 출처 객체

출처 객체의 getter 와 setter 를 호출한다.

즉, 속성을 단순히 복사하거나 새롭게 정의하는 것이 아니라 할당하는 것이다.

```jsx
const obj = { a: 1 };
const copy = Object.assign({}, obj);
console.log(copy); // { a: 1 }
```

`Object.assign()` 의 출처 값이 객체에 대한 참조인 경우, 참조 값만을 복사한다.

즉, 얕은 복사이다.

```jsx
let obj = { 
  a: 1,
  b: { 
    c: 2,
  },
}

let newObj = JSON.parse(JSON.stringify(obj));

obj.b.c = 20;
console.log(obj); // { a: 1, b: { c: 20 } }
console.log(newObj); // { a: 1, b: { c: 2 } } (New Object Intact!)
```

`JSON.parse(JSON.stringify(object))` 를 사용하면 불변성을 가지는 깊은 복사를 할 수 있다.

대신 이 방법으로는 메서드를 복사할 수 없다. 순환 객체도 복사할 수 없다.

`Object.assing()` 은 열거 가능한 속성만 복사한다고 되어있는데,

```jsx
let someObj = {
  a: 2,
}

let obj = Object.create(someObj, { 
  b: {
    value: 2,  
  },
  c: {
    value: 3,
    enumerable: true,  
  },
});

let objCopy = Object.assign({}, obj);
console.log(objCopy); // { c: 3 }
```

`enumerable` 속성 서술자를 가지고 있기 때문에 복사되었다.

객체를 복사하는 다른 방법으로 전개 구문 `...` 를 사용할 수 있다.

```jsx
const array = [
  "a",
  "c",
  "d", {
    four: 4
  },
];
const newArray = [...array];
console.log(newArray);
// Result 
// ["a", "c", "d", { four: 4 }]
```

---

참고 

[https://www.zerocho.com/category/JavaScript/post/573d812680f0b9102dc370b7](https://www.zerocho.com/category/JavaScript/post/573d812680f0b9102dc370b7)

[https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/create](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/create)

[https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/assign](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)