# 22_고차함수Higher-Order Function

Created: Jun 29, 2020 11:41 PM

# 고차함수Higher-Order Function

## 고차함수란

함수를 인자로 전달받거나 함수를 결과로 반환하는 함수를 말한다.

즉, 고차함수는 인자로 받은 함수를 필요한 시점에 호출하거나 클로저를 생성하여 반환한다.

자바스크립트 함수는 일급 객체이므로 값처럼 인자로 전달할 수 있고, 반환할 수도 있다.

### 일급 객체first-class object

생성, 대입, 연산, 인자 또는 반환값으로서의 전달 등 프로그래밍 언어의 기본적 조작을 제한없이 사용할 수 있는 대상을 의미한다.

1. 무명의 리터럴로 표현이 가능하다.
2. 변수나 자료 구조(객체, 배열 등)에 저장할 수 있다.
3. 함수의 파라미터에 전달할 수 있다.
4. 반환값으로 사용할 수 있다.

자바스크립트 함수는 일급 객체이다.

그러므로 함수를 변수에 할당하거나 파라미터로 넘길 수 있다.

### 고차함수 사용

`map`, `filter`, `reduce`는 자바스크립트 언어 내부에 포함된 고차함수이다.

모두 함수를 파라미터로 받는 함수들이다.

`setTimeout` 과 `addEventListener` 등등.. 함수 인자를 가지고 있는 함수들이 고차함수이다.

함수를 전달할 때 `()` 가 없으면 함수 객체 자체를, 있으면 함수 실행 결과를 전달한다.

✔ 예제

```jsx
const characters =  [
	{name:  'Luke Skywalker', img:  'http://example.com/img/luke.jpg', species:  'human'},
	{name:  'Han Solo', img:  'http://example.com/img/han.jpg', species:  'human'},
	{name:  'Leia Organa', img:  'http://example.com/img/leia.jpg', species:  'human'},
	{name:  'Chewbacca', img:  'http://example.com/img/chewie.jpg', species:  'wookie'}
];

// 아래의 함수들은 모두 순수함수이다.
const humans = data => data.filter(character => character.species ===  'human');
const images = data => data.map(character => character.img);
const compose = (func1, func2) => data => func2(func1(data));
const displayCharacterImages = compose(humans, images);

console.log(displayCharacterImages(characters));

/* 
Logs out the following array
	["http://example.com/img/luke.jpg",
	 "http://example.com/img/han.jpg",
	 "http://example.com/img/leia.jpg"
	 ]
*/
```

✔ 함수를 값으로 반환하는 예제

```jsx
const area = function() {
	return this.width * this.height;
};

const boundArea = area.bind({ width: 2, height: 3 });

boundArea();
```

### 장점

- 가독성이 좋다.

    조건문이나 반복문을 제거할 수 있다. 

- 변수 사용을 줄인다.

    오류 발생을 근본적으로 줄일 수 있다.

→ 부수효과(side effect)를 최대한 억제한다.

⇒ 함수형 프로그래밍

참고

[https://poiemaweb.com/js-array-higher-order-function](https://poiemaweb.com/js-array-higher-order-function)

[https://poiemaweb.com/js-function#3-first-class-object-일급-객체](https://poiemaweb.com/js-function#3-first-class-object-%EC%9D%BC%EA%B8%89-%EA%B0%9D%EC%B2%B4)

[https://velog.io/@victor/고차함수란고차함수](https://velog.io/@victor/%EA%B3%A0%EC%B0%A8%ED%95%A8%EC%88%98%EB%9E%80%EA%B3%A0%EC%B0%A8%ED%95%A8%EC%88%98)

[http://jeonghwan-kim.github.io/js/2017/04/03/high-order-function-in-javascript.html](http://jeonghwan-kim.github.io/js/2017/04/03/high-order-function-in-javascript.html)

[https://velog.io/@jakeseo_me/자바스크립트-개발자라면-알아야-할-33가지-개념-22-자바스크립트-자바스크립트-고차-함수Higher-Order-Function-이해하기](https://velog.io/@jakeseo_me/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%9D%BC%EB%A9%B4-%EC%95%8C%EC%95%84%EC%95%BC-%ED%95%A0-33%EA%B0%80%EC%A7%80-%EA%B0%9C%EB%85%90-22-%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-%EA%B3%A0%EC%B0%A8-%ED%95%A8%EC%88%98Higher-Order-Function-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0)