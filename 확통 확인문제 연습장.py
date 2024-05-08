import numpy as np
import pandas as pd # 데이터프레임 쓴다는 뜻

from scipy.stats import binom 
import matplotlib.pyplot as plt
from scipy.stats import norm 
plt.rcParams['font.family'] = 'Malgun Gothic'

def number(w):
    print(f"########{w}번#########")
number(8.1)
mean = 7
sig = 15
x= np.arange(mean-50, mean+50, 0.1)
y = norm.pdf(x,mean,sig)
plt.bar(x,y)
plt.show()

number(8.2)
m = 175
s= 20
x= np.arange(m-50, m+50, 0.1)
y = norm.pdf(x,m,s)
plt.bar(x,y)
plt.show()

number(9.1)
print(f"(1)  :  (x-170)/10")
number(9.2)
print(f"(2) : (x-25)/ 5")
number(9.3)
print(f"(3) : (x-85)/15")

number(10.1)
print(0.93319-0.5)
m = 0
s = 1
x = norm.cdf(1.5,m,s)
x2 = norm.cdf(0,m,s)
print(x-x2)

number(10.2)
# P(z<=1.5) - P(z<=1)
print(0.93319-0.84134)

m=0
s=1
x=norm.cdf(1,m,s)
x2=norm.cdf(1.5,m,s)
print(x2-x)

number(10.3)

print(2*0.89617)

m=0
s=1
x=norm.cdf(1.26, m, s)
print(2*x)

number(10.4)
# 음수지만 양수여도 넓이는 같기때문에 양수로 계산
print(0.99379 - 0.93319)

m = 0
s=1
x = norm.cdf(2.5,m,s)
x2 = norm.cdf(1.5,m,s)
print(x-x2)

number(10.5)

print(1-0.93319)

m = 0
s = 1
x = norm.cdf(1.5,m,s)
print(1-x)

number(10.6)

print(1-0.97725)

m=0
s=1

x = norm.cdf(2,m,s)
print(1-x)

number(11.1)

m=75
s = 10

x = norm.cdf(90,m,s)
print(1-x)

number(11.2)

m=75
s=10

x = norm.cdf(70,m,s)
x2 = norm.cdf(80,m,s)

print(x2-x)

number(11.3)

m=75
s=10
x = norm.cdf(60,m,s)
print(x)


number(12.1)

z = (90-75)/10 # 1.5

m=0
s=1
x = norm.cdf(z,m,s)
print(1-x)

number(12.2)

z = (70 - 75)/10
z1 = (80 - 75) / 10
m=0
s=1
x = norm.cdf(z,m,s)
x2 = norm.cdf(z1,m,s)
ze = norm.cdf(0,m,s)

print(x2 -x)

print(2*(x2-ze)) # 다른 방법

number(12.3)

z = (60-75)/10   # 양수로 계산 할거면 1-x 해야함

m=0
s=1

x = norm.cdf(z,m,s)
print(x)

number(13.1)
#1.64 ~ 1.65 즉 1.64xxx가 나와야함
m = 0
s=1
print(norm.ppf(0.95,m,s))
# 동일

number(13.2)
# 표 찾아보면 1.95xxxx가 나옴
m = 0
s=1
print(norm.ppf(0.975,m,s))
# 동일

number(13.3)
# 음수표까지 찾아보면 -1.644xxx 임
m = 0
s=1

print(norm.ppf(0.05,m,s))
#동일 

number(13.4)
# 음수표까지 찾아보면 -2.32xxx 가 나옴
m = 0
s=1
print(norm.ppf(0.01,m,s))
# 동일

number(13.5)
# 1.28 xx ~ 1.29 임 즉 1.28xxx
m = 0
s=1
print(norm.ppf(0.9,m,s))



d














