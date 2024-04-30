# pmf : 합이 1
# [a,b,c,d,e]


# 누적분포함수 : cdf = 마지막이 1임
# binom.cdf(x,n,p)
# [a , a+b, a+b+c, a+b+c+d, a+b+c+d+e]


# 누적분포함수의 역함수 : ppf = cdf랑 다르게 x를 안 넣고 확률을 넣음
# 즉 cdf 의 역함수 : ppf
# binom.ppf(q,n,p)


import numpy as np
import pandas as pd # 데이터프레임 쓴다는 뜻

from scipy.stats import binom 
import matplotlib.pyplot as plt
from scipy.stats import norm 
plt.rcParams['font.family'] = 'Malgun Gothic'

n = 50
p = 0.5
q = 0.9

k = binom.ppf(q,n,p)

print("k = ", k)


print("P(X<=29)",binom.cdf(29,n,p))
print("P(X<=30)",binom.cdf(30,n,p))
print("P(X<=31)",binom.cdf(31,n,p)) # 질문 : 왜 29가 아니라 30인가 


# 정규분포 : 중요함 별 5개

# 정규분포 : "연속"확률분포 중에서 가장 많이 활용되는 분포임 , 종 모양
# 정규분포 수식을 외우라고 하진 않음
# 평균하고 표준편차가 중요함 이 2개를 이용해서 구함.

# 그래프 위치는 평균이 결정
# 그래프가 넓적한지 길쭊한지는 표준편차가 결정

# 평균 = 중앙값 = 최빈값
# 정규분포 그래프 넓이는 무조건 1 , 음수로 갈 수 없음.


# 33페이지 1번 넓적한 거 분산이 큼 # 분산이 큰 건지 표준편차가 큰 건지?
# 33페이지 2번 평균이 큼 


# pdf = 확률밀도함수
# norm.pdf 

m = 50
s = 5

x = np.arange(m-30,m+30,0.1)
y = norm.pdf(x,m,s)

plt.bar(x,y)
plt.show()

##################################


m = 53
s = 20

x = np.arange(m-53,m+47, 0.1)
y = norm.pdf(x,m,s)

plt.bar(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("수학 A영역(m=53, s=20)")
plt.show()

# #################################

m = 57
s = 15

x = np.arange(m-53,m+47, 0.1)
y = norm.pdf(x,m,s)

plt.bar(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("수학 B영역(m=57, s=15)")
plt.show()



# 몽땅 똑같은 모양으로 만들어주는 것 : 정규분포의 표준화
# 표준화 : Z
# Z = X - 평균 / 표준편차(시그마)
# 표준정규분포 : 평균 0 , 표준편차 1로 통일

# 표준정규분포를 사용하면 한 번에 비교가능

# 38페이지 수학이 더 순위높음

# 44페이지 ? 1.28 페이지
# 1.2 행 0.8열 -> 0.3997 
# 0.3997 + 0.5 = 0.8997 -> 상위 10.003
# 0.5는 그래프의 반절 
