# 作者: 王道 龙哥
# 2024年04月10日11时26分25秒
# xxx@qq.com
import numpy as np
from matplotlib import  pyplot as plt

us_file_path = "youtube_video_data/US_video_data_numbers.csv"
uk_file_path = "youtube_video_data/GB_video_data_numbers.csv"

# t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
t_us = np.loadtxt(us_file_path,delimiter=",",dtype="int")

# 取评论的数据
t_us_comments = t_us[:,-1]



# 怎么知道分多少，打印最大和最小值
print(t_us_comments.max(),t_us_comments.min())

d = 10000

bin_nums = (t_us_comments.max()-t_us_comments.min())//d

# 绘图
plt.figure(figsize=(20,8),dpi=80)

plt.hist(t_us_comments,bin_nums)


plt.show()