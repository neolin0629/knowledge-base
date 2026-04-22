import akshare as ak
import pandas as pd
import json
import os
from datetime import datetime

def get_sh_index_data(year):
    """
    获取上证指数指定年份的数据
    """
    print(f"\n{'='*60}")
    print(f"正在获取 {year} 年上证指数数据...")
    print(f"{'='*60}")
    
    # 创建保存目录
    save_dir = f"D:\\历史复盘\\{year}"
    os.makedirs(save_dir, exist_ok=True)
    
    # 设置日期范围
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    
    # 使用akshare获取日线数据
    try:
        df = ak.stock_zh_a_hist(
            symbol="000001",  # 上证指数代码
            period="daily",   # 日线
            start_date=start_date,
            end_date=end_date,
            adjust=""         # 不复权
        )
        
        if df is None or df.empty:
            print(f"警告：{year}年未获取到数据")
            return None
            
        print(f"成功获取 {len(df)} 条日线数据")
        
        # 重命名列
        df.columns = ['日期', '开盘', '收盘', '最高', '最低', '成交量', '成交额', '振幅', '涨跌幅', '涨跌额', '换手率']
        
        # 保存日线数据
        daily_file = os.path.join(save_dir, f"sh_index_{year}.csv")
        df.to_csv(daily_file, index=False, encoding='utf-8-sig')
        print(f"日线数据已保存: {daily_file}")
        
        # 处理月度数据
        df['日期'] = pd.to_datetime(df['日期'])
        df['年月'] = df['日期'].dt.to_period('M')
        
        monthly_data = df.groupby('年月').agg({
            '开盘': 'first',
            '收盘': 'last',
            '最高': 'max',
            '最低': 'min',
            '成交量': 'sum'
        }).reset_index()
        monthly_data['年月'] = monthly_data['年月'].astype(str)
        
        # 计算月度涨跌幅
        monthly_data['涨跌幅'] = ((monthly_data['收盘'] / monthly_data['开盘'] - 1) * 100).round(2)
        
        # 保存月度数据
        monthly_file = os.path.join(save_dir, f"monthly_{year}.csv")
        monthly_data.to_csv(monthly_file, index=False, encoding='utf-8-sig')
        print(f"月度数据已保存: {monthly_file}")
        
        # 计算年度统计数据
        sh_start = df.iloc[0]['开盘']  # 年初开盘
        sh_end = df.iloc[-1]['收盘']    # 年末收盘
        
        # 全年最高点和最低点
        sh_high = df['最高'].max()
        sh_high_date = df[df['最高'] == sh_high]['日期'].iloc[0]
        
        sh_low = df['最低'].min()
        sh_low_date = df[df['最低'] == sh_low]['日期'].iloc[0]
        
        # 全年涨跌幅
        sh_return = round((sh_end / sh_start - 1) * 100, 2)
        
        # 全年振幅
        full_year_amplitude = round((sh_high - sh_low) / sh_low * 100, 2)
        
        # 最大单日涨幅和跌幅
        max_gain = round(df['涨跌幅'].max(), 2)
        max_gain_date = df[df['涨跌幅'] == df['涨跌幅'].max()]['日期'].iloc[0]
        
        max_loss = round(df['涨跌幅'].min(), 2)
        max_loss_date = df[df['涨跌幅'] == df['涨跌幅'].min()]['日期'].iloc[0]
        
        # 最大回撤
        df['累计最高'] = df['最高'].cummax()
        df['回撤'] = (df['最高'] - df['最低']) / df['累计最高'] * 100
        max_drawdown = round(df['回撤'].max(), 2)
        
        # 构建统计数据
        stats = {
            "年份": year,
            "年初开盘": round(sh_start, 2),
            "年末收盘": round(sh_end, 2),
            "全年涨跌幅": sh_return,
            "全年最高点": round(sh_high, 2),
            "全年最高点日期": sh_high_date.strftime('%Y-%m-%d'),
            "全年最低点": round(sh_low, 2),
            "全年最低点日期": sh_low_date.strftime('%Y-%m-%d'),
            "最大单日涨幅": max_gain,
            "最大单日涨幅日期": max_gain_date.strftime('%Y-%m-%d'),
            "最大单日跌幅": max_loss,
            "最大单日跌幅日期": max_loss_date.strftime('%Y-%m-%d'),
            "全年振幅": full_year_amplitude,
            "最大回撤": max_drawdown
        }
        
        # 保存统计数据
        stats_file = os.path.join(save_dir, f"stats_{year}.json")
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
        print(f"统计数据已保存: {stats_file}")
        
        # 打印统计摘要
        print(f"\n{year}年上证指数统计：")
        print(f"  年初开盘: {stats['年初开盘']}")
        print(f"  年末收盘: {stats['年末收盘']}")
        print(f"  全年涨跌幅: {stats['全年涨跌幅']:.2f}%")
        print(f"  全年最高: {stats['全年最高点']} ({stats['全年最高点日期']})")
        print(f"  全年最低: {stats['全年最低点']} ({stats['全年最低点日期']})")
        print(f"  最大单日涨幅: {stats['最大单日涨幅']:.2f}% ({stats['最大单日涨幅日期']})")
        print(f"  最大单日跌幅: {stats['最大单日跌幅']:.2f}% ({stats['最大单日跌幅日期']})")
        print(f"  全年振幅: {stats['全年振幅']:.2f}%")
        print(f"  最大回撤: {stats['最大回撤']:.2f}%")
        
        return stats
        
    except Exception as e:
        print(f"获取 {year} 年数据时发生错误: {str(e)}")
        import traceback
        traceback.print_exc()
        return None

def main():
    """
    主函数：处理2016-2025年的所有数据
    """
    print("="*60)
    print("上证指数历史数据获取程序 (2016-2025)")
    print("="*60)
    
    # 要处理的年份
    years = range(2016, 2026)  # 2016-2025
    
    # 存储所有年份的统计
    all_stats = []
    
    for year in years:
        stats = get_sh_index_data(year)
        if stats:
            all_stats.append(stats)
    
    # 保存汇总数据
    if all_stats:
        summary_file = "D:\\历史复盘\\summary.json"
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(all_stats, f, ensure_ascii=False, indent=2)
        print(f"\n{'='*60}")
        print(f"所有年份数据获取完成！")
        print(f"汇总数据已保存: {summary_file}")
        print(f"{'='*60}")
        
        # 打印所有年份的涨跌幅
        print("\n2016-2025年上证指数年度涨跌幅：")
        print("-" * 40)
        for stats in all_stats:
            return_str = f"{stats['全年涨跌幅']:+.2f}%"
            print(f"{stats['年份']}年: {stats['年末收盘']:>10.2f} ({return_str})")
        print("-" * 40)

if __name__ == "__main__":
    main()
