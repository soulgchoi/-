# 04_명시적 변환, 암시적 변환, Nominal, 구조화, 덕 타이핑

Created: Jul 23, 2020 12:35 PM

## 암시적 변환Implicit Conversion

### 숫자 계산에서 String

연산자( `-` , `*` , `/` , `%` ) 가 포함된 숫자 계산에서 피연산자로 문자열을 전달하면, 문자열은 `Number` 함수를 호출하는 것과 유사하게 처리된다.

숫자만 포함하는 문자열은 숫자로 변환되지만, 숫자가 아닌 문자를 포함할 경우 `NaN` 을 반환한다.

```jsx
3 * "3" // 3 * 3
3 * Number("3") // 3 * 3
Number("5") // 5

Number("1.") // 1
Number("1.34") // 1.34
Number("0") // 0
Number("012") // 12

Number("1,") // NaN
Number("1+1") // NaN
Number("1a") // NaN
Number("one") // NaN
Number("text") // NaN
```

### `+` 연산자

- 수학적 덧셈
- 문자열 연결concatenation

두 가지 기능을 수행한다.

문자열이 `+` 연산자의 **피연산자**일 경우, 문자열을 숫자로 변환하는 대신 **숫자를 문자열로 변환**한다.

```jsx
// 문자열로 연결
1 + "2" // "12"
1 + "js" // "1js"

// 덧셈
1 + 2 // 3
1 + 2 + 1 // 4

// 덧셈 후 연결
1 + 2 + "1" // "31"
(1 + 2) + "1" // "31"

// 모두 연결
1 + "2" + 1 // "121"
(1 + "2") + 1 // "121"
```

### Object

객체는 대개 `[object Object]` 로 변환된다.

```jsx
"name" + {} // "name[object Object]
```

모든 자바스크립트 객체는 `toString` 메서드를 상속받기 떄문에 문자열로 형변환이 가능하다.

`toString` 으로 반환된 값은 문자열 연결, 수학적 계산에 동일하게 사용된다.

### Array

`join` 메서드를 매개변수 없이 호출하는 것과 유사하게 동작한다.

```jsx
"me" + [1,2,3] // "me1,2,3"
4 + [1,2,3] // "41,2,3"
4 * [1,2,3] // NaN
```

### `valueOf`

`valueOf` 메서드는 객체의 원시 값을 반환한다. `toString` 보다 우선해서 사용한다.

### 참&거짓

### false 반환

- `false`
- 0
- `null`
- `undefined`
- `""`
- `NaN`
- -0

나머지 값들은 모두 `true` 를 반환한다.

### `NaN`

`NaN` 은 자기 자신과 같지 않은 유일한 값이다.

```jsx
NaN === NaN  // false

const notANumber = 3 * "a" // NaN

notANumber == notANumber // false
notANumber === notANumber // false

if (notANumber !== notANumber) // true
```

## 명시적 형변환Explict Conversion

명시적 형변환은 개발자가 직접 코드를 작성하여 어떤 형으로 바꿀지 명시해주는 것을 말한다.

`parseInt` , `Number` , `parseFloat` , `toString` 등의 메서드를 사용해 어떤 타입으로 형변환할지 직접 작성한다.

## 명칭적(명목적) 타이핑Nominal Typing

특정 키워드를 통해 타입을 지정해 사용하는 방식이다.

같은 이름의 자료형으로 선언된 경우에만 변수를 호환해서 사용할 수 있다.

## [덕 타이핑Duck Typing](https://ko.wikipedia.org/wiki/%EB%8D%95_%ED%83%80%EC%9D%B4%ED%95%91)

동적 타이핑의 한 종류로, 객체의 변수 및 메서드의 집합이 객체의 타입을 결정하는 것을 말한다.