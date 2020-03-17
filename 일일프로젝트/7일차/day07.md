# 7일차 Collection

Created: Mar 17, 2020 10:03 AM

# Collection 사용하기

## Collection

### Collection 이란?

Stack, Queue, Array, List, Hash, Dictionary, ... 

### 언제 Collection 을 쓸까?

동일한 속성의 데이터들을 반복적으로 비교 연산

비교 연산 후 결정되는 동작이 비슷한 패턴으로 반복

### Collection 사용에 고려할 것

collection 을 만들기 위한 CPU/메모리 비용

가독성, 메모리, 씨피유 사용량 등 종합적으로 고려하여 적절하게 사용

collection 을 초기에 한 번 만들고, 사용을 여러 번 할 경우, 성능이 크게 개선

## 문제

    import datetime
    
    
    def getDays(year, month):
    
        if month == 1:
            return 31
        elif month == 3:
            return 31
        elif month == 5:
            return 31
        elif month == 7:
            return 31
        elif month == 8:
            return 31
        elif month == 10:
            return 31
        elif month == 12:
            return 31
        elif month == 4:
            return 30
        elif month == 6:
            return 30
        elif month == 9:
            return 30
        elif month == 11:
            return 30
        elif month == 2:
            if((year % 4) == 0) and ((year % 100) != 0) or ((year % 400 ) == 0):
                return 29
            else:
                return 28
    
    dt = datetime.datetime.today()
    
    print(getDays(dt.year, dt.month))

위의 코드를 Collection 을 사용해 아래처럼 바꿨다.

    import datetime
    
    def getDays(year, month):
        days = {
            '31': [1, 3, 5, 7, 8, 10, 12],
            '30': [4, 6, 9, 11],
        }
    		# 30, 31 일 출력이 반복되므로 dictionary 로 간결하게 만들었다.	
    
        for key, val in days.items():
            if month in val:
                return key
            else:
                if((year % 4) == 0) and ((year % 100) != 0) or ((year % 400 ) == 0):
                    return 29
                else:
                    return 28
    						# 윤년은 if 문으로 따로 계산하기 위해 그대로 두었다.
    
    dt = datetime.datetime.today()
    
    print(getDays(dt.year, dt.month))