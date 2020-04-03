# SubPJT2

이미지 캡셔닝 구현

## 이미지 캡셔닝 이란?

인공지능 컴퓨터 비전의 분야 중 하나이다. 컴퓨터가 사진을 보고 적절한 설명을 자동으로 붙이는 것, 이미지를 묘사하는 문장을 생성하는 것을 의미한다.

이미지로 입력input 하고 문장으로 output 하는 형태이다.

이미지의 특성을 뽑아내는 데에는 컨볼루션 신경망(CNN, Convolutional Neural Networks)를, 특성을 바탕으로 문장을 생상하는 부분은 순환 신경망(Recurrent Neural Networks)를 사용한다.



## 데이터 처리

### 데이터 정규화 Data Normalization

왜 정규화가 필요한가?

- 신경망 학습 속도를 높이기 위해

- Local optimum 에 빠질 가능성을 줄이기 위해

  비슷한 범위를 가질 때 경사하강법으로 Global optimum 을 찾기 더 쉬워진다.

  ![Untitled.png](C:/Users/multicampus/SSAFY/A405/subPJT2/doc/솔지/README/Untitled.png)

이미지 데이터는 0~255 픽셀 정보를 가지므로, 
데이터를 255로 나누면 0~1.0 사이의 값을 가질 수 있다.

**(정규화하고자 하는 값 - 데이터 최소값) / (데이터 최대값 - 데이터 최소값)**

또는

**(정규화하고자 하는 값 - 데이터의 평균) / 데이터의 표준편차**

로 표현할 수 있다.

```python
# 텐서플로우로 평균 0과 분산 1을 갖도록 각 이미지의 크기를 선형으로 조정하기
tf.image.per_image_standardization(
    image
)
```

