#-*-encoding:utf-8-*-

#计算频数和频率
#计算频数最简单的方法就是用字典。给定一个序列t：
t = []
hist = {}
for x in t:
    hist[x] = hist.get(x,0) + 1

n = float(len(t))
pmf = {}
for x, freq in hist.items():
    pmf[x]  = freq / n
#将值映射到其频数的字典，将其除以n即可把频数转换成概率，这称为归一化
#归一化后的直方图称为PMF（Probability Mass Function,概率质量函数）