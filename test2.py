#本程序用与分析哪种手机型号的评分最高
'''
在评判评分高低时定义了一种算法
Rating * Review Votes = Multiply
Multiply / 具体每种型号的个数 = 平均分
'''

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

#数据清洗
data=pd.read_csv('Amazon_Unlocked_Mobile.csv')
del data['Reviews']#删除Reviews这一列
data = data.dropna(axis=0)#删除空值
data.to_csv('cleaned2.csv',index=False)#保存为csv表
#写入替换原表
data1=pd.read_csv('cleaned2.csv')
data2=data1['Rating'] * data1['Review Votes']#求乘积值,暂时赋值给data2存在内存中
with open ('cleaned2.csv','w',) as csvfile:#替换原表所有值在第一行写入'Multiply'
    spamwriter = csv.writer(csvfile,dialect='excel')
    spamwriter.writerow(['Multiply'])
with open ('cleaned2.csv','a', newline='') as f:#在上面表的基础上追加写入乘积值data2
       csv.writer(f).writerows(zip(data2))

data3=pd.read_csv('cleaned2.csv')#读取数据

data4=data1.join(data3)#将数据清洗后的表data1与只有乘积的那张表data3进行拼接
data4.to_csv('cleaned2.csv',index=False)

#分组计算平均值
new_data = pd.read_csv('cleaned2.csv')#读表并赋值给new_data
data_groupby = new_data.groupby('Product Name').agg({'Multiply':[np.mean]})#按Product Name分组求平均值
data_sort = data_groupby.sort_values([('Multiply','mean')],ascending=False)#按product Name分组对平均值进行排序
data_head = data_sort.head(10)#把平均值最高的前十名列出来
print(data_head)

#绘图
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

df_plot=data_head.plot.barh()
df_plot.set_xlabel('平均得分')
df_plot.set_title('评价最高的手机型号')
plt.show()
