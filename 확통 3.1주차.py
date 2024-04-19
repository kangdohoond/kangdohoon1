import numpy as np
import pandas as pd
# 모집단추정 -> OO분포라고 가정하자 , 
fish = np.array([2,3,3,4,4,4,4,5,5,6])

print(f"16번 \n분산 : {fish.var()} {np.var(fish)}")  # 
print(f"불편분산 : {fish.var(ddof=1)} {np.var(fish,ddof=1)}")  # 표본분산,  ddof = 1은 불편분산을 계산할 때,
print(f"표준편차 : {fish.std()} {np.std(fish)}")      # 표준편차
print(f"불편표준편차 : {fish.std(ddof=1)} {np.std(fish, ddof=1)}")

print("정규화 : 몽땅 0 ~ 1 사이로 만들자 어떤 값이든 축소, 식 : (x - min) / (max - min)")
print("표준화 : 식 : (x-mu)/시그마(표준편차), 평균 0 ") # mu 는 평균 
# x - 평균 = 편차 -> 편차는 음수, 0 , 양수 다 가능 , 편차들의 평균은 무조건 0 
# 편차의 거리만 알 거면 제곱하면 됨 
# 편차를 다 제곱해서 평균내면 분산 
# 루트 분산 = 표준편차 


print(f"18번 \n오리지널 fish, {fish}")
fish1 = (fish-fish.min())/(fish.max() -fish.min())
print(f"정규화 fish1 : {fish1}")
fish2 = (fish-fish.mean())/(fish.std())
print(f"표준화 fish2 : {fish2}")
n = np.round(fish2.mean())
print(f"{n}")
print(fish2.var())



#print(f"17번 \n물고기 길이의 정규화 : {sum}")
