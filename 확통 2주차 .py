import numpy as np
import pandas as pd 


# 리스트는 다양한 타입 가질 수 있음 
# 배열 array 는 다양한 타입 가질 수 없음 , 즉 str 이랑 int가 같이있으면 둘다 str로 변함 
# DataFrame은 다양한 타입 가질 수 있음 . 

# df = pd.DataFrame(
# [[1,2],
#  [3,4],
#  [5,6]],
#     columns = ['a','b'])   # 꼭 columns 를 써야함 다른 변수 안 됨  # 바꾸고싶으면 df.columns=['가', '나']
# print(df)   
# pd.concat ([]) = 데이터를 병합하다 라는 뜻 
df1 = pd.DataFrame({
    'col1' : [1,2,3,4,5],
    'col2' : [2,4,6,8,10],
    'col3' : ['A', 'B', 'C', 'D', 'E']})

print(df1)
print(f"{df1.head(n=3)} 11페이지 1번 " )  # 맨 위에 3개만 출력하라는 뜻 
print(f"{df1.query('index==0')} 11페이지 2번 " ) # 0행 출력하라는 뜻 
print(f"{df1.query('col3=="B"')} 11페이지 3번 ") # 따옴표 작은 거 안에 작은거 불가능 / 작은 거 안에 큰거만 
# col3 에 있는 B 위치의 행을 출력하라는 뜻 
print(f"{df1.query('col3=="A" & col1==2')} 11페이지 4번 ")  # ??  데이터를 찾아와라 그런 뜻 커리 
print(f"{df1.query('col3=="A" | col1 == 2')} 11페이지 5번 ")
print(f"{df1.query('col3=="A"')[['col2','col3']]} 11페이지 6번 ")


# 데이터프레임에서 컬럼 한개의 타입은 시리즈임 . 데이터프레임 자체의 타입을 치면 데이터프레임 타입이라고 나옴 
# 배열로 바꾸고싶으면 np.array 안에 넣으면 됨
# df.col1.values 써도 됨
# axis = 0 행이 많아지는 거 / axis = 1 열이 많아지는 거

# 모집단 


# 중요 : 통계학에서는 '모집단이 특정분포를 따른다고 가정' 합니다. 
# 포아송분포 : 가장 소중한 사람이 나의 수업이 끝나고 문 앞에 있을 확률 . 0 % 는 아니지만 정말 작은 확률 
# 
def w ():
    print("\n")
r = np.zeros(5, dtype = int)
print(f"{r} 9번의 1번 문제") # 컴마 안나옴 
w()
a = np.zeros((3,3), dtype = int)
print(f"{a} 9번의 2번")
w()
a = np.ones(5, dtype = float)
print(f"{a} 9번의 3번")
w()
a = np.tile(5,9)
print(f"{a}, 10번의 1번 ")
w()
a = np.full(5,9)
print(f"{a}, 10번의 2번 ")
w()
a = np.eye(3, dtype = int)  # eye = I , 단위행렬 출력하는 거임 
print(f"{a}, 10번의 3번 ")
w()
a = np.arange(20)
print(f"{a}, 11번의 1번 ")
w()

print(f"{a.reshape(4,5)}, 11번의 2번 ")
w()

print(f"{a} 11번의 3번") # 리셰입 한다해서 a가 바뀌진 않음
w()

a = [1,'A']
print(type(a[0]))
print(f"{type(a[1])} 12번 1번")
w()
a = np.array(a)
print(type(a[0]))
print(f"{type(a[1])} 12번 2번")
w()
df1 = pd.DataFrame({
    'a' : [1,2,3],
    'b' : [ 4,5,6]
})   
df2 = pd.DataFrame({
    'a' : [7,8,9],
    'b' : [10,11,12]
})

cc = pd.concat([df1, df2], axis = 0 )
print(f"{cc} 13번 1번  \n")

cc = pd.concat([df1, df2], axis = 1 )
print(f"{cc} 13번 2번  \n")



# df1 = pd.DataFrame({
#     ['A',1], ['B', 2], ['C',3]
# })
a = pd.DataFrame(
    [['A', 1], ['B', 2], ['C',3]],
    columns = ['x1', 'x2']
)
b = pd . DataFrame({
    'x1':['B', 'C', 'D'],
    'X3':[2,3,4]
})

print(f"{a}, 14번 \n")
print(b, "\n")
print(pd.concat([a,b]), '\n')
print(pd.concat([a,b], axis=1) , '\n')






