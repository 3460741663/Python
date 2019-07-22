with open('收盘价Dashboard.html', 'w', encoding='utf8') as html_file:
    html_file.write(
        '<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
    for svg in [
            '收盘价月日均值(Y).svg', '收盘价对数变化折线图(Y).svg', '收盘价星期均值(Y).svg',
            '收盘价折线图 (Y) .svg', '收盘价周日均值(Y).svg'
    ]:
        html_file.write(
            '    <object type="image/svg+xml" data="{0}" height=500 width = 600></object>\n'.format(svg))  # 1
    html_file.write('</body></html>')
