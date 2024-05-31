"""가설 내야함 

크다 또는 같다 . 작은건 관심이 없음 같다에 묻어감

유의수준 5프로를 검정 하세요 이렇게 나옴
검정하세요 하면 t분포임 t 테스트

t = (x바 - u) / S/np.sqrt(n)

5장 22번 

첫단계 : 가설정하기
H0 = 3055
H1 = M>3055

자유도 = 41
n = 42

알파 = 0.05

5장 22번 시험임 비슷하게


n은 1031 아님 42가 n 임

H1 = 비싸다 . 

cdf 써야함 

6장 8페이지 

t = x바 - 3055 / S(표준편차)/루트n
"""

import numpy as np
import pandas as pd # 데이터프레임 쓴다는 뜻

from scipy.stats import binom 
import matplotlib.pyplot as plt
from scipy.stats import norm 
plt.rcParams['font.family'] = 'Malgun Gothic'
from scipy.stats import t
from scipy import stats

data = pd.read_excel("C:/Users/kiiti/Downloads/커피가격.xlsx")
mu = 3055
n = 42
print(data.describe())

plt.hist(data, label = 'Coffee Price', bins = 7)
plt.legend()
plt.show()

#손수 한 코드
t = (np.mean(data)-mu)/(np.std(data, ddof=1)/np.sqrt(n))
print(f"t값 : {t}")
p = 1-stats.t.cdf(t, n-1)   # stats 붙인 이유 : from scipy.stats import t 이게 없으면 stats를 쓰고, 있으면 빼도됨
print(f"p값 : {p}")

# 파이썬 메소드 쓰는 코드
result = stats.ttest_1samp(data.coeffee, mu, alternative='greater')
print(result)

if p<0.05:
    print("H0기각")
else :
    print("H0를 기각할 수 없음")

# 비싸지않다.










# 6장 확인문제 1번 시험 이렇게 나옴 

"""
H0 = 6300
H1 = 
"""

data = pd.read_excel("C:/Users/kiiti/Downloads/S기업_점심비용.xlsx")
mu = 6300
n = 100
print(data.describe())

plt.hist(data, label = 'lunch', bins = 7)
plt.legend()
plt.show()

#손수 한 코드
t = (np.mean(data)-mu)/(np.std(data, ddof=1)/np.sqrt(n))
print(f"t값 : {t}")
p = 1-stats.t.cdf(t, n-1)   # stats 붙인 이유 : from scipy.stats import t 이게 없으면 stats를 쓰고, 있으면 빼도됨
print(f"p값 : {p}")

# 파이썬 메소드 쓰는 코드
result = stats.ttest_1samp(data.lunch, mu, alternative='two-sided')
print(result)

if 2*p<0.05:   # 양측이라서 곱하기 2 해야함
    print("H0기각")
else :
    print("H0를 기각할 수 없음") 

# 알파보다 작아야하는데 크니까 기각할 수 없다.













# 6장 2번

data = pd.read_csv("C:/Users/kiiti/Downloads/스마트폰_이용시간.csv", header = None)
mu = 35
n = 40
print(data.describe())

plt.hist(data, label = 'smart phone', bins = 7)
plt.legend()
plt.show()

#손수 한 코드
t = (np.mean(data)-mu)/(np.std(data, ddof=1)/np.sqrt(n))
print(f"t값 : {t}")
p = 1-stats.t.cdf(t, n-1)   # stats 붙인 이유 : from scipy.stats import t 이게 없으면 stats를 쓰고, 있으면 빼도됨
print(f"p값 : {p}")

# 파이썬 메소드 쓰는 코드
result = stats.ttest_1samp(data, mu, alternative='two-sided')
print(result)

if 2*p<0.05:   # 양측이라서 곱하기 2 해야함
    print("H0기각")
else :
    print("H0를 기각할 수 없음") 

#차이가 있는지 << 즉 양측임























data = pd.read_csv("C:/Users/kiiti/Downloads/스마트폰_이용요금.txt", header = None)
mu = 68000
n = 80
# H0 = 68000 홈페이지 입장
# H1 = 6.8만원 이상내고있다 . c군 입장 
print(data.describe())

plt.hist(data, label = 'smart phone', bins = 7)
plt.legend()
plt.show()

#손수 한 코드
t = (np.mean(data)-mu)/(np.std(data, ddof=1)/np.sqrt(n))
print(f"t값 : {t}")
p = 1-stats.t.cdf(t, n-1)   # stats 붙인 이유 : from scipy.stats import t 이게 없으면 stats를 쓰고, 있으면 빼도됨
print(f"p값 : {p}")

# 파이썬 메소드 쓰는 코드
result = stats.ttest_1samp(data, mu, alternative='greater')
print(result)

if p<0.05:   
    print("H0기각")
else :
    print("H0를 기각할 수 없음") 
    
# p = 0.1737 , 알파 = 0.05
# 즉 p>알파라서 기각 x