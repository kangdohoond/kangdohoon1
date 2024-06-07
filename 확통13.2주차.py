import numpy as np
import pandas as pd # 데이터프레임 쓴다는 뜻

from scipy.stats import binom 
import matplotlib.pyplot as plt
from scipy.stats import norm 
plt.rcParams['font.family'] = 'Malgun Gothic'
from scipy.stats import t
from scipy import stats


# 4장 15번 

# z = ( 95 - 70 ) / 10 = 2.5

# 1 - 0.994 = 0.006
# 1500 * 0.006 = 9



"""
대응 표본
rel 은 등분산 이분산이 없음 


"""

data = pd.read_excel("C:/Users/kiiti/Downloads/피트니스_결과.xlsx")
print(data[['before', 'after']].describe()) # 그냥 data.디스크라이브 해도됨 

data.boxplot(column =['before', 'after'], vert=False)
plt.show()

result = stats.ttest_rel(data.before, data.after, alternative = 'greater') # greater 이라는 말은 비포>에프터 라는 뜻 에프터를 먼저 쓴다면 less를 적어야함
print(result)


# 6장 4번 

# 일단 개수가 다르니까 따로따로 해야함

data1 = pd.read_excel("C:/Users/kiiti/Downloads/배터리,근로,성적,체중/배터리_지속시간_china.xlsx")
data2 = pd.read_excel("C:/Users/kiiti/Downloads/배터리,근로,성적,체중/배터리_지속시간_korea.xlsx")

result1 = stats.levene(data1.china, data2.korea, center = 'mean')
print(result1) # 0.05보다 작으므로 H0기각, 이분산임

# 독립임 즉 ind 써야함 

data = pd.read_excel("C:/Users/kiiti/Downloads/배터리,근로,성적,체중\배터리_지속시간.xlsx")
print(data.describe())

data.boxplot(column = ['china', 'korea'], vert=False)
plt.show()

data1 = pd.read_excel("C:/Users/kiiti/Downloads/배터리,근로,성적,체중/배터리_지속시간_china.xlsx")
data2 = pd.read_excel("C:/Users/kiiti/Downloads/배터리,근로,성적,체중/배터리_지속시간_korea.xlsx")

result = stats.ttest_ind(data1.china, data2.korea, alternative = 'two-sided', equal_var= False)
print(result)


# 6장 5번 

# 양측임 
#양쪽 다 100명이라 따로따로 할 필요없음
data = pd.read_excel("C:/Users/kiiti/Downloads/배터리,근로,성적,체중/주당_근로시간.xlsx")
result = stats.levene(data.daejeon, data.gwangju, center='mean')
print(result) # 기각 , 이분산 


print(data.describe())

data.boxplot(column = ['daejeon', 'gwangju'], vert=False)
plt.show()


result = stats.ttest_ind(data.daejeon, data.gwangju, alternative = 'greater', equal_var= False)
print(result) # H0 기각 , 즉 두 지역의 근로시간 차이가 있다.




# 6장 6번 
# 대응임 rel , 단측
# 왜 levene 안 하는지 ? rel 이라서 그런가?
data = pd.read_excel("C:/Users/kiiti/Downloads/배터리,근로,성적,체중/확률및통계_성적.xlsx")
print(data[['midterm', 'final']].describe())

data.boxplot(column = ['midterm', 'final'], vert = False)
plt.show()

result = stats.ttest_rel(data.midterm, data.final, alternative = 'less')
print(result)

# 7번 

# 단측 , 

data = pd.read_excel("C:/Users/kiiti/Downloads/배터리,근로,성적,체중\체중비교.xlsx")
print(data[['before', 'after']].describe())


#체중이 줄어든 거니까 비포를 먼저쓰고 그레이터 써야함
data.boxplot(column = ['before', 'after'], vert = False)
plt.show()

result = stats.ttest_rel(data.before, data.after, alternative = 'less')
print(result) # 체중이 줄어들었다 동호회 갈만하다 