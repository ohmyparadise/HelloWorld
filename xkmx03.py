##11
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
df=pd.read_excel("cj.xlsx")
df["数目"] = df.count(axis=1)
for i in df.index:
    if df.at[i , "数目" ] == 8:
        df.at[i, "选考成绩"] = df.at[i, "成绩"]-df.at[i, "英"]
    else:
        df.at[i,"选考成绩"] = df.at[i, "成绩"]
df1=df[df.选考成绩>210]
df2 = df1.groupby("校码",as_index=True).count()
plt. figure(figsize = (5, 2))
plt.barh(df2.index,df2.选考成绩)             # 根据图 b ,建立学校与人数的对比图表
plt. xlabel( "人数")
plt. ylabel( "学校")
plt. title( "各学校人数比对")
plt. show()


##12
# def judge(x,c):
#     for j in range(c):
#         if  a[j]==x:
#             return False
#     return True
# import random
# n = 4
# a=[]
# x = random.randint(1,20)           #生成1 ~ 20 之间的随机数
# a.append(x)
# c = 1
# while c<n:
#     x=random.randint(1,20)
#     if judge(x,c)==True:
#         a.append(x)              #在列表 a最后增加元素 x
#         c+= 1
# print(a)
