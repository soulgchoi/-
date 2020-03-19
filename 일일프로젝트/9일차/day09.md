# 9일차 얼굴인식

Created: Mar 19, 2020 3:05 PM

# Google Colab 기반의 얼굴인식 프로젝트

## Colab 사용

### Google Colab(Cloaboratory)

Jupyter Notebook 처럼 웹 브라우저에서 코드를 작성하고 실행할 수 있다. Colab 은 Jupyter Notebook 에 추가로 Python 소스코드를 Google 클라우드 컴퓨팅 환경에서 GPU와 TPU 를 무료로 사용할 수 있고, 소스코드나 데이터를 Google Drive 에서 불러오고 저장할 수 있다. 

클라우드 기반으로 딥러닝, 머신러닝, 데이터 사이언스 분야에서 많이 사용한다.

## 얼굴인식

### 사용한 라이브러리

**OpenCV**

컴퓨터 비전 라이브러리 중 하나로, 실시간 이미지 프로세싱에 중점을 둔 라이브러리이다. 영상처리에 많이 사용한다.

**Numpy**

행렬이나 일반적으로 대규모 다차원 배열을 쉽게 처리 할 수 있도록 지원하는 파이썬의 라이브러리이다. NumPy는 데이터 구조 외에도 수치 계산을 위해 효율적으로 구현된 기능을 제공한다.

**Matplotlib**

그래프 표시 라이브러리이다.

**face-recognition 1.3.0**

Dlib 기반의 얼굴감지, 인식 패키지이다.

### Face Detection

```python
import cv2, os
import face_recognition as fr
from IPython.display import Image, display
from matplotlib import pyplot as plt

image_path = '사용할 이미지 위치'
face_locations = fr.face_locations(image)

for (top, right, bottom, left) in face_locations:
	cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 3)

plt.reParams['figure.figsize'] = (16, 16)
plt.imshow(image)
plt.show()
```

### Face Recognition

앞서 `face_locations()` 함수를 사용해 사진에서 얼굴을 찾았다. face_recognition 은 이 얼굴영역을 encoding 한 후 encoding 된 데이터로 face_distance() 를 구해 동일인인지 판별할 수 있다.

```python
import cv2, os
import face_recognition as fr
from IPython.display import Image, display
from matplotlib import pyplot as plt

plt.rcParams['figure.figsize'] = (1, 1)

known_person_list = [] 
known.person_list.append(fr.load_image_file('이미지 위치')
# list 에 이미지 파일들을 넣는다.

known_face_list = []
for person in known_person_list:
	# 얼굴좌표를 잘라낸다.
	top, right, bottom, left = fr.face_locations(person)[0]
	face_image = person[top:bottom, left:right]
	# known_face_list 에 잘라낸 face_image 를 저장한다.
	known_face_list.append(face_image)

# 얼굴들을 출력해서 볼 수 있다.
for face in known_face_list:
	plt.imchow(face)
	plt.show()
                         
# 비교할 얼굴 이미지를 가져온다.
unknown_person = fr.load_image_file('이미지 위치')

# 얼굴좌표를 잘라낸다.
	top, right, bottom, left = fr.face_locations(person)[0]
	unknown_face = unknown_person[top:bottom, left:right]

# 타이틀을 붙여 출력한다.
plt.title('unknown_face')
plt.imshow(unknown_face)
plt.show()


#
# 얼굴영역을 인코딩한다.
enc_unknown_face = fr.face_encodings(unknown_face)

# 다른 얼굴 리스트와 비교한다.
for face in known_face_list:
	# 등록된 얼굴들을 인코딩한다.
	enc_known_face = fr.face_encodings(face)
	
	# 등록된 얼구로가 새로운 얼굴의 distance 계산
	distance = fr.face_distance(enc_known_face, enc_unknown_face[0])

	# distance 수치로 동일인 여부를 판별할 수 있다.
	plt.title('distance: ' + str(distance))
	plt.imshow(face)
	plt.show()
```

distance 가 0.5 아래이면 동일인, 0.5 이상은 타인으로 볼 수 있다. (0.6 을 기준으로 하기엔 내가 비교한 이미지에서는 모두 0.5 대가 나왔다.)
