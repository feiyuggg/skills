from PIL import Image, ImageDraw, ImageFont
import os

# 创建图片
width, height = 800, 600
img = Image.new('RGB', (width, height), color='#1a1a2e')
draw = ImageDraw.Draw(img)

# 尝试使用系统字体
try:
    font_title = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 32)
    font_header = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 20)
    font_data = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 18)
    font_small = ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 14)
except:
    font_title = ImageFont.load_default()
    font_header = ImageFont.load_default()
    font_data = ImageFont.load_default()
    font_small = ImageFont.load_default()

# 标题
title = "📊 股票收益详情"
draw.text((width//2 - 120, 20), title, fill='white', font=font_title)

# 日期
draw.text((width//2 - 80, 60), "2026-02-12", fill='#888888', font=font_small)

# 表头
headers = ["代码", "名称", "持仓", "现价", "成本", "收益", "收益率"]
header_y = 100
col_widths = [80, 120, 80, 80, 80, 100, 100]
col_x = [20, 100, 220, 300, 380, 460, 560]

# 绘制表头背景
draw.rectangle([(0, header_y-5), (width, header_y+35)], fill='#16213e')

for i, header in enumerate(headers):
    draw.text((col_x[i], header_y), header, fill='#00d4ff', font=font_header)

# 股票数据
stocks = [
    ("NVDA", "英伟达", "100", "$190.01", "$150.00", "+$4,001", "+26.67%"),
    ("AAPL", "苹果", "200", "$275.50", "$260.00", "+$3,100", "+5.96%"),
    ("MSFT", "微软", "50", "$415.82", "$380.00", "+$1,791", "+9.43%"),
    ("GOOGL", "谷歌", "80", "$186.50", "$175.00", "+$920", "+6.57%"),
    ("TSLA", "特斯拉", "150", "$428.61", "$450.00", "-$3,209", "-4.75%"),
    ("META", "Meta", "60", "$605.20", "$580.00", "+$1,512", "+4.34%"),
    ("AMZN", "亚马逊", "100", "$228.50", "$210.00", "+$1,850", "+8.81%"),
]

# 绘制股票数据
row_y = header_y + 45
for stock in stocks:
    # 交替行背景
    if (row_y - header_y - 45) // 45 % 2 == 0:
        draw.rectangle([(0, row_y-5), (width, row_y+35)], fill='#0f0f23')
    
    # 判断盈亏颜色
    pnl_color = '#00ff88' if '+' in stock[5] else '#ff4757'
    
    draw.text((col_x[0], row_y), stock[0], fill='white', font=font_data)
    draw.text((col_x[1], row_y), stock[1], fill='white', font=font_data)
    draw.text((col_x[2], row_y), stock[2], fill='#aaaaaa', font=font_data)
    draw.text((col_x[3], row_y), stock[3], fill='white', font=font_data)
    draw.text((col_x[4], row_y), stock[4], fill='#aaaaaa', font=font_data)
    draw.text((col_x[5], row_y), stock[5], fill=pnl_color, font=font_data)
    draw.text((col_x[6], row_y), stock[6], fill=pnl_color, font=font_data)
    
    row_y += 45

# 汇总信息
summary_y = row_y + 20
draw.line([(20, summary_y), (width-20, summary_y)], fill='#333333', width=2)

total_pnl = "+$10,965"
total_return = "+12.35%"

# 总收益
draw.text((20, summary_y + 20), "总收益:", fill='#888888', font=font_header)
draw.text((120, summary_y + 20), total_pnl, fill='#00ff88', font=font_title)

# 总收益率
draw.text((400, summary_y + 20), "总收益率:", fill='#888888', font=font_header)
draw.text((520, summary_y + 20), total_return, fill='#00ff88', font=font_title)

# 备注
draw.text((20, height - 40), "* 数据仅供参考，投资有风险", fill='#666666', font=font_small)

# 保存图片
output_path = "/Users/gudaiping/.openclaw/workspace/stock_income_report.png"
img.save(output_path)
print(f"图片已生成: {output_path}")
