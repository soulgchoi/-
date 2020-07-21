# 19_map, reduce, filter

Created: Jun 25, 2020 11:57 PM

함수형 프로그래밍을 위해 세 함수를 알아둘 필요가 있다.

함수형 프로그래밍은 함수의 출력 값이 함수에 전달 된 인수에만 의존하는 프로그래밍 패러다임이다. 

모두 `Array.prototype` 에 정의되어 있으므로 어느 위치의, 어떤 배열에서도 사용할 수 있다.

# map

`[map()](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/map)` 메서드는 배열 내의 모든 요소 각각에 대하여 주어진 함수를 호출한 결과를 모아 새로운 배열을 반환한다.

```jsx
const array1 = [1, 4, 9, 16];

// pass a function to map
const map1 = array1.map(x => x * 2);

console.log(map1);
// expected output: Array [2, 8, 18, 32]
```

```jsx
arr.map(callback(currentValue[, index[, array]])[, thisArg])
```

콜백 함수를 각각의 요소에 대해 한번씩 순서대로 불러 그 함수의 반환값으로 새로운 배열을 만든다. 

콜백 함수는 (`undefined` 를 포함해서) 배열 값이 들어있는 인덱스에 대해서만 호출된다.

(`[]` 도 에러는 발생하지 않는다.)

`map` 은 호출한 배열 값을 변형하지 않는다. 콜백 함수에 의해 변형될 수는 있다.

# reduce

`[reduce()](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce)` 메서드는 배열의 각 요소에 대해 주어진 리듀서(reducer) 함수를 실행하고(왼쪽에서 오른쪽으로 반복), **하나의 결과값**을 반환한다. (number 가 아니다. value!!)

`reduceRight` 는 반대방향이다.

```jsx
const array1 = [1, 2, 3, 4];
const reducer = (accumulator, currentValue) => accumulator + currentValue;

// 1 + 2 + 3 + 4
console.log(array1.reduce(reducer));
// expected output: 10

// 5 + 1 + 2 + 3 + 4
console.log(array1.reduce(reducer, 5));
// expected output: 15
```

```jsx
arr.reduce(callback[, initialValue])
```

**리듀서** 함수는 네 개의 인자를 가진다.

1. 누산기accumulator (acc)

    콜백의 반환값을 누적한다.

    콜백의 이전 반환값 또는, 콜백의 첫 번째 호출이면서 `initialValue` 를 제공한 경우에는 `initialValue` 의 값이다.

2. 현재 값 (cur)
3. 현재 인덱스 (idx)

     `initialValue` 를 제공한 경우 0, 아니면 1

4. 원본 배열 (src)

    `reduce()` 를 호출한 배열

`initialValue` 는 옵션이다.

초기값을 제공하지 않으면 배열의 첫 번째 요소를 사용한다.

빈 배열에서 초기값 없이 `reduce` 를 호출하면 오류가 발생한다.

✔ 배열의 값 합산 

```jsx
var sum = [0, 1, 2, 3].reduce(function (accumulator, currentValue) {
  return accumulator + currentValue;
}, 0);
// sum is 6

var total = [ 0, 1, 2, 3 ].reduce(
  ( accumulator, currentValue ) => accumulator + currentValue,
  0
);
```

```jsx
const sum = (arr) => arr.reduce((total, item) => total += item, 0);
```

✔ 객체 배열의 값 합산

```jsx
var initialValue = 0;
var sum = [{x: 1}, {x:2}, {x:3}].reduce(function (accumulator, currentValue) {
    return accumulator + currentValue.x;
},initialValue)

console.log(sum) // logs 6

var initialValue = 0;
var sum = [{x: 1}, {x:2}, {x:3}].reduce(
    (accumulator, currentValue) => accumulator + currentValue.x
    ,initialValue
);

console.log(sum) // logs 6
```

✔ 중첩 배열 펼치기

```jsx
var flattened = [[0, 1], [2, 3], [4, 5]].reduce(
  function(accumulator, currentValue) {
    return accumulator.concat(currentValue);
  },
  []
);
// 펼친 결과: [0, 1, 2, 3, 4, 5]
```

✔ 객체 내의 값 인스턴스 개수 세기

```jsx
var names = ['Alice', 'Bob', 'Tiff', 'Bruce', 'Alice'];

var countedNames = names.reduce(function (allNames, name) { 
  if (name in allNames) {
    allNames[name]++;
  }
  else {
    allNames[name] = 1;
  }
  return allNames;
}, {});
// countedNames is:
// { 'Alice': 2, 'Bob': 1, 'Tiff': 1, 'Bruce': 1 }
```

이외에도 프로미스를 순차적으로 실행하거나 중복 제거, `map` 처럼 사용할 때 등등

✔ 프로미스 체이닝 

```jsx
let itemIDs = [1, 2, 3, 4, 5];
itemIDs.reduce((promise, itemID) => {  
  return promise.then(_ => api.deleteItem(itemID));  
}, Promise.resolve());

// 아래와 같다
Promise.resolve()  
.then(_ => api.deleteItem(1))  
.then(_ => api.deleteItem(2))  
.then(_ => api.deleteItem(3))  
.then(_ => api.deleteItem(4))  
.then(_ => api.deleteItem(5));
```

# filter

`[filter()](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)` 메서드는 주어진 함수의 테스트를 통과하는 모든 요소를 모아 새로운 배열로 반환한다.

```jsx
const words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];

const result = words.filter(word => word.length > 6);

console.log(result);
// expected output: Array ["exuberant", "destruction", "present"]
```

```jsx
arr.filter(callback(element[, index[, array]])[, thisArg])
```

콜백 함수에서 `true` 면 요소를 유지하고, `false` 면 버린다.

어떤 요소도 테스트를 통과하지 못하면 빈 배열을 반환한다.

`filter` 는 호출되는 배열을 변화시키지 않는다.

✔ 예제

```jsx
const fruits = ['apple', 'banana', 'grapes', 'mango', 'orange'];

// 검색 조건에 따른 배열 필터링(쿼리)
const filterItems = (query) => {
  return fruits.filter((el) =>
    el.toLowerCase().indexOf(query.toLowerCase()) > -1
  );
}

console.log(filterItems('ap')); // ['apple', 'grapes']
console.log(filterItems('an')); // ['banana', 'mango', 'orange']
```

`find` 는 조건에 적합한 첫번째 요소만 반환한다.

## 왜 map, reduce, filter 를 사용하는가?

- 인덱스를 통해 액세스하는 대신 현재 값으로 직접 작업한다.
- 배열의 혹시 모를 오류를 방지한다.
- 새 배열을 만들고 값을 그 안에 넣지 않아도 된다.

    최종 값을 한번에 반환하므로 반환 값을 새 변수에 할당하기만 하면 된다.

- `for` 루프를 쓰지 않아도 된다.

## map, reduce, filter 주의할 점

- 콜백 함수는 `return` 이 있어야 한다.