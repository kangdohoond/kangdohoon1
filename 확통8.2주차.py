import numpy as np
import pandas as pd # 데이터프레임 쓴다는 뜻

from scipy.stats import binom 
import matplotlib.pyplot as plt
from scipy.stats import norm 
plt.rcParams['font.family'] = 'Malgun Gothic'

# 질문 : 분포랑 정규분포랑 차이가 뭔지

# Z 점수 : -3 <= Z <= 3     
# T 점수 : 10 * Z + 50   : 즉 : 20 <= Z <= 80

# 표준정규분포 전체의 면적(확률)(넓이)은 1  # 42페이지
# 표준정규분포 절반의 면적(확률)은 0.5  , 문제: P(z>=0.7)을 40페이지 표로 알아내봐라
# -> 1 - (Z>=0.7)     -> 1-0.758 = 0.24xxxx 
# 문제 : P(-0.4 <= Z <= 1.3) :
# 풀이 : p(Z<=1.3) - p(Z<=-0.4), 
# P(Z<=1.3) - P(Z >= 0.4) , P(Z<=1.3) - (1-P(Z<=0.4)), 정답 : 1.3 이니까 0.90320 - (1-0.6642) = 0.55xxxx


# pdf 는 그냥 y 값을 알려주는 거임   

# 문제 : -1.5 ~ 0.5 넓이? 구하기
#         P(Z<=0.5) - P(Z <= -1.5)
        # P(Z<=0.5) - P(Z >= 1.5)
        # P(Z<=0.5) - (1 - P (Z<=1.5))   # 이 3줄이 하나의 식인지? 안그럼 3개가 다 다른 식인건지?



# x 축에 있는 값을 구해주는 것 : ppf

# 1.28 ~ 1.29 


print(norm.ppf(0.9,0,1))   # ,평균, 표준편차 


# pdf : x가 뭐일때 y가 뭐를 구하는 것
# cdf : 뭔가 주어졌을 때 면적 구하는 것
# ppf : 면적이 주어졌을 때 x 값 구하는 것  : 즉 : cdf랑 ppf랑 역함수 관계임

# 8번 

m = 7
s = 15
x = np.arange(m-50, m+50, 0.1)
y = norm.pdf(x,m,s)

plt.bar(x,y)
plt.show()

# 8번의 2번
m = 175
s = 20
x = np.arange(m-50, m+50, 0.1)
y = norm.pdf(x,m,s)

plt.bar(x,y)
plt.show()


m = 0 
s = 1
print(norm.ppf(0.975,m,s))





