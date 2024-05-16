import numpy as np
import pandas as pd # 데이터프레임 쓴다는 뜻

from scipy.stats import binom 
import matplotlib.pyplot as plt
from scipy.stats import norm 
plt.rcParams['font.family'] = 'Malgun Gothic'
from scipy.stats import t

m=50
s=5

x = np.arange(m-50,m+50,0.1)
y = norm.pdf(x,m,s)
plt.bar(x,y)
plt.show()
