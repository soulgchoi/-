# DB 프로젝트

Created: Mar 09, 2020 9:27 PM

# DB 프로젝트 - 관계형 데이터베이스

## 산출물 내역

1. 주어진 테이블을 분할한 ERD_DIAGRAM
2. 데이터 출력

## ERD_DIAGRAM

### 데이터베이스 설계

👩 student

​	기수(curriculum) 과 지역(region), 반(group) 은 별도의 테이블을 만들어 외래키로 갖는다.

​	지역별, 기수별 조회를 용이하게 한다.

​	프로젝트 별 팀은 student_team 테이블을 만들어 학생과 팀이 N:M 관계가 되도록 한다.

🙋‍♂️ attendance

​	처음에는 student, attendance 외래키를 갖는 student_attendance 테이블을 만들 생각이었으나... 날짜별로 구분하기 쉽지 않아 attendance 테이블에 학생별 날짜, 입퇴실 시간을 함께 넣었다.

👩‍💻 algorithm 

​	알고리즘 취득 성적을 갱신이 아닌 추가 개념으로 보고 student 와 1:N 관계로 설정했다.
​	한 명의 학생이 여러 개의 성적을 취득할 수 있기 때문이다.

🤦‍♀️ exam

​	exam 테이블에서 시험을 분류하고, 

​	examgrade 테이블을 거쳐 student 와 exam 이 N:M 관계가 되게 한다.

📌 [https://multifrontgarden.tistory.com/181](https://multifrontgarden.tistory.com/181) 이 페이지를 참고했다.

![1%20_DB/day1_1.jpg](1%20_DB/day1_1.jpg)

​	이렇게 그릴 수 있지만,

![1%20_DB/day1_2.jpg](1%20_DB/day1_2.jpg)

위의 형태가 더 보편적이라 하여 이를 따랐다.

👨‍👧‍👧👨‍👧‍👧  group

​	한 지역 안에 여러개의 반이 있으므로 region 과 group 은 1:N 이다.
​	한 명의 프로가 여러 반을 담당하므로, 👩‍🏫teacher 와 group 역시 1:N 이다.

​	한 반에는 여러 명의 학생이 있을 수 있으므로 group 과 student 가 1:N 관계가 된다.

👬 team

​	여러 개의 프로젝트를 진행하며 각각 팀이 나뉘므로, project 와 team 은 1:N 관계이다. 

​	한 학생이 여러 번 팀에 속하고, 하나의 팀은 여러 명의 학생이 속하므로 student_team 테이블을 경유하여 N:M 관계가 된다.

⚡ project

​	exam 과 동일하게 grade 테이블을 구성한다.

### 산출물

![1%20_DB/day1_3.png](1%20_DB/day1_3.png)



## 데이터 출력 예시

### 각 일자별 빠진 교육생 자료 출력

​	attendance 테이블에서 해당 날짜에 student_id 가 있는지 판단하여 출력한다.

​	아래는 2020-01-01 을 기준으로 한 예시이다.

```sql
SELECT student_id, `name` FROM db.student
WHERE student_id NOT IN (
	SELECT DISTINCT student_id FROM db.attendance WHERE DATE='2020-01-01'
);
```

출력 결과는 다음과 같다.

![1%20_DB/day1_4.jpg](1%20_DB/day1_4.jpg)

### 각 기수별, 지역별, 팀별 상위 알고리즘(A+이상) 인원 수

```sql
SELECT COUNT(student_id) FROM db.`algorithm` 
WHERE (grade='A+' OR grade='B')
AND student_id IN (
	기수, 지역, 팀 등 다른 조건을 여기에 건다.
)
```

- 기수별 (예시는 2기)

    ```sql
    SELECT COUNT(student_id) FROM db.`algorithm` 
    WHERE (grade='A+' OR grade='B')
    AND student_id IN (
    	SELECT DISTINCT student_id FROM db.student WHERE curriculum_id='2'
    )
    ```

    출력결과

    ![1%20_DB/day1_5.jpg](1%20_DB/day1_5.jpg)

- 지역별 (예시는 서울)

    ```sql
    SELECT COUNT(student_id) FROM db.`algorithm` 
    WHERE (grade='A+' OR grade='B')
    AND student_id IN (
    	SELECT DISTINCT student_id FROM db.student WHERE region_id='1'
    )
    ```

    출력결과

    ![1%20_DB/day1_6.jpg](1%20_DB/day1_6.jpg)

- 팀별 (예시는 프로젝트 1의 1팀이다.)

    ```sql
    SELECT COUNT(student_id) FROM db.`algorithm` 
    WHERE (grade='A+' OR grade='B')
    AND student_id IN (
    	SELECT DISTINCT student_id FROM db.student_team WHERE team_id='1'
)
    ```

    출력결과
    
    ![1%20_DB/day1_7.jpg](1%20_DB/day1_7.jpg)

