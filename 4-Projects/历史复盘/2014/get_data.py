import baostock as bs
import pandas as pd
import json

# 登录
lg = bs.login()
print(f"登录结果: {lg.error_msg}")

# 获取上证指数2014年数据
print("正在获取2014年上证指数数据...")
rs = bs.query_history_k_data_plus('sh.000001',
    'date,open,high,low,close,volume',
    start_date='2014-01-01',
    end_date='2014-12-31',
    frequency='d')

data_list = []
while rs.next():
    data_list.append(rs.get_row_data())

# 转换为DataFrame
df = pd.DataFrame(data_list, columns=['日期', '开盘', '最高', '最低', '收盘', '成交量'])

# 转换数据类型
df['开盘'] = df['开盘'].astype(float)
df['收盘'] = df['收盘'].astype(float)
df['最高'] = df['最高'].astype(float)
df['最低'] = df['最低'].astype(float)
df['成交量'] = df['成交量'].astype(float)

# 添加年月列
df['年月'] = df['日期'].str[:7]

# 保存日度数据
df[['日期', '开盘', '收盘', '最高', '最低', '成交量', '年月']].to_csv('D:\\历史复盘\\2014\\sh_index_2014.csv', index=False, encoding='utf-8-sig')
print(f"日度数据已保存，共{len(df)}个交易日")

# 计算月度数据
monthly_data = []
for month, group in df.groupby('年月'):
    monthly_data.append({
        '年月': month,
        '开盘': round(group['开盘'].iloc[0], 2),
        '收盘': round(group['收盘'].iloc[-1], 2),
        '最高': round(group['最高'].max(), 2),
        '最低': round(group['最低'].min(), 2),
        '成交量': int(group['成交量'].sum()),
        '涨跌幅': round((group['收盘'].iloc[-1] / group['开盘'].iloc[0] - 1) * 100, 2)
    })

monthly_df = pd.DataFrame(monthly_data)
monthly_df.to_csv('D:\\历史复盘\\2014\\monthly_2014.csv', index=False, encoding='utf-8-sig')
print(f"月度数据已保存，共{len(monthly_df)}个月")

# 计算统计数据
stats = {
    'sh_start': round(float(df['收盘'].iloc[0]), 2),
    'sh_end': round(float(df['收盘'].iloc[-1]), 2),
    'sh_return': round((df['收盘'].iloc[-1] / df['收盘'].iloc[0] - 1) * 100, 2),
    'sh_high': round(float(df['最高'].max()), 2),
    'sh_high_date': df.loc[df['最高'].idxmax(), '日期'],
    'sh_low': round(float(df['最低'].min()), 2),
    'sh_low_date': df.loc[df['最低'].idxmin(), '日期'],
    'max_drawdown': round((1 - df['最低'].min() / df['最高'].max()) * 100, 2)
}

with open('D:\\历史复盘\\2014\\stats_2014.json', 'w', encoding='utf-8') as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)

print("统计数据已保存")
print(f"\n2014年核心数据:")
print(f"年初: {stats['sh_start']:.2f}")
print(f"年末: {stats['sh_end']:.2f}")
print(f"全年涨幅: {stats['sh_return']:.2f}%")
print(f"最高点: {stats['sh_high']:.2f} ({stats['sh_high_date']})")
print(f"最低点: {stats['sh_low']:.2f} ({stats['sh_low_date']})")

bs.logout()
