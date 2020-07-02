# 24_컬렉션Collection

Created: Jul 1, 2020 11:22 PM

# 컬렉션

목록성 데이터를 처리하는 자료구조를 통칭한다.

자료구조(Data Structure)는 어떤 정보를 담는 것을 의미하여, 하나의 데이터가 아닌 여러 데이터를 담을 때 사용하는 것이다.

## 자바스크립트 컬렉션

### Map

```jsx
const foo = new Map()

foo.set(key, value) 
foo.get(key)
foo.has(key)
foo.delete(key)
foo.clear()
foo.size

foo.keys()
foo.values()
foo.entries()
```

키와 값을 서로 연결(매핑)시켜 저장하며, 저장된 순서대로 각 요소들을 반복적으로 접근할 수 있도록 한다.

`Map` 객체에 저장되어 있는 각 요소들을 [키, 값] 형태의 배열로 반복적으로 반환해주는 `for...of` 를 사용할 수 있다.

```jsx
var sayings = new Map();
sayings.set("dog", "woof");
sayings.set("cat", "meow");
sayings.set("elephant", "toot");
sayings.size; // 3
sayings.get("fox"); // undefined
sayings.has("bird"); // false
sayings.delete("dog");

for (var [key, value] of sayings) {
  console.log(key + " goes " + value);
}
// "cat goes meow"
// "elephant goes toot"
```

- `Object` 와 `Map` 비교
    - [https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Map](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Map)
    - `Object`의 키는 `[Strings](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/String)`이며, Map의 키는 모든 값을 가질 수 있다.
    - `Object`는 크기를 수동으로 추적해야하지만, `Map`은 크기를 쉽게 얻을 수 있다.
    - `Map`은 삽입된 **순서대로** 반복된다.
    - 객체(Object)에는 prototype이 있어 Map에 기본 키들이 있다. (이것은 `map = Object.create(null)` 를 사용하여 우회할 수 있다. )
- 언제 `Map` 을 쓸까?
    - 실행 시까지 키를 알수 없고, 모든 키가 동일한 type이며 모든 값들이 동일한 type일 경우에는 objects를 대신해서 map을 사용해라.
    - 각 개별 요소에 대해 적용해야 하는 로직이 있을 경우에는 objects를 사용해라.
- `Map` 의 유용성
    - 기존 객체에 메타 데이터를 추가하거나 불변 객체에 추가 데이터를 넣기 위해 사용할 수 있다.

### WeakMap

```jsx
new WeakMap([iterable])
WeakMap.prototype.get(key) : this
WeakMap.prototype.set(key, value) : this
WeakMap.prototype.has(key) : boolean
WeakMap.prototype.delete(key, value) : boolean
```

`WeakMap` 객체는 object 만을 키로 허용하고 값은 임의의 값을 허용하는 키/값 형태의 요소의 집합이다. 키가 가지고 있는 객체에 대한 참조는 객체에 대한 참조가 더이상 존재하지 않을 경우 garbage collection(GC)의 수거 대상이 되는 약한 참조를 의미한다.

`Map`객체와 다른 점은 `WeakMap`의 키들은 열거형이 아니라는 점이다. (즉, 키 목록을 제공해 주는 메서드가 없다는 것이다.) 만약에 키 목록을 제공한다면 garbage collection의 상태, 결과에 따라 키 목록이 변하게 될 것이다.

`WeakMap` 은 객체의 사적인 정보를 저장하기 위해서 혹은 상세 구현 내용을 숨기기 위해서이다.

```jsx
const privates = new WeakMap();

function Public() {
  const me = {
    // Private data goes here
  };
  privates.set(this, me);
}

Public.prototype.method = function () {
  const me = privates.get(this);
  // Do stuff with private data in `me`...
};

module.exports = Public;
```

`WeakMap` 객체인 `privates` 는 export 되지 않는다.

- `Map` 과의 차이

    `Map` 은 객체가 계속 메모리에 남아있게 된다. (garbage collected 되지 않는다.)

    ```jsx
    const foo = new Map()

    let bar = { name: 'Ben' }

    foo.set(bar, { age: 25 })
    foo.get(bar) // { age: 25 }

    bar = null
    foo.entries() // [ [{ name: 'Ben' }, { age: 25 }] ]
    ```

    `WeakMap` 을 사용하면 제거할 수 있다.

    ```jsx
    const foo = new WeakMap()

    // You can only use objects as keys, no primitives
    foo.set('primitive', 1) // TypeError: Invalid value used as weak map key

    let bar = { name: 'Ben' }

    foo.set(bar, { age: 25 })
    foo.get(bar) // { age: 25 }

    bar = null
    // If there are no other reference to bar, it is removed as a key from foo
    ```

- `WaekMap` 장점

    `WeakMap` 에 저장된 객체는 인스턴스가 없으면 접근할 수 없다.

    ⇒ 개인 데이터에 사용하기 좋다.

    필요없는 DOM 요소를 garbage collect 할 수 있다.

### Set

```jsx
new Set([iterable]);

Set.add()
Set.clear()
Set.delete(value)
Set.entries()
Set.has(value)
Set.keys()
Set.values()
```

`[Set](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Set)` 객체는 값들의 집합이다. 입력된 **순서**에 따라 저장된 요소를 반복처리할 수 있다.

`Set` 은 **중복된 값을 허용하지 않는다.** 따라서 특정 값은 `Set` 내에서 하나만 존재하게 된다.

`Map` 처럼 `for...of` 로 반복하는 데 사용할 수 있다.

- `Array` 대신 `Set` 을 사용할 때 장점
    - `[indexOf](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/indexOf)`메서드를 사용하여 배열내에 특정 요소가 존재하는지 확인하는 것은 느리다.
    - 배열에선 해당 요소를 배열에서 잘라내야 하는 반면 Set객체는 요소의 값으로 해당 요소를 삭제하는 기능 제공한다.
    - `[NaN](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/NaN)`은 배열에서 indexOf메서드로 찾을 수 없다.
    - Set객체는 값의 유일성을 보장하기 때문에 직접 요소의 중복성을 확인할 필요가 없다.

### WeakSet

`[WeakSet](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/WeakSet)`객체는 객체를 저장하는 일종의 집합이다.

`WeakSet` 내의 중복된 객체는 없으며 `WeakSet` 내의 요소를 열거할 수는 없다.

- `Set` 과 차이점
    - `WeakSet` 은 객체만 저장할 수 있다. 특정 type 의 값을 저장할 수 없다.
    - 약한 참조를 가진다. WeakSet내에 저장되어 있는 객체에 대한 참조가 없게되면 garbage collection 대상이 되어 수거된다. 따라서 현재 저장되어 있는 객체에 대한 목록은 없으며 WeakSet은 열거형이 아니다.
- 장점

    메모리 누수가 발생하지 않기 때문에 안전하게 DOM 요소를 키로 저장할 수 있다.

참고

[https://tenlie10.tistory.com/10](https://tenlie10.tistory.com/10)

[https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Keyed_collections](https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Keyed_collections)