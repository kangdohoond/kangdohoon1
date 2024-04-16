import numpy as np
import pandas as pd # 데이터프레임 쓴다는 뜻

from scipy.stats import binom 
import matplotlib.pyplot as plt

# 표준편차는 0이상 1이하이다 -> X 
# 분산도 0 이상이다 .
# 확률의 합은 1 , 확률은 1 이하 . 

# 100명이 전부 75점 받으면 분산 -> 0

# 이산확률분포가 가중치 고려한 평균 
# 16페이지 이산확률분포 첫줄이 편차제곱 *확률 # 제곱 필수

# 분산 이산확률분포 : E(x^2) - E(x)^2

# E(x) = X * P(x)  -> 즉 E(x^2) = X^2 * P(x)

# 이항확률분포 : 오직 두가지의 경우의 수 (성공 실패만 있는 실험을 n회 반복적
# 으로 시행한다고 할 때 성공실패 횟수를 나타내는 확률변수 x 가 갖게 될 분포)

# 동전 던지기 이항확률분포 : n = 2 , p = 0.5

# 동전 5개 던지기 이항확률분포 : 이거 시험 x 를 0~ 5 중 하나 알려주고 구해보라함

# 이항확률분포 평균 구해봐라 : pmf : 확률질량함수

n = 5 
p = 0.5

x = np.arange(n+1)
mean, var = binom.stats(n,p)

prob = binom.pmf(x,n,p) # ppt 23페이지 확률분포표 p(x) 이게 stats 임 , 리스트에 쫙 출력은 prob

print('mean=', mean, 'var=', var)
plt.bar(x,prob)
plt.title('binom(n=5, p=0.5)')
plt.show()
print(prob)

n = 3 # n = 몇 회임 횟수 
p = 1/3
# p(x=1) = (1  3)(1/3)((2/3)^2) =  ( 3! / (1! * 2!) ) * (1/3) * (4/9) = 4/9
x = np.arange(n+1)
mean, var = binom.stats(n,p)

prob = binom.pmf(x,n,p) # ppt 23페이지 확률분포표 p(x) 이게 stats 임 , 리스트에 쫙 출력은 prob

print('mean=', mean, 'var=', var)
plt.bar(x,prob)
plt.title('binom(n=3, p=1/3)')
plt.show()
print(prob)
# p(x=1) = (3! / (0! *(3!) ) * (1/3 ^0) * (1-1/3)^3-0  = 8/27 = 0.2962 .... 
# p(x=2) = 