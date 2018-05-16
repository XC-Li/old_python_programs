# 图书馆上座研究
By Xc.Li
Last update: Apr.24
共享数据（百度云）：http://pan.baidu.com/s/1skJiMnV
如何获取、处理数据的技术细节：http://www.jianshu.com/p/bc02a7a70b81
简单来说就是在每天7：00~23：00之间在每个小时的00，10，20，30，40，50分钟获取图书馆当时所有楼层的上座情况，然后保存到一个文件里。
**基于共享数据得出的研究结果需要在发布的结果上标上本人名字与本文链接**
#研究目标
不同周的同一天的上座规律有什么不同？同一周的不同天的上座规律有什么不同？上座人数与时间之间是否存在普遍性规律，或者受什么因素影响发生改变？


#数据处理
用stata里的命令将三周22天的数据整合到一个文件里了。在百度云根目录：**ROS.dta**
数据格式：

    use ROS.dta

|变量名称|变量内容|
|----|----|
|dec_time|以十进制格式的时间|
|*[day]* *[n]*F*m*|第n个星期*[day]*的*[m]*楼的上座人数（绝对值）|
|*[day]* tso|第n个星期*[day]*的总上座人数（绝对值）|
|*[day]* tsor|第n个星期*[day]*的总上座率（tso/1596）|
TSO(Total Seat Occupied)
TSOR (Total Seat Occupied Rate)

#基本图形分析
观测期：Mar.28-Apr.18
**第一周** :Mar.28 - Apr.03
**第二周** :Apr.04 - Apr.10
**第三周** :Apr.11- Apr.17

## 不同周之间对同天进行比较
    graph twoway line Mon1tso dec_time || line Mon3tso dec_time || line Mon4tso dec_time ,xlabel(7(1)23) ylabel(0(150)1596)

![周一](http://upload-images.jianshu.io/upload_images/1034202-ddab0553a67148e0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![周二](http://upload-images.jianshu.io/upload_images/1034202-49ab9c85483504b3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![周三](http://upload-images.jianshu.io/upload_images/1034202-fbdaf2ce0106f150.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![周四](http://upload-images.jianshu.io/upload_images/1034202-68d0d98ea6717024.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![周五](http://upload-images.jianshu.io/upload_images/1034202-33af29b09bd2bbfe.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![周六](http://upload-images.jianshu.io/upload_images/1034202-c279db9ce5f7b5c1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![周日](http://upload-images.jianshu.io/upload_images/1034202-8ac312e9bebf4973.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

可以看出：
周一：涨跌时间相似，幅度：四、三、一，一三周接近
周二：涨跌时间相似，幅度：三、（一二周接近）
周三：涨跌时间相似，幅度：三、二、一，上午一三周接近，下午二三周接近
周四：涨跌时间相似，幅度：三、二、一，上午接近，下午有明显区别
周五：涨跌时间相似，幅度：三、二、一，二三接近
周六：涨跌二三周接近，与第一周区别明显（数据不完整度比较大）
周日：涨跌二三周接近，与第一周区别明显

###结论1：
观测期间，周际在涨跌时间上有相似性，规律稳定。但是在具体上座人数上有区别。总体而言是第三周人数大于第二周大于第一周。
上午上座的规律性强于下午和晚上，周末的规律性强于工作日。

## 同一周不同天之间进行比较

    graph twoway line  Mon1tso dec_time || line Tue1tso dec_time || line Wed1tso dec_time || line Thu1tso dec_time || line Fri1tso dec_time,xlabel(7(1)23) ylabel(0(150)1596)


![第一周](http://upload-images.jianshu.io/upload_images/1034202-bed065c90d8235fc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![第二周（没有周一的数据）](http://upload-images.jianshu.io/upload_images/1034202-a0f3db329ec521d2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![第三周](http://upload-images.jianshu.io/upload_images/1034202-bdebea19fb137dbc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

可以看出：
第一周：周一周二非常接近，周三周四比较接近，周五差异较大
第二周：没有周一的数据，周三周四比较接近，周五差异较大
第三周：周一二三四都比较接近，但晚上周一周二接近，周三周四接近，周五差异大。

###结论2：
周一周二较接近，周三周四较接近，周五应该单独列出。
看起来15：00前上座人数都比较少，模式都比较接近。而15：00以后不同天、不同周之间差别变大。

>进一步研究：找出周一~周四、周五、周六周日的上座变化规律
可能进一步细化不同楼层的上座规律