# 10_setTimeout, setInterval, requestAnimationFrame

Created: Jun 16, 2020 3:47 PM

# Scheduling

함수가 특정 시간에 실행되도록 결정한다.

`setTimeout` 과 `setInterval` 은 모두 자바스크립트의 부분이라기보다, 호스팅 환경이 가지고 있는 내부적인 스케쥴러 메서드이다. 모든 브라우저와 NodeJS에서 지원한다.

## setTimeout

```javascript
let timerId = setTimeout(func|code, [delay], [arg1], [arg2], ...)
// id 를 반환한다.
```

함수를 `setTimeout` 에 주고, `setTimeout` 이 함수를 실행한다.

변수에 할당해서 `clearTimeout(변수)` 으로 취소할 수 있다.

`setTimeout` 에서 숫자는 함수를 메시지 올리기까지의 **최소 대기 시간**이다. 지연될 수 있다.

재귀적으로 사용하여 실행 사이 지연을 보장할 수 있다.

`setTimeout` 은 **고정 지연**을 보장한다.

### `setTimeout(..., 0)`

```javascript
setTimeout(() => alert("World"));

alert("Hello");
```

콜 스택에 들어가는 순서 주의할 것.

### setTimeout 활용

CPU 소모가 심한 코드를 `setTimeout` 으로 분리해서 수행할 수 있다.

혹은 프로세스가 진행되는 동안 브라우저가 다른 작업을 수행할 수 있게 한다.

## setInterval

```javascript
let timerId = setInterval(func|code, [delay], [arg1], [arg2], ...)
```

정해진 매시간마다 함수를 실행한다.

`clearInterval` 로 취소할 수 있다.

1초보다 짧으면 브라우저가 강제로 간격을 조정할 수 있다.

CPU, 그래픽카드에 따라 느려질 수 있다.

함수 호출도 `setInterval` 의 한 부분으로 시간이 소비된다.

`setTimeout` 을 재귀적으로 사용하는 편이 더 좋다.

## Garbage collection

`setInterval` 과 `setTimeout` 모두 내부 참조가 함수 안에 생겨나고 스케쥴러에 저장된다. 함수가 외부 lexical 환경을 참조하기 때문에, 함수가 살아있는 동안 외부 변수들도 메모리를 차지한다.

함수 스케쥴링이 필요없어지면 취소하는 것이 좋다.

## requestAnimationFrame

```javascript
requestAnimationFrame(callback)
```

```javascript
function repeatOften() {
  // Do whatever
  requestAnimationFrame(repeatOften);
}
requestAnimationFrame(repeatOften);
```

브라우저가 업데이트, 렌더링 할 때마다 요청한다.

브라우저를 repaint 하기 직전에(==리페인트될 준비가 되었을 때) 콜백 함수를 실행한다.

스스로를 반복호출하지 않기 때문에 재귀적으로 사용해야 한다.

모니터 주사율에 맞추어 실행한다. 평균 주사율이 60FPS 라면 1초에 60번 실행한다. 

CPU, 그래픽카드에 최적화되어있다.

`setTimeout` , `setInterval` 과 마찬가지로 id 를 반환하므로 `cancleAnimationFrame` 으로 취소할 수 있다.

CSS의 `transition` 으로 처리하기 어려운 애니메이션이나, HTML5 의 `Canvas`, `SVG` 등의 애니메이션 구현을 위해 사용한다.

모든 애니메이션을 프레임 단위로 계산해야 하는 어려움이 있다.

```javascript
var start = null;
var element = document.getElementById('SomeElementYouWantToAnimate');
element.style.position = 'absolute';

function step(timestamp) {  // timestamp 매개 변수를 사용해서
  if (!start) start = timestamp;  // 시간이 변할 때마다

  var progress = timestamp - start;

  element.style.left = Math.min(progress / 10, 200) + 'px';

  if (progress < 2000) {
    window.requestAnimationFrame(step);  // 실행하도록 만든다.
  }
}

window.requestAnimationFrame(step);
```