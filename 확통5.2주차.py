import numpy as np
import pandas as pd # 데이터프레임 쓴다는 뜻

from scipy import stats
import matplotlib.pyplot as plt
# # 확인문제 18번

# data = pd.read_csv("C:/Users/kiiti/Downloads/sample1 (1).csv") # pd.read 썻다는 건 데이터 프레임 타입이라는 뜻

# import pandas as pd 
# import matplotlib.pyplot as plt
# file_data= pd.read_csv("C:/Users/kiiti/Downloads/sample1 (1).csv")
# print(file_data[0:5])
# total_score= file_data['점수'] * 5 + file_data['출석']
# print(type(total_score))
# print(f"{total_score}\n")

# new_data= [file_data['이름'], total_score]
# print(type(new_data))
# result= pd.concat(new_data, axis=1, keys=['name', 'total'])  # axis = 0  : 위에서 아래로
# print(type(result))
# print(result)       
# result.to_excel("C:/Users/kiiti/Downloads/result1.xlsx") 
# plt.hist(total_score, label='scoredata', bins=7)
# plt.legend()
# plt.savefig("C:/Users/kiiti/Downloads/histogram of score.png")
# plt.show()




# 확인문제 19번 

x = pd.DataFrame(pd.read_excel("C:/Users/kiiti/Downloads/외식비/외식비.xlsx"))

data = pd.concat([x.냉면, x.비빔밥], axis=0)
print(data)


plt.hist(data, label = 'food', bins=6, color = 'blue')
# print(data)
print(f"왜도 : {stats.skew(x)}\n") 
plt.legend()
plt.xlabel("www")
plt.ylabel("zzz")
plt.savefig("C:/Users/kiiti/OneDrive/바탕 화면/histtogram of score.png")
plt.show()

print("\n")


data = pd.read_excel("C:/Users/kiiti/Downloads/중학생_남자_키/중학생_남자_키.xlsx")  # 파일 읽기
data2 = pd.read_excel("C:/Users/kiiti/Downloads/중학생_남자_몸무게/중학생_남자_몸무게.xlsx") # 파일읽기


file_fin = pd.concat([data, data2], axis=0)  # concat으로 데이터를 합침 / 열을 기준으로.
plt.scatter(data, data2) # 산점도 메소드 , x축을 키로 정함 
plt.xlabel('ki') # x축 이름? 을 ki 
plt.ylabel('momuka') # y축 이름을 몸무게
plt.savefig("C:/Users/kiiti/OneDrive/바탕 화면/sanjumpo.png") # savefig를 통해 사진 파일 생성? 저장

plt.show() # 보여주기




