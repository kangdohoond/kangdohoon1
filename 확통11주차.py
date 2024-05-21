import numpy as np
import pandas as pd # 데이터프레임 쓴다는 뜻

from scipy.stats import binom 
import matplotlib.pyplot as plt
from scipy.stats import norm 
plt.rcParams['font.family'] = 'Malgun Gothic'
from scipy.stats import t

n = 30
trial = 1000
# 데이터를 읽어오는 라인
data = np.loadtxt("C:/Users/kiiti/Downloads/data30000.txt") # 3만개짜리 1차원배열
print(data[0])


#우리가 원하는건 2차원배열 


#1000행 30열 이차원 배열로 바꾸는 라인
# data.reshape(1000,30) 
# print(data[0])


x = np.zeros(trial)
for i in range(trial):
    x[i] = np.mean(data[i])

# 19번
print(f"표본평균의 최소 최대 : {np.min(x)}{np.max(x)}")
print(f"중앙값 :  {np.median(x)}")
print(f"표본평균들의 평균을 모평균으로 추정 : {np.mean(x)}")
print(f"표본평균들의 표준편차 * 루트n : {np.std(x,ddof=1)*np.sqrt(n)}")

# 19.2번
y= norm.pdf(x,np.mean(x),np.std(x)) # 확률밀도함수 구할 땐 그냥 표준편차 써도됨 불편 ㄴ 
plt.bar(x,y)
plt.show()

# 19.3번
plt.hist(x,bins=11, color = 'green')
plt.show()



# 20번

data = [99.46, 44.22, 99.22, 83.76, 66.62, 42.94,  6.06, 83.29, 31.34 ,38.14 ,51.02 ,66.29
, 22.78 ,59.72 , 6.93, 80.04 ,27.39 ,76.67, 85.3 , 50.6  ,34.51 ,96.39 , 9.84 ,99.05,
  0.16, 27.69 ,12.74 , 3.52 , 7.13, 27.74]


print(f"모집단평균추정 : {np.mean(data)}")
print(f"모집단표준편차추정 : {np.std(data,ddof=1)}") # 얘는 오리지널 데이터라서  *루트n 안함
# 곱하는 경우는 한 번 표본평균들에서 걸러진 거임

plt.hist(data,bins=6)
plt.show()

# 21번

    # 구간추정해야함

data = [99.46, 44.22, 99.22, 83.76, 66.62, 42.94,  6.06, 83.29, 31.34 ,38.14 ,51.02 ,66.29
, 22.78 ,59.72 , 6.93, 80.04 ,27.39 ,76.67, 85.3 , 50.6  ,34.51 ,96.39 , 9.84 ,99.05,
  0.16, 27.69 ,12.74 , 3.52 , 7.13, 27.74]


zu = norm.ppf(0.975,0,1) # 1.96
m = np.mean(data)
s = np.std(data, ddof=1)
print(f"하한 : {m - zu * s / np.sqrt(n)}")
print(f"상한 : {m + zu * s / np.sqrt(n)}")

print(f"{norm.interval(0.95, m,s/np.sqrt(n))}")

print(t.interval(0.95,n-1, m, s/np.sqrt(n)))


# 21.2번

n = 30000

# 데이터를 읽어오는 라인
data = np.loadtxt("C:/Users/kiiti/Downloads/data30000.txt")

zu = norm.ppf(0.975,0,1) # 1.96
m = np.mean(data)
s = np.std(data, ddof=1)
print(f"하한 : {m - zu * s / np.sqrt(n)}")
print(f"상한 : {m + zu * s / np.sqrt(n)}")

print(f"{norm.interval(0.95, m,s/np.sqrt(n))}")  

# 