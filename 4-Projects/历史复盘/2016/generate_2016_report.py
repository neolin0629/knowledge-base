import pandas as pd
import json
from datetime import datetime
import base64
from io import BytesIO

# 读取数据
with open('stats_2016.json', 'r', encoding='utf-8') as f:
    stats = json.load(f)

df = pd.read_csv('sh_index_2016.csv')
df['日期'] = pd.to_datetime(df['日期'])

monthly_df = pd.read_csv('monthly_2016.csv')

# 生成HTML报告
html_content = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2016年A股年度复盘报告 | 熔断之年</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns"></script>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style type="text/tailwindcss">
        @layer base {{
            body {{
                font-family: 'Inter', sans-serif;
                background: #0a0a0f;
                color: #e2e8f0;
            }}
            h1, h2, h3, h4 {{
                font-family: 'Noto Serif SC', serif;
            }}
        }}
        @layer components {{
            .glass-panel {{
                background: rgba(30, 30, 40, 0.6);
                backdrop-filter: blur(12px);
                border: 1px solid rgba(255, 255, 255, 0.08);
            }}
            .gradient-text {{
                background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }}
            .glow-red {{
                box-shadow: 0 0 30px rgba(239, 68, 68, 0.3);
            }}
            .glow-green {{
                box-shadow: 0 0 30px rgba(34, 197, 94, 0.3);
            }}
            .timeline-line {{
                background: linear-gradient(to bottom, #60a5fa, #a78bfa);
            }}
        }}
    </style>
</head>
<body class="min-h-screen">
    <!-- Hero Section -->
    <header class="relative overflow-hidden py-20 px-6">
        <div class="absolute inset-0 opacity-20">
            <div class="absolute top-0 left-1/4 w-96 h-96 bg-blue-500 rounded-full filter blur-3xl"></div>
            <div class="absolute bottom-0 right-1/4 w-96 h-96 bg-purple-500 rounded-full filter blur-3xl"></div>
        </div>
        <div class="relative max-w-6xl mx-auto text-center">
            <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-red-500/20 border border-red-500/30 text-red-400 text-sm mb-6">
                <span class="w-2 h-2 rounded-full bg-red-500 animate-pulse"></span>
                年度跌幅 -12.24%
            </div>
            <h1 class="text-5xl md:text-7xl font-bold mb-4 gradient-text">2016</h1>
            <h2 class="text-2xl md:text-3xl text-gray-300 mb-6">熔断之年 · 惊魂一月</h2>
            <p class="text-gray-400 max-w-2xl mx-auto text-lg">
                年初熔断机制引发史诗级暴跌，全年振幅高达34.13%。<br>
                从3538点断崖式下跌至2638点，市场经历了前所未有的恐慌。
            </p>
        </div>
    </header>

    <!-- Key Metrics -->
    <section class="px-6 py-12">
        <div class="max-w-6xl mx-auto">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
                <div class="glass-panel rounded-2xl p-6 text-center glow-red">
                    <div class="text-3xl font-bold text-red-400">{stats['全年涨跌幅']:.2f}%</div>
                    <div class="text-sm text-gray-400 mt-1">全年涨跌幅</div>
                </div>
                <div class="glass-panel rounded-2xl p-6 text-center">
                    <div class="text-3xl font-bold text-gray-200">{stats['全年振幅']:.2f}%</div>
                    <div class="text-sm text-gray-400 mt-1">全年振幅</div>
                </div>
                <div class="glass-panel rounded-2xl p-6 text-center">
                    <div class="text-3xl font-bold text-red-400">{stats['最大回撤']:.2f}%</div>
                    <div class="text-sm text-gray-400 mt-1">最大回撤</div>
                </div>
                <div class="glass-panel rounded-2xl p-6 text-center">
                    <div class="text-3xl font-bold text-gray-200">{stats['年末收盘']:.0f}</div>
                    <div class="text-sm text-gray-400 mt-1">年末收盘</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Price Chart -->
    <section class="px-6 py-12">
        <div class="max-w-6xl mx-auto">
            <div class="glass-panel rounded-2xl p-6">
                <h3 class="text-xl font-semibold mb-6 flex items-center gap-2">
                    <span class="w-1 h-6 bg-gradient-to-b from-blue-500 to-purple-500 rounded-full"></span>
                    上证指数全年走势
                </h3>
                <div class="h-80">
                    <canvas id="priceChart"></canvas>
                </div>
            </div>
        </div>
    </section>

    <!-- Monthly Performance -->
    <section class="px-6 py-12">
        <div class="max-w-6xl mx-auto">
            <div class="glass-panel rounded-2xl p-6">
                <h3 class="text-xl font-semibold mb-6 flex items-center gap-2">
                    <span class="w-1 h-6 bg-gradient-to-b from-blue-500 to-purple-500 rounded-full"></span>
                    月度表现
                </h3>
                <div class="h-64">
                    <canvas id="monthlyChart"></canvas>
                </div>
            </div>
        </div>
    </section>

    <!-- Timeline -->
    <section class="px-6 py-12">
        <div class="max-w-4xl mx-auto">
            <h3 class="text-2xl font-semibold mb-10 text-center">2016年大事记</h3>
            <div class="relative">
                <div class="absolute left-4 md:left-1/2 top-0 bottom-0 w-0.5 timeline-line transform md:-translate-x-1/2"></div>
                
                <div class="space-y-8">
                    <div class="relative flex flex-col md:flex-row items-start md:items-center">
                        <div class="md:w-1/2 md:pr-8 md:text-right">
                            <div class="glass-panel rounded-xl p-4">
                                <div class="text-red-400 font-bold">1月4日</div>
                                <div class="text-sm text-gray-300">熔断首日</div>
                                <div class="text-xs text-gray-500 mt-1">A股首次实施熔断机制，当日暴跌6.86%</div>
                            </div>
                        </div>
                        <div class="absolute left-4 md:left-1/2 w-4 h-4 bg-red-500 rounded-full border-4 border-gray-900 transform -translate-x-1/2 md:-translate-x-1/2"></div>
                        <div class="md:w-1/2 md:pl-8 pl-12"></div>
                    </div>
                    
                    <div class="relative flex flex-col md:flex-row items-start md:items-center">
                        <div class="md:w-1/2 md:pr-8"></div>
                        <div class="absolute left-4 md:left-1/2 w-4 h-4 bg-red-600 rounded-full border-4 border-gray-900 transform -translate-x-1/2 md:-translate-x-1/2"></div>
                        <div class="md:w-1/2 md:pl-8 pl-12">
                            <div class="glass-panel rounded-xl p-4">
                                <div class="text-red-400 font-bold">1月7日</div>
                                <div class="text-sm text-gray-300">二次熔断</div>
                                <div class="text-xs text-gray-500 mt-1">开盘仅29分钟即触发熔断，创历史最快纪录</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="relative flex flex-col md:flex-row items-start md:items-center">
                        <div class="md:w-1/2 md:pr-8 md:text-right">
                            <div class="glass-panel rounded-xl p-4">
                                <div class="text-yellow-400 font-bold">1月7日</div>
                                <div class="text-sm text-gray-300">暂停熔断</div>
                                <div class="text-xs text-gray-500 mt-1">证监会紧急叫停熔断机制，仅实施4天</div>
                            </div>
                        </div>
                        <div class="absolute left-4 md:left-1/2 w-4 h-4 bg-yellow-500 rounded-full border-4 border-gray-900 transform -translate-x-1/2 md:-translate-x-1/2"></div>
                        <div class="md:w-1/2 md:pl-8 pl-12"></div>
                    </div>
                    
                    <div class="relative flex flex-col md:flex-row items-start md:items-center">
                        <div class="md:w-1/2 md:pr-8"></div>
                        <div class="absolute left-4 md:left-1/2 w-4 h-4 bg-red-700 rounded-full border-4 border-gray-900 transform -translate-x-1/2 md:-translate-x-1/2"></div>
                        <div class="md:w-1/2 md:pl-8 pl-12">
                            <div class="glass-panel rounded-xl p-4">
                                <div class="text-red-400 font-bold">1月27日</div>
                                <div class="text-sm text-gray-300">全年最低点</div>
                                <div class="text-xs text-gray-500 mt-1">指数触及2638.30点，为全年最低点</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="relative flex flex-col md:flex-row items-start md:items-center">
                        <div class="md:w-1/2 md:pr-8 md:text-right">
                            <div class="glass-panel rounded-xl p-4">
                                <div class="text-green-400 font-bold">3月2日</div>
                                <div class="text-sm text-gray-300">强势反弹</div>
                                <div class="text-xs text-gray-500 mt-1">单日大涨4.26%，创全年最大单日涨幅</div>
                            </div>
                        </div>
                        <div class="absolute left-4 md:left-1/2 w-4 h-4 bg-green-500 rounded-full border-4 border-gray-900 transform -translate-x-1/2 md:-translate-x-1/2"></div>
                        <div class="md:w-1/2 md:pl-8 pl-12"></div>
                    </div>
                    
                    <div class="relative flex flex-col md:flex-row items-start md:items-center">
                        <div class="md:w-1/2 md:pr-8"></div>
                        <div class="absolute left-4 md:left-1/2 w-4 h-4 bg-blue-500 rounded-full border-4 border-gray-900 transform -translate-x-1/2 md:-translate-x-1/2"></div>
                        <div class="md:w-1/2 md:pl-8 pl-12">
                            <div class="glass-panel rounded-xl p-4">
                                <div class="text-blue-400 font-bold">6月24日</div>
                                <div class="text-sm text-gray-300">英国脱欧</div>
                                <div class="text-xs text-gray-500 mt-1">英国脱欧公投通过，全球股市震荡</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="relative flex flex-col md:flex-row items-start md:items-center">
                        <div class="md:w-1/2 md:pr-8 md:text-right">
                            <div class="glass-panel rounded-xl p-4">
                                <div class="text-purple-400 font-bold">11月</div>
                                <div class="text-sm text-gray-300">深港通获批</div>
                                <div class="text-xs text-gray-500 mt-1">深港通正式获批，市场迎来利好</div>
                            </div>
                        </div>
                        <div class="absolute left-4 md:left-1/2 w-4 h-4 bg-purple-500 rounded-full border-4 border-gray-900 transform -translate-x-1/2 md:-translate-x-1/2"></div>
                        <div class="md:w-1/2 md:pl-8 pl-12"></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Market Analysis -->
    <section class="px-6 py-12">
        <div class="max-w-6xl mx-auto">
            <div class="grid md:grid-cols-2 gap-6">
                <div class="glass-panel rounded-2xl p-6">
                    <h4 class="text-lg font-semibold mb-4 text-red-400">市场特征</h4>
                    <ul class="space-y-3 text-sm text-gray-300">
                        <li class="flex items-start gap-2">
                            <span class="text-red-500 mt-1">•</span>
                            <span>熔断机制实施仅4天即被叫停，成为A股史上最短命的制度</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-red-500 mt-1">•</span>
                            <span>1月份跌幅达22.59%，创历史最大单月跌幅之一</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-red-500 mt-1">•</span>
                            <span>全年最大回撤25.44%，投资者信心遭受重创</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-red-500 mt-1">•</span>
                            <span>监管层多次出手维稳，包括暂停IPO、限制减持等</span>
                        </li>
                    </ul>
                </div>
                <div class="glass-panel rounded-2xl p-6">
                    <h4 class="text-lg font-semibold mb-4 text-green-400">投资机会</h4>
                    <ul class="space-y-3 text-sm text-gray-300">
                        <li class="flex items-start gap-2">
                            <span class="text-green-500 mt-1">•</span>
                            <span>3月份反弹11.74%，为全年最佳月度表现</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-green-500 mt-1">•</span>
                            <span>8-11月震荡上行，从2800点反弹至3300点</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-green-500 mt-1">•</span>
                            <span>供给侧改革主题贯穿全年，煤炭、钢铁板块表现亮眼</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-green-500 mt-1">•</span>
                            <span>年末深港通开通，外资持续流入</span>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="px-6 py-8 text-center text-gray-500 text-sm">
        <p>数据来源：东方财富 | 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
    </footer>

    <script>
        // 价格走势图
        const priceCtx = document.getElementById('priceChart').getContext('2d');
        const priceData = {df[['日期', '收盘']].to_dict('records')};
        
        new Chart(priceCtx, {{
            type: 'line',
            data: {{
                labels: priceData.map(d => d['日期']),
                datasets: [{{
                    label: '上证指数',
                    data: priceData.map(d => d['收盘']),
                    borderColor: '#60a5fa',
                    backgroundColor: 'rgba(96, 165, 250, 0.1)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.4,
                    pointRadius: 0,
                    pointHoverRadius: 4
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                interaction: {{
                    intersect: false,
                    mode: 'index'
                }},
                plugins: {{
                    legend: {{
                        display: false
                    }},
                    tooltip: {{
                        backgroundColor: 'rgba(30, 30, 40, 0.9)',
                        titleColor: '#e2e8f0',
                        bodyColor: '#e2e8f0',
                        borderColor: 'rgba(255, 255, 255, 0.1)',
                        borderWidth: 1
                    }}
                }},
                scales: {{
                    x: {{
                        grid: {{
                            color: 'rgba(255, 255, 255, 0.05)'
                        }},
                        ticks: {{
                            color: '#64748b',
                            maxTicksLimit: 6
                        }}
                    }},
                    y: {{
                        grid: {{
                            color: 'rgba(255, 255, 255, 0.05)'
                        }},
                        ticks: {{
                            color: '#64748b'
                        }}
                    }}
                }}
            }}
        }});

        // 月度表现图
        const monthlyCtx = document.getElementById('monthlyChart').getContext('2d');
        const monthlyData = {monthly_df[['年月', '涨跌幅']].to_dict('records')};
        
        new Chart(monthlyCtx, {{
            type: 'bar',
            data: {{
                labels: monthlyData.map(d => d['年月']),
                datasets: [{{
                    label: '月度涨跌幅',
                    data: monthlyData.map(d => d['涨跌幅']),
                    backgroundColor: monthlyData.map(d => d['涨跌幅'] >= 0 ? 'rgba(34, 197, 94, 0.7)' : 'rgba(239, 68, 68, 0.7)'),
                    borderColor: monthlyData.map(d => d['涨跌幅'] >= 0 ? '#22c55e' : '#ef4444'),
                    borderWidth: 1
                }}]
            }},
            options: {{
                responsive: true,
                maintainAspectRatio: false,
                plugins: {{
                    legend: {{
                        display: false
                    }},
                    tooltip: {{
                        backgroundColor: 'rgba(30, 30, 40, 0.9)',
                        titleColor: '#e2e8f0',
                        bodyColor: '#e2e8f0',
                        borderColor: 'rgba(255, 255, 255, 0.1)',
                        borderWidth: 1,
                        callbacks: {{
                            label: function(context) {{
                                return context.parsed.y.toFixed(2) + '%';
                            }}
                        }}
                    }}
                }},
                scales: {{
                    x: {{
                        grid: {{
                            color: 'rgba(255, 255, 255, 0.05)'
                        }},
                        ticks: {{
                            color: '#64748b'
                        }}
                    }},
                    y: {{
                        grid: {{
                            color: 'rgba(255, 255, 255, 0.05)'
                        }},
                        ticks: {{
                            color: '#64748b',
                            callback: function(value) {{
                                return value + '%';
                            }}
                        }}
                    }}
                }}
            }}
        }});
    </script>
</body>
</html>
'''

# 保存HTML文件
with open('2016_A股年度复盘报告.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("2016年复盘报告已生成：2016_A股年度复盘报告.html")
