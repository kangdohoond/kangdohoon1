import numpy as np
import pandas as pd
# 절사평균 : 평균을 내긴하는데 제일 높은 점수와 제일 낮은 점수를 제외(중앙값의 장점)하고 계산.
from scipy import stats
import matplotlib.pyplot as plt
a = np.array([1,2,3,3,4,4,6,7,7,10]) # 36 * 1/8  , 첫 값 끝 값 지워야함
print(f"a의 mean : {a.mean()}")
print(f"a의 절사평균 : {stats.trim_mean(a,0.1)}\n")

x = pd.read_excel("C:/Users/kiiti/Downloads/중학생_남자_몸무게/중학생_남자_몸무게.xlsx") # 이거 시험 , 컬럼명이 있는지 없는지 판단 . 
# header = None  이런 거 
print(f"x의 mean : {x.mean()}")
print(f"x의 10% 절사평균 : {stats.trim_mean(x, 0.1)}\n") # dtype 상관 안 써도 됨

x = pd.read_excel("C:/Users/kiiti/Downloads/중학생_남자_몸무게/중학생_남자_몸무게.xlsx", header = None) # 이거 시험 , 컬럼명이 있는지 없는지 판단 . 
# header = None  이런 거  , 47.5를 안 넣는 거
print(f"x의 mean : {x.mean()}")
print(f"x의 10% 절사평균 : {stats.trim_mean(x, 0.1)}")

# 심슨의 패러독스 -> 전체로보면 남학생이 높은데 하나씩 보면 여학생이 확률 높음 / 그러므로 하나씩만 보면 안 됨 
# 그래도 조작은 아님

# 산포도 : 최댓값 - 최솟값 
# 31페이지 : 더하기는 안변하는데 곱하기는 변함  # 시험
# 데이터에 10배하면 분산은 100배됨 , 표준편차는 10배 # 시험
# 표준편차는 0이 될 수도 있다,  음수 불가능   ## 시험 

# 남자키 얼마 상위 몇퍼센트인지 시험
# 추측할 때 중요한 거 : 어느 분포를 따르는 거 가정 , 2 . 표본에서 얻은 데이터 넣는 거 
# 32페이지  1번 사진 정규분포. 평균 = 중앙값 = 최빈값
# 2번 . 시험이 쉬웠다 . 오른쪾에 쏠려있으면 2번째 사진 . 왜도 < 0 , 평균 < 중앙값 < 최빈값
# 3번 . 시험이 어려웠다 . 왼쪽에 쏠려있으면 3번째 사진 . 왜도 > 0 , 평균 > 중앙값 > 최빈값
# 왜도가 0에 가까울 수록 중앙에 쏠려있음 , 음수면 오른쪾 , 양수는 왼쪽
# 왜도는 0을 기준 
# 손으로 구해봐라 안 나옴 / 나머지는 손으로 계산해봐라 할 수 있음
# 첨도는 3으로 기준 
# 뾰족한 정도 . 커지면 커질수록 뾰족해짐 
# 표준편차는 커지면 커질수록 퍼지는 정도 
#  

# x = pd.DataFrame(pd.read_excel("C:/Users/kiiti/Downloads/외식비/외식비.xlsx"))
# print(f"왜도 : {stats.skew(x)}\n") # 
# print(f"첨도 : {stats.kurtosis(x)}\n") # 

# print(f"{x.describe()}\n") # 하나하나 필요한 거 뽑아서 쓰는 거 시험
# print(f"{stats.describe(x)}\n")


x = pd.DataFrame(pd.read_excel("C:/Users/kiiti/Downloads/외식비/외식비.xlsx"))
print(f"왜도 : {stats.skew(x)}\n") # 
print(f"첨도 : {stats.kurtosis(x)}\n") # 

print(f"{x.describe()}\n")
print(f"{stats.describe(x)}\n")

plt.hist(x.냉면, label = 'food', bins=5, color = 'blue')
print(f"왜도 : {stats.skew(x)}\n") # 왜도 > 0 , 0.161xxx > 0 , 저게 냉면의 왜도임
plt.legend()
plt.xlabel("www")
plt.ylabel("zzz")
plt.show()

plt.hist(x.비빔밥, label = 'food', bins=5, color = 'gray') # 0.6121xxx
print(f"왜도 : {stats.skew(x)}\n") 
plt.legend()
plt.xlabel("www")
plt.ylabel("zzz")
plt.show()

plt.hist(x.김치찌개, label = 'food', bins=5, color = 'skyblue') # 1.0026
print(f"왜도 : {stats.skew(x)}\n")
plt.legend()
plt.xlabel("www")
plt.ylabel("zzz")
plt.show()

plt.hist(x.삼겹살, label = 'food', bins=5, color = 'black') # 0.0395
print(f"왜도 : {stats.skew(x)}\n") 
plt.legend()
plt.xlabel("www")
plt.ylabel("zzz")
plt.show()

plt.hist(x.자장면, label = 'food', bins=5,color = 'purple') # 0.1675
print(f"왜도 : {stats.skew(x)}\n") 
plt.legend()
plt.xlabel("www")
plt.ylabel("zzz")
plt.show()

plt.hist(x.삼계탕, label = 'food', bins=5, color = 'green') # - 0.7236 xxx
print(f"왜도 : {stats.skew(x)}\n") 
plt.legend()
plt.xlabel("www") # 
plt.ylabel("zzz")
plt.show()
plt.hist(x.칼국수, label = 'food', bins=5, color = 'yellow') # -0.0481
print(f"왜도 : {stats.skew(x)}\n") 
plt.legend()
plt.xlabel("www")
plt.ylabel("zzz")
plt.show()
# 1 4 end
plt.hist(x.김밥, label = 'food', bins=5, color = 'red') # -0.1283xxx
print(f"왜도 : {stats.skew(x)}\n") 
plt.legend()
plt.xlabel("www")
plt.ylabel("zzz")
plt.show()
# 냉면 비빔밥 김치찌개 삼겹살 자장면 삼계탕 칼국수 김밥
 # 김치찌개 > 비빔밥 > 자장면 > 냉면 > 삼겹살 > 칼국수 > 김밥 > 삼계탕








