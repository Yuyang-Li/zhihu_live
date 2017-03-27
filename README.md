# zhihu_live
data cleaning and easy visualization

## function of files
- tools: 数据清洗(v1.2)
- analysis：数据可视化
- live_ednde:来源数据（已结束的知乎Live）
- ended:清洗后数据
- des_end:数据描述
- live_ongoing：来源数据（正在进行的Live）
- ongoing:清洗后数据
- result_zhihu_live.ipynb：Jupyter notebook输出的结果描述
## 处理过程
### 数据清洗
- 异常值：将0值改为nan
- 将费用中的数字提取出来
- 提取了介绍的字数（可能与关注人数有关）

### 数据可视化
- 直方图
- 箱形图
- 简单线性回归分析
 
## 新的尝试
- 这次把所有的代码写成函数，可以直接通过表格名称调用
- 关于tools(v1.2):改进了代码的模块化
- 基本用sns画图，感觉挺好用的
- btw,pycharm画图比Spyder友好（也可能因为我改进了代码.尴尬）

## 下一步工作
- 改进data cleaning的模块化（做过一次修改）
- 改进jupyter编码的模块化
## 疑问及备注
- 关于编码：开头的import sys的必要性和改进不明
- 可视化和统计分析数据太多了反而不知道怎么选择和使用
- btw..特意筛出了介绍字数，从这个数据的表现来看可以说几乎和live的各项指标毫无关系，至于是和介绍内容无关还是仅仅和字数这个指标无关，如果要研究的话可以做进一步的文本分析（如表达特征、话题）（挖个坑等有空了回头试试）
