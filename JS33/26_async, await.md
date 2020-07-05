# 26_async, await

Created: Jul 5, 2020 11:52 AM

# async & await

## async function

자바스크립트에서 모든 비동기 함수는 사실상 `AsyncFunction` 객체이다.

```jsx
async function [name]([param1[, param2[, ..., paramN]]]) { statements }
```

암시적으로 `Promise` 를 사용하여 결과를 반환한다. 즉 `async function` 의 반환값은 암묵적으로 `Promise.resolve` 로 감싸진다.

`async` 함수에는 `await` 식이 포함될 수 있다. 

이 식은 함수의 실행을 일시중지하고 전달된 `Promise` 의 해결을 기다린 다음 `async` 함수의 실행을 다시 시작하고 완료 후 값을 반환한다.

✔ 예제

```jsx
async function hello() {
	return  'Hello Alligator!';
}
const b = hello();
console.log(b); // [object Promise] { ... }
```

`async` 함수의 반환값은 프로미스이기 때문에 아래처럼 사용해야 한다.

```jsx
async function hello() {
	return  'Hello Alligator!';
}

const b = hello();

b.then(x =>  console.log(x)); // Hello Alligator!
```

## await

`await` 는 `async function` 내부에서만 사용할 수 있다.

```jsx
[rv] = await expression;
```

반환값은 `Promise` 에 의해 만족되는 값이거나, `Promise` 가 아니 경우에는 그 값 자체이다.

`await` 문은 `async` 함수의 실행을 중단시키고, `Promise` 가 `resolve`(fulfill) 되거나 reject 되기를 기다리고, 다시 `async` 함수를 실행시킨다.

이때 `await` 문의 값은 `Promise` 에서 fulfill 된 값이다.

`await` 가 함수 실행을 중단시키는 동안 다른 스크립트나 이벤트를 다룰 수 있다.

```jsx
function f() {
  let promise = Promise.resolve(1);
  let result = await promise; // Syntax error
}
```

`await` 를 `async` 함수가 아닌 동기식 함수에서 사용하면 에러가 발생한다.

✔ 예제

위에서 `async` 함수의 반환값이 프로미스이기 때문에 `then()` 을 사용했는데,

```jsx
async function hello() {
	return  'Hello Alligator!';
}
const b = await hello();
console.log(b); // Hello Alligator!
```

`await` 를 사용하면 프로미스의 `resolve` 값을 반환한다.

### 에러 처리

`try ... catch` 구문을 사용하여 에러 처리를 동기적으로 수행할 수 있다.

```jsx
async function asyncFunc() {
  try {
    // fetch data from a url endpoint
    const response = await axios.get("/some_url_endpoint");
    const data = await response.json();
    return data;
  } catch(error) {
    console.log("error", error);
    // appropriately handle the error
  }
}
```

항상 프로미스를 반환하므로 `catch` 를 사용하여 처리되지 않은 오류도 처리할 수 있다.

여러 `await` 줄이있는 경우 `catch` 블록은 모든 줄에서 발생하는 오류를 포착한다.

## `await` 와 `Promise`

`await` 는 각 함수가 순차적으로 수행된다. 동시에 수행하려면 `Promise.all` 을 사용한다.

`Promise.all` 은 전달된 모든 프라미스가 `resolve` 되면 배열을 반환한다.

```jsx
async function asyncFunc() {
  const response = await Promise.all([
    axios.get("/some_url_endpoint"),
    axios.get("/some_url_endpoint")
  ]);
  ...
}
```

### 왜 async/await 를 쓰는가...

프로미스 패턴은 동일한 코드를 반복하는 경우가 많다.

`async/await` 는 가독성이 뛰어나다.

참고

[https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/async_function](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/async_function)

[https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/AsyncFunction](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/AsyncFunction)

[https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/await](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/await)