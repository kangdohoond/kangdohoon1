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







