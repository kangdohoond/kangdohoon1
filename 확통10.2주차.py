import numpy as np
import pandas as pd # 데이터프레임 쓴다는 뜻

from scipy.stats import binom 
import matplotlib.pyplot as plt
from scipy.stats import norm 
plt.rcParams['font.family'] = 'Malgun Gothic'
from scipy.stats import t

"""
퀴즈1번

95%구간 68.2~72.7 이렇게 구간추정을 할 때 이 의미는 ?

1. 95%의 학생들이 위 범위에 들어간다.
2. 모집단의 평균이 위 구간에 들어갈 확률이 95%이다.

정답은 2번


///////////

구간찾아봐라
모집단(모수) 표준편차(시그마)가 적혀있으면 정규분포

표본 표준편차 (S)

시그마가 없으면(S가 있으면) 
n이 대충 30 이상이면 정규분포 아니면 t분포



퀴즈2번

표준편차와 표준오차(sem)의 차이를 말해보세요.

표준편차 : 루트(분산)
여기서 분산은 그냥 분산일 수도 있고 불편분산일 수도 있다.

5.2장에서는 불편분산을 사용한다.
즉, 기술통계 말고 추측통계 할 때는 불편분산을 사용함.

지금 우리는 모평균을 추정하고 있다.
즉, 추즉통계.
따라서 구간추정할 때는 무조건 불편분산 ddof=1

표준오차 : 표준편차 / 루트n 
구간추정에서는 표준오차 sem을 사용

5.2장 12페이지 보면

왼쪽그림의 시그마^2/n 이게 표본분산 

표준편차: 시그마 / 루트n    << 즉 이게 표준오차임 

13페이지 분모가 표준오차임
13페이지 마지막줄 +-1.96 적혀있는 공식 외우면 좋음

95% 일 때 1.96인 이유는 Z 위치임

15페이지

100명 = n 
58만명 = x바
10만원 = 시그마
95% = 1.96





"""

# 확인문제 14번 
# 혹시나 1.96이 기억이 안난다면 구하는 방법 : print(norm.ppf(0.95,0,1))
n = 50
mean = 70.4
#불편분산임
s = 6
sem = s/ np.sqrt(n)

zu = norm.ppf(0.975,0,1)

print(zu)

print(f"하한 : {mean-zu*sem}")
print(f"상한 : {mean+zu*sem}")

print(norm.interval(0.95, loc=mean, scale=sem)) # 상한 하한 바로 나오는 메소드


# 99% 할거면 0.975 대신 0.995 넣어ㅑ함


n = 50
mean = 70.4
#불편분산임 << why?
s = 6
sem = s/ np.sqrt(n)

zu = norm.ppf(0.995,0,1)
# zu = t.ppf(0.995, df = 자유도)
print()
print(zu) 
print(f"하한 : {mean-zu*sem}")
print(f"상한 : {mean+zu*sem}")

print(f"정규분포 : {norm.interval(0.99, loc=mean, scale=sem)}") # 상한 하한 바로 나오는 메소드
print(f"t분포 : {t.interval(0.99, 49, loc=mean, scale=sem)}") # 49는 자유도임 -> 50 - 1 

# 어느경우에서도 95%보다 99% 신뢰구간이 더 넓다? yes <<<<<<< 중요함 

# 16페이지 알파/2 저건 걍 1.96이라는 뜻
# 즉 17페이지에 알파가 0.05니까 0.025
# 자유도 9일 때

print(t.ppf(0.025,df=9))
print(t.ppf(0.975,df=9))   # 이건 그냥 바로 위에 코드에 - 붙이면 같은 답임

# 19페이지문제
# 시그마가 없으니까 

# n = 10
# mean = 262.7

#var = ((260-262.7)**2 + (265-262.7) **2 ~~~~ ) / n-1
print()
a = [260,265,250,270,272,258,262,268,270,252]
n = len(a)

print(f"평균 : {np.mean(a)}")
print(f"분산 : {np.var(a)}")
print(f"불편분산 : {np.var(a, ddof=1)}")

# 시간없어서 다 못적음 ppt에 있음

# 15번 16번 과제
# 15번 t분포
n = 25
mean = 35
s = 5
print(t.)

# 확인문제 17번

"""
n=10 n=50 표본의 크기가 커지면 신뢰구간은 좁혀짐

정답 : 2번임

"""










