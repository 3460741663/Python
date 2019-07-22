import json
import pygal
import math

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

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价 (Y)'
line_chart.x_labels = dates
N = 20 # X轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]
close_log = [math.log10(a) for a in close]
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('收盘价对数变化折线图 (Y) .svg')

