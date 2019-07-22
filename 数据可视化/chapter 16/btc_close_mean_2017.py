import json
import pygal
import math
from itertools import groupby

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart

# 将数据加载到一个列表中
filename = 'btc_close_2017_urllib.json'
with open(filename) as f:
    btc_data = json.load(f)
    
# 创建5个列表，分别存储日期和收盘数据
dates = []
months = []
weeks = []
weekdays = []
close = []

# 打印每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
    # ~ print("{} is month {} week {}, {}, the close price is {} RMB".format(dates, months, weeks, weekdays, close))

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month], close[:idx_month], '收盘价月日均值(Y)',
    '月日均值')



