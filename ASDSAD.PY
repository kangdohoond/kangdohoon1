import numpy as np
import pandas as pd # 데이터프레임 쓴다는 뜻

from scipy.stats import binom 
import matplotlib.pyplot as plt
from scipy.stats import norm 
plt.rcParams['font.family'] = 'Malgun Gothic'
from scipy.stats import t
from scipy import stats

data = pd.read_excel("C:/Users/kiiti/Downloads/배터리,근로,성적,체중/주당_근로시간.xlsx")
result = stats.levene(data.daejeon, data.gwangju, center='mean')
print(result) # 기각 , 이분산 


print(data.describe())

data.boxplot(column = ['daejeon', 'gwangju'], vert=False)
plt.show()


result = stats.ttest_ind(data.daejeon, data.gwangju, alternative = 'greater', equal_var= False)
print(result) # H0 기각 , 즉 두 지역의 근로시간 차이가 있다.
