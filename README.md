# zhihu_live
data cleaning and easy visualization

## function of files
- data: 数据清洗
- analysis：数据可视化
- live_ednde:来源数据（已结束的知乎Live）
- ended:清洗后数据
- des_end:数据描述
- live_ongoing：来源数据（正在进行的Live）
- ongoing:清洗后数据
- des_ongo:数据描述
- all:合并数据
## 处理过程
### 数据清洗
- 异常值：将0值改为nan
- 将费用中的数字提取出来
- 提取了介绍的数字（可能与关注人数有关）

### 数据可视化
- 备注：这部分的描述可以等到表达成Jupyter之后比较方便？
- 直方图
- 箱形图
- 简单线性回归分析
 
## 新的尝试
- 这次把所有的代码写成函数，可以直接通过表格名称调用
    
    - 有空的时候写成包，以后不用再复制代码了，别人可视化的时候应该也可以用
- 基本用sns画图，感觉挺好用的
    
    - btw,pycharm画图比Spyder友好（也可能因为我改进了代码.尴尬）

## 下一步工作
- 结果的Jupyter表达
- 学习可视化之后的后期处理怎么做

## 疑问
- 想打标签，需要get到列名…这个不会
- 关于编码：开头的import sys...一串代码的改进方案是？
- 多元回归分析要怎么弄？
- 其实还不太会用jupyter_(:зゝ∠)_
