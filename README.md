## webSpider_Douban
[![license][badge-license]][license]


## V1:
返回排行榜电影名字

Output the title-lists of top ten latest movie charts to a csv file

## V2:
返回豆瓣排行榜上前十部电影的数据细节(不再只是电影名!); 表头新增更新时间

Output the information of each movie in the top ten latest movie charts to a csv file

### V2.1:
添加适当注释并优化了有利于分析的数据细节
### V2.2.0:  V2.2.1:
规范化

## V3:
Coming soon...

## Quick Start
### Install
```bash
pip install webSpider-Douban
```
### Do something fun
```python
from webSpider_Douban import Crawler

# default Crawler(info_option='1', output_option='1')
#  option_num   |  info_option  |  output_option  |
#       1       |  title only   |      print      | 
#       2       |    details    |       csv       |
# ** print can only print title so far

aini = Crawler()  
aini.help()  # Generate methods introduction in details
aini.run()  # Fetch data 
# The process normally take 38 seconds.
```
## Issues
###问题
1: CSV文件用Mac上的Excel2016打开出现乱码。
###原因
1: 我在Mac上开发的，Mac上的Excel2016的中文编码方式是GB18030而不是UTF8。
###解决方法
1:

a) CSV文件直接用Numbers打开；
b) CSV文件用Numbers打开后导出到Excel文件；
c) 命令行
```bash
cd 到目标路径
iconv -f UTF8 -t GB18030 old_name.csv >new_name.csv
```
###More
Please contact bHZ6aC5sb3VpczIwMTNAZ21haWwuY29t


[badge-version]: https://img.shields.io/github/license/v1siuol/webSpider_Douban.svg

[pypi]: https://pypi.python.org/pypi/webSpider-Douban
[license]: https://github.com/v1siuol/webSpider_Douban/blob/master/LICENSE.txt