[https://lsjsj92.tistory.com/387](https://lsjsj92.tistory.com/387)
[https://www.tensorflow.org/tutorials/load_data/images](https://www.tensorflow.org/tutorials/load_data/images)
[https://goodtogreate.tistory.com/entry/Neural-Network-적용-전에-Input-data를-Normalize-해야-하는-이유](https://goodtogreate.tistory.com/entry/Neural-Network-적용-전에-Input-data를-Normalize-해야-하는-이유)



### 데이터 어그멘테이션 Data Augmentaion

Image Augmentation 은 원본 이미지에 변화를 줘서 데이터를 부풀리는 것을 말한다.

- 데이터를 부풀려서 성능을 높인다.

  딥러닝의 overfitting 문제를 해결하기 위해

- 데이터 학습 범위를 넓힌다.

이미지를 좌우반전 하거나, 자르거나, 밝기를 조절하는 등 다양한 응용법이 있다.

Keras 의 `ImageDataGenerator` 를 사용해서 구현할 수 있다.

`width_shift_range`, `horizontal_flip`, .. 다양한 값을 줄 수 있다.

[https://machinelearningmastery.com/how-to-configure-image-data-augmentation-when-training-deep-learning-neural-networks/](https://machinelearningmastery.com/how-to-configure-image-data-augmentation-when-training-deep-learning-neural-networks/)
[http://blog.naver.com/PostView.nhn?blogId=4u_olion&logNo=221437862590&parentCategoryNo=&categoryNo=45&viewDate=&isShowPopularPosts=true&from=search](http://blog.naver.com/PostView.nhn?blogId=4u_olion&logNo=221437862590&parentCategoryNo=&categoryNo=45&viewDate=&isShowPopularPosts=true&from=search)
[https://nittaku.tistory.com/272](https://nittaku.tistory.com/272)



### 차이점

정규화와 어그멘테이션 모두 학습 성능을 높이기 위한 방법이지만, 

- 정규화는 모델링 수정이다.

  모든 데이터에 일관되게 적용되어야 한다.

- 어그멘테이션은 의미 그대로 데이터 기능 보강이다.

  훈련 데이터세트에만 적용하고, 검증과 테스트 데이터에는 적용하지 않는다.



## 합성곱 신경망(CNN, Convolutinal Neural Network)

CNN 은 데이터의 특징Feature 를 추출하는 역할을 한다.

이미지에서 물체의 형태를 인지하거나 색깔을 구별하는 등 특성을 뽑아낼 것이다.

컨볼루셔널 레이어는 필터Filter 와, 필터의 값을 비선형으로 바꾸어 주는 활성화Activation 함수(ReLU 같은)로 이루어진다.



### 필터Filter

이미지의 특징을 찾아내기 위한 공용 파라미터이다. 입력 데이터를 지정된 간격으로 순회하며 채널별로 합성곱을 하고, 모든 채널(컬러는 3개)의 합성곱의 합을 Feature Map 으로 만든다.

**stride** 는 필터가 이동하는 간격이다.

7x7 이미지를 3x3, stride 1 필터로 순회하면 5x5 피처 맵을 반환한다.
stride 가 2라면 아웃풋은 3x3 피처 맵이 될 것이다.

**피처 맵의 크기 == (N - F) / stride + 1**

위의 식을 따르면 아웃풋은 입력 데이터보다 작다. 즉, 어떤 정보를 잃어버린다는 문제가 발생한다.

그래서 사용하는 개념이 **패딩Padding** 이다.

지정된 픽셀만큼 특정 값으로 가상의 벽을 두른다.

패딩을 사용하는 목적은

- 데이터가 작아지는 것을 방지하기 위해

- 모서리 부분을 나타내기 위해

라고 볼 수 있다.

7x7 에 1 의 패딩을 두르면 9x9 가 되고 7x7 의 아웃풋을 얻을 수 있다.

입력과 출력 사이즈가 같아지게 만드는 것이 일반적이다.

이런 과정을 채널 수만큼 반복했을 때 예로 32x32x3 이미지에 패딩 없이 6개의 필터를 사용한다고 가정하면 (28, 28, 6) 의 결과를 얻을 수 있을 것이다.



### 풀링Pooling

풀링은 샘플링이라고 볼 수 있다.

컨볼루션 레이어에서 한 레이어만 뽑아내서 resize(sampling) 한다.

Max Pooling 은 가장 큰 값을 가져오는(==샘플링하는) 방법이다.

최종 아웃풋을 완전 연결 계층Fully Connected Layer에 넣어서 결과를 얻을 수 있다.
(fully connected layer 는 앞에서 뽑아낸 특징들을 판단하는 역할을 한다.)



[https://bcho.tistory.com/1149?category=555440](https://bcho.tistory.com/1149?category=555440)
[http://taewan.kim/post/cnn/#1-3-필터-filter-stride](http://taewan.kim/post/cnn/#1-3-%ED%95%84%ED%84%B0-filter-stride)
[https://youtu.be/Em63mknbtWo](https://youtu.be/Em63mknbtWo)
[https://youtu.be/2-75C-yZaoA](https://youtu.be/2-75C-yZaoA)



### CNN 모델 학습

#### Inception(GoogLeNet)

딥러닝 학습에서 망이 깊고 레이어가 높을 수록 성능은 좋아지지만, 연산량이 많고 과적합 등의 문제로 학습이 힘들어진다.

- CNN 의 연산량

  Weight, Bias 말고도 노드 개수, 레이어 깊이 등의 하이퍼파라미터

  연산을 거칠 때마다 채널이 커지고, 필터의 크기도 하이퍼파라미터가 되어 필터 크기에 따라 연산량이 많아진다.

  stride 와 padding 값 역시 하이퍼파라미터이므로 레이어가 많아지면 연산이 많아진다.

  풀링 과정에서도 필터와 stride 등등.. Hyper Param 값들이 많다.

이를 해결하기 위한 방안 중 하나가 Sparse Connectivity 이다. 컨볼루션 연산은 굉장히 Dense하게... 빽빽하게 연결되어 있는데 이를 높은 관련성을 가진 노드끼리만 연결하도록 바꾸는 것이다.

실제로는 Dense matrix 연산보다 Sparse Matrix 연산이 더 큰 리소스를 필요로 한다. Dense matrix 연산은 기술이 많이 발전하면서 더 효율적이 되었다.

Inception 은 Feature Map 을 추출하는 과정에서 Sparse 한 방식으로 노드 간의 연결은 줄이면서 행렬 연산은 Dense 하게 하도록 처리한 것이다.

Inception Module 의 연산

1. 1x1 convolution
2. 1x1 convolution + 3x3 convolution
3. 1x1 convolution + 5x5 convolution
4. 3x3 MaxPooling + 1x1 convolution

이 네 가지의 연산 결과를 Channel-wise 한다.

1x1 convolution 은 채널 수를 조절하고 줄이는 역할을 한다. 채널을 줄여서 파라미터 개수도 절약할 수 있다.

https://datascienceschool.net/view-notebook/8d34d65bcced42ef84996b5d56321ba9/

https://ikkison.tistory.com/86