import numpy as np
import pandas as pd # 데이터프레임 쓴다는 뜻

from scipy.stats import binom 
import matplotlib.pyplot as plt
from scipy.stats import norm 
plt.rcParams['font.family'] = 'Malgun Gothic'
from scipy.stats import t
from scipy import stats

"""
독립인 두 표본에 대한 t 검정

이때 모집단은 스마트폰을 이용하는 남성 전체와 스마트폰을 이용하는 여성 전체이므로 두 개이며 서로 독립적인 표본이다.

독립인 두 표본에 대한 t검정에 사용하는 함수는 ttest.ind()

두 집단이 분산이 같다고 가정한다 . 이러면 등분산
구해봐라~ 하고 다르면 이분산 , 이분산이라면 equal_var = False 넣어야함 
"""

data = pd.read_excel("C:/Users/kiiti/Downloads/6.2/성인_스마트폰_이용시간.xlsx") # 컬럼명이 없으면 header = None 이거 시험
print(data.describe()) # 25 50 75 % 이렇게 나오는 거 사분위수 라고 함
# 50%를 중앙값이라고 함 


data.boxplot(column=['male', 'female'], vert=False) # False는 가로라는 뜻 True는 세로라는 뜻
# 상자도형 (두개 비교할 때 편함)
plt.show()

data1 = pd.read_excel("C:/Users/kiiti/Downloads/6.2/성인_스마트폰_이용시간_남자.xlsx")
data2 = pd.read_excel("C:/Users/kiiti/Downloads/6.2/성인_스마트폰_이용시간_여자.xlsx")

result = stats.ttest_ind(data1.male, data2.female, alternative = 'two-sided') # 분산이 같다고 가정된 거임
print(result)
# 0.00034 니까 0.05보다 작음 
# 즉 0.00034 < 0.05 
# H0 기각  , 패배


data = pd.read_excel("C:/Users/kiiti/Downloads/6.2/대학생_수면시간.xlsx")
print(data.describe())

data.boxplot(column=['male', 'female'], vert = False)
plt.show()
data1 = pd.read_excel("C:/Users/kiiti/Downloads/6.2/대학생_수면시간_남자.xlsx")
data2 = pd.read_excel("C:/Users/kiiti/Downloads/6.2/대학생_수면시간_여자.xlsx")

result = stats.ttest_ind(data1.male, data2.female, alternative = 'two-sided', equal_var = False)
print(result)




# 등분산인지 이분산인지 헷갈리는 거 
# std = 2.912     ,    3.2xxxx

# 무조건 이분산인 거 
# 1.8xxxxx ,   0.9 xxxx




"""
levene 를 사용해서 등분산인지 이분산인지 결정

"""
re = stats.levene(data1.male, data2.female, center = 'mean')
print(re)

# 질문 : 만약 이분산이라고 가정하면, levene에서 나온 p 값이랑 ttest_ind(~~~~~ , equal = False)랑 p값이 같은지? 다름 
"""
ttest_ind 랑 + from_stats 차이는 전자는 원본 데이터 있을 때 
후자는 딱 데이터가 정해져있을 때 
"""
# 여기까지는 전부 독립 표본 



















