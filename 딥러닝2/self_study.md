# 이미지 정규화

## 를 위한 이미지와 넘파이 배열 다루기 연습

#### OpenCV

openCV 로 이미지를 다뤄보려고 설치했지만 실제로 쓰지는 않아서 설치 명령어만 기재한다.

```powershell
# 아나콘다
conda install opencv
# pip
pip install opencv-python
```

---

numpy, pillow, tensorflow 를 사용했다.

```python
import numpy as np
import tensorflow as tf
from PIL import Image
from tensorflow.keras.layers import Input
```

이렇게 임포트해두고 시작한다.

```python
def get_path_caption():
    img_paths = []
    captions = []

    with open('..\\..\\datasets\\captions.csv') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|')
        next(csvreader)
        for row in csvreader:
            img_paths.append(row[0])
            captions.append(row[2].lstrip())

    return img_paths, captions

img_paths, captions = get_path_caption()
```

지난 서브 프로젝트에서 작성한 코드로 이미지 경로를 불러왔다.
이 코드는 팀 프로젝트가 진행되면서 바뀔 예정이다.

불러온 이미지로 다양하게 프린트 해본다.

```python
# 이미지 하나만 찍어보기
img_name = img_paths[0]
img = Image.open('..\\..\\datasets\\images\\' + img_name)

# numpy 배열로 변경해서 각 픽셀값 출력
pix = np.array(img)
print(pix)
```

output:

    [[[  0   6   4]
      [  2   6   5]
      [  3   5   4]
      ...
      [219 244 249]
      [222 253 255]
      [221 249 250]]
    
     [[  4   8   7]
      [  3   5   4]
      [  5   7   6]
      ...
      [228 253 250]
      [212 245 254]
      [218 253 255]]
    
     [[  3   3   3]
      [  4   4   4]
      [  5   5   5]
      ...
      [242 255 255]
      [232 255 251]
      [214 245 250]]
    
     ...
    
     [[166 177 147]
      [180 188 131]
      [130 155 100]
      ...
      [106 158  86]
      [134 172 113]
      [107 163  72]]
    
     [[202 219 151]
      [144 175 115]
      [133 160 117]
      ...
      [157 188 129]
      [156 186 124]
      [157 196 117]]
    
     [[144 157  87]
      [185 211 172]
      [184 214 152]
      ...
      [156 186 122]
      [191 200 153]
      [106 126  65]]]
    



``````python
print(img.size)  # 가로세로 몇 픽셀인지
print(pix[200][200])  # 200, 200 위치의 rgb 값
print(img.mode)  # rgb 인지 hdr 인지 그런거?
print(img.format)  # 이미지 형식
``````

output: 

    (333, 500)
    [103 70 25]
    RGB
    JPEG



``````python
data = np.asarray(img)  # 넘파이 배열로 바꾼다.
print(type(data))
print(data.shape)  # 배열과 차원을 확인한다. rgb 이미지라 3 채널
# print(data)  # 위에서 print(pix) 했을 때와 동일
``````

ouput:

    <class 'numpy.ndarray'>
    (500, 333, 3)



``````python
data.resize(255, 255)

data2 = data.copy()
data2.resize(255, 255)

print(data2)
print(data2.shape)
``````

`data.resize()` 는
ValueError: cannot resize this array: it does not own its data
에러가 발생한다.

`data` 를 카피한 `data2` 는 `resize()` 가 된다.

#### ❗ `np.array()` 와 `np.asarray()` 의 차이 

