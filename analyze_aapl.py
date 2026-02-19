#!/usr/bin/env python3
"""
使用yahooquery分析苹果股票(AAPL)
"""

from yahooquery import Ticker
import json
from datetime import datetime

def analyze_aapl():
    """分析AAPL股票的主要指标"""
    
    # 创建Ticker对象
    aapl = Ticker('AAPL')
    
    # 获取基本信息
    print("🔍 正在获取AAPL股票数据...")
    
    # 价格信息
    price_data = aapl.price
    print("\n💰 价格信息:")
    if 'AAPL' in price_data:
        price_info = price_data['AAPL']
        print(f"  当前价格: ${price_info.get('regularMarketPrice', 'N/A')}")
        print(f"  昨日收盘: ${price_info.get('regularMarketPreviousClose', 'N/A')}")
        print(f"  今日开盘: ${price_info.get('regularMarketOpen', 'N/A')}")
        print(f"  52周区间: ${price_info.get('fiftyTwoWeekLow', 'N/A')} - ${price_info.get('fiftyTwoWeekHigh', 'N/A')}")
        print(f"  市值: ${price_info.get('marketCap', 'N/A'):,}" if isinstance(price_info.get('marketCap'), (int, float)) else f"  市值: {price_info.get('marketCap', 'N/A')}")
    
    # 基本面指标
    key_stats = aapl.key_stats
    print("\n📊 关键指标:")
    if 'AAPL' in key_stats:
        stats = key_stats['AAPL']
        print(f"  市盈率(P/E): {stats.get('trailingPE', 'N/A')}")
        print(f"  前瞻PE: {stats.get('forwardPE', 'N/A')}")
        print(f"  市销率(P/S): {stats.get('priceToSalesTrailing12Months', 'N/A')}")
        print(f"  股息率: {stats.get('dividendYield', 'N/A')}")
        print(f"  负债权益比: {stats.get('debtToEquity', 'N/A')}")
        
    # 财务数据
    financial_data = aapl.financial_data
    print("\n💼 财务数据:")
    if 'AAPL' in financial_data:
        fin_data = financial_data['AAPL']
        print(f"  净利润率: {fin_data.get('profitMargins', 'N/A')}")
        print(f"  ROE(净资产收益率): {fin_data.get('returnOnEquity', 'N/A')}")
        print(f"  ROA(资产回报率): {fin_data.get('returnOnAssets', 'N/A')}")
        print(f"  营业收入: {fin_data.get('totalRevenue', 'N/A')}")
        
    # 收益日历
    calendar_events = aapl.calendar_events
    print("\n📅 收益日历:")
    if 'AAPL' in calendar_events:
        events = calendar_events['AAPL']
        earnings_date = events.get('earnings', {}).get('earningsDate', [])
        if earnings_date and isinstance(earnings_date[0], (int, float)):
            # 如果是时间戳
            print(f"  下次收益发布: {datetime.fromtimestamp(earnings_date[0]).strftime('%Y-%m-%d') if earnings_date else 'N/A'}")
        elif earnings_date and isinstance(earnings_date[0], str):
            # 如果是字符串日期
            print(f"  下次收益发布: {earnings_date[0].split()[0] if earnings_date else 'N/A'}")
        else:
            print("  下次收益发布: N/A")
        print(f"  预期每股收益: {events.get('earnings', {}).get('epsForecast', events.get('earnings', {}).get('earningsAverage', 'N/A'))}")
        print(f"  预期营业收入: {events.get('earnings', {}).get('revenueAverage', 'N/A')}")
    
    # 推荐趋势
    recommendations = aapl.recommendation_trend
    print("\n📈 分析师建议趋势:")
    if 'AAPL' in recommendations:
        recs = recommendations['AAPL']
        print(f"  强力买入: {recs.get('strongBuy', 'N/A')}")
        print(f"  买入: {recs.get('buy', 'N/A')}")
        print(f"  持有: {recs.get('hold', 'N/A')}")
        print(f"  卖出: {recs.get('sell', 'N/A')}")
        print(f"  强力卖出: {recs.get('strongSell', 'N/A')}")
    
    # 公司概况
    asset_profile = aapl.asset_profile
    print("\n🏢 公司概况:")
    if 'AAPL' in asset_profile:
        profile = asset_profile['AAPL']
        print(f"  行业: {profile.get('industry', 'N/A')}")
        print(f"  部门: {profile.get('sector', 'N/A')}")
        print(f"  员工人数: {profile.get('fullTimeEmployees', 'N/A'):,}" if isinstance(profile.get('fullTimeEmployees'), (int, float)) else f"  员工人数: {profile.get('fullTimeEmployees', 'N/A')}")
        print(f"  总部: {profile.get('address1', 'N/A')}, {profile.get('city', 'N/A')}, {profile.get('country', 'N/A')}")
    
    # 技术洞察
    tech_insights = aapl.technical_insights
    print("\n🤖 技术洞察:")
    if 'AAPL' in tech_insights:
        insights = tech_insights['AAPL']
        print(f"  技术评分为: {insights.get('totalScore', 'N/A')}/10")
        if 'instrumentInfo' in insights:
            instrument_info = insights['instrumentInfo'][0] if isinstance(insights['instrumentInfo'], list) else insights['instrumentInfo']
            print(f"  技术趋势: {instrument_info.get('investmentTechnicals', {}).get('signal', 'N/A')}")
    
    # 新闻
    news = aapl.news(count=3)
    print("\n📰 最新新闻:")
    if news:
        for i, article in enumerate(news[:3]):
            print(f"  {i+1}. {article.get('title', 'N/A')}")
            if article.get('pubDate'):
                if isinstance(article.get('pubDate'), (int, float)):
                    print(f"     发布时间: {datetime.fromtimestamp(article.get('pubDate')/1000).strftime('%Y-%m-%d %H:%M') if article.get('pubDate') else 'N/A'}")
                else:
                    print(f"     发布时间: {article.get('pubDate') if article.get('pubDate') else 'N/A'}")
            else:
                print("     发布时间: N/A")

if __name__ == "__main__":
    try:
        analyze_aapl()
        print(f"\n✅ 分析完成于 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"❌ 分析过程中出现错误: {str(e)}")
        import traceback
        traceback.print_exc()