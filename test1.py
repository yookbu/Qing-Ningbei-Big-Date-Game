#本程序用于统计分析哪个手机品牌的购买人数最多
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#读取表格
data1=pd.read_csv('Amazon_Unlocked_Mobile.csv')
#数据清洗
del data1['Reviews']#删除Reviews这一列
data1 = data1.dropna(axis=0)#删除空值
data1.to_csv('cleaned1.csv',index=False)#保存为csv表
#计数
data2 = pd.read_csv('cleaned1.csv')

x = data2['Brand Name']#取数据集中的Brand Name
x0 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])#构造1到10的序列
x1 = x.value_counts()#统计每个品牌的数量
x2 = x1.head(10)#排行榜前十名
print(x2)
#绘图
x2.plot.bar()#用直方图显示
for x, y in zip(x0, x2):#为柱状图添加数字
    plt.text(x - 1, y + 1, '%.f' % y, ha='center', va='bottom')
plt.show()#绘制出图表