​	([https://studymake.tistory.com/406](https://studymake.tistory.com/406) 참고)

​	`np.array()` : 복사본 생성, 원본 데이터를 변경해도 바뀌지 않는다.

​	`np.asarray()` : 참조본 생성, 원본이 변경되면 자동으로 같이 변경된다.

output: 

    [[[  0   6   4]
      [  2   6   5]
      [  3   5   4]
      ...
      [219 250 255]
      [217 250 255]
      [216 249 254]]
    
     [[216 249 254]
      [215 250 254]
      [216 251 255]
      ...
      [166 201 143]
      [159 182 126]
      [159 193 109]]
    
     [[206 228 156]
      [165 193 145]
      [161 203 183]
      ...
      [ 51 108   0]
      [129 162  73]
      [211 214 185]]
    
     ...
    
     [[  4  22   0]
      [  9  31  10]
      [ 29  78  33]
      ...
      [ 41 163 168]
      [ 59 162 177]
      [ 51 167 166]]
    
     [[ 67 169 174]
      [ 75 166 184]
      [ 67 173 187]
      ...
      [213 216 199]
      [186 186 174]
      [115 113  98]]
    
     [[141 146 124]
      [143 136 120]
      [150 146 135]
      ...
      [  3   5   2]
      [ 32  26  26]
      [ 30  32  21]]]
    
    (255, 255, 3)



### 텐서플로우로 RGB 평균, 분산 구하기

```python
from tensorflow.keras.layers import Input
input_shape = (255, 255, 3)
img_input = Input(shape=input_shape)
mean, var = tf.nn.moments(data, axes=[0,1])
```

`tf.nn.moments(x=???, axes=[])`

x 자리에 어떤 값이 들어가야 하는지 공부가 더 필요하다.

TypeError: data type not understood
라고 에러가 발생했다.



### 넘파이로 평균, 분산 구하기

```python
path = '..\\..\\datasets\\images\\'
img_path = img_paths[:10]
images = []
for f in img_path:
    img = Image.open(path + f)
    resize_img = img.resize((255, 255))
    image = np.asarray(resize_img)
    mean = np.mean(image, axis=(0, 1))
    var = np.var(image, axis=(0, 1))
    print(mean, var)
    image2 = ((image[0, 1] - mean) / var)
```

output: 

데이터 열개를 슬라이싱 했지만 5, 5 동일해서 사실상 두 개의 이미지였다.

    [ 89.13399462 110.94199154  71.80461361] [5155.57000392 5154.66514713 4471.48602254]
    [151.85550173 151.94119185 150.38023837] [5212.37096954 5264.52403103 5199.35661063]

`axis=(0, 1)` 을 넣으면 R, G, B 각각의 값을, `axis=(0, 1, 2)` 는 RGB 를 한번에 계산한다.

이 부분이 이해가 잘 안돼서 아래처럼 간단한 배열로 테스트했다.

#### axis 이해하기

```python
arr = np.array(
    [
        [
            [1, 2, 3],
            [4, 5, 6]
        ],
        [
            [11, 12, 13],
            [14, 15, 16]
        ]
    ]
)

**p**rint(arr.shape)

print('arr.sum(axis=1)')
print(arr.sum(axis=1))
print('arr.sum(axis=0)')
print(arr.sum(axis=0))
print('arr.sum(axis=2)')
print(arr.sum(axis=2))

print('arr.sum(axis=(0, 0))')
print(arr.sum(axis=(0, 1)))
print('arr.mean(axis=(0, 1))')
print(arr.mean(axis=(0, 1)))
```

output:

    (2, 2, 3)
    
    arr.sum(axis=1)
    [[ 5  7  9]
     [25 27 29]]
    
    arr.sum(axis=0)
    [[12 14 16]
     [18 20 22]]
    
    arr.sum(axis=2)
    [[ 6 15]
     [36 45]]
    
    arr.sum(axis=(0, 0))
    [30 34 38]
    
    arr.mean(axis=(0, 1))
    [7.5 8.5 9.5]

손으로 써보니 훨씬 쉽게 이해되었다.

[https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html](https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html)

[http://taewan.kim/post/numpy_sum_axis/](http://taewan.kim/post/numpy_sum_axis/)

[https://datascienceschool.net/view-notebook/464860bf5a5f4e139b05ccc473f1f15c/](https://datascienceschool.net/view-notebook/464860bf5a5f4e139b05ccc473f1f15c/)