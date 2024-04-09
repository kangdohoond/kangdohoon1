import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # 기억하라고 했음 시험 조심 

# data = pd.read_csv("C:/Users/kiiti/Downloads/중학생_남자_키.txt", sep="\t") # type = 데이터프레임
# data = np.loadtxt("C:/Users/kiiti/Downloads/중학생_남자_키.txt") 

# # 히스토그램에서 중요한 건 막대의 수 
# plt.hist(data, label = 'bins=10', bins=10)  # 막대수 10 , hist = 히스토그램
# plt.legend()
# plt.show()

# plt.hist(data, label = 'bins=5', bins=5)
# plt.legend()
# plt.show()
# print (type(data))
# from matplotlib import font_manager, rc

# # 한글 폰트 설정
# font_path = "C:/Windows/Fonts/malgun.ttf"  # 설치한 나눔글꼴 폰트 파일 경로
# font_name = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font_name)   # 걍 내가 해본거임 

# ############################



# x = [6,7,8,9,10,11]
# y = [16109, 41401, 53121, 59899, 53450, 82565]

# plt.bar(x,y) # bar = 막대그래프 그리라는 뜻 
# plt.title('number of cases by month')
# plt.show()

# x = ['str', 'sad', 'dsdsdsd', 'sdsdsdfgg', 'wewe', 'wetgff']
# y = [16109, 41401, 53121, 59899, 53450, 82565]

# plt.bar(x,y) # bar = 막대그래프 그리라는 뜻 
# plt.title('number of cases by month')
# plt.show()

# ratio= [22,24,16,38,5]
# labels = ['피자', '햄버거', '치킨', '파스타', '마라']

# plt.pie(ratio,labels=labels,autopct='%.1f%%')
# plt.show()


# x = [2014, 2015, 2016, 2017, 2018, 2019, 2020]
# y1 = [14.4, 14.5, 15.4, 16.9, 17.8, 17.6, 27.6]
# y2 = [20.5, 21.0, 22.8, 23.6, 24.2, 24.3, 29.5]

# plt.plot(x,y1, linestyle='solid', label='teens')
# plt.plot(x,y2, linestyle='dashed', label='20s')

# plt.legend(loc='best', ncol=2)
# plt.title('internet usege time per week')
# plt.show()

# data = pd.read_excel("C:/Users/kiiti/Downloads/초등학생_키몸무게/초등학생_키몸무게.xlsx")
# plt.scatter(data.weight, data.height)
# plt.xlabel('height')
# plt.ylabel('weight')
# plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # 이거 중요함
data = pd.read_excel("C:/Users/kiiti/Downloads/초등학생_키몸무게/초등학생_키몸무게.xlsx", index_col = 0)
#print(data) # 데이터갯수 = 34 
plt.hist(data, label = 'bins=7', bins=7)  # 막대수 7 , hist = 히스토그램

plt.xlabel('weight')
plt.ylabel('people')

plt.legend()
plt.show()