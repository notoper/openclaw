#!/usr/bin/env python3
"""
新加坡信息调研脚本
根据SOUL.md的要求，收集和整理新加坡相关信息
"""

import os
import sys
from datetime import datetime
from tavily import TavilyClient

def get_tavily_client():
    """获取Tavily客户端"""
    api_key = os.environ.get('TAVILY_API_KEY')
    if not api_key:
        print("❌ 未设置TAVILY_API_KEY环境变量")
        sys.exit(1)
    return TavilyClient(api_key=api_key)

def search_info(client, query, max_results=5):
    """搜索信息"""
    try:
        response = client.search(
            query=query,
            search_depth="basic",
            max_results=max_results
        )
        return response.get('results', [])
    except Exception as e:
        print(f"⚠️  搜索失败: {query} - {e}")
        return []

def format_results(results, section_name):
    """格式化搜索结果"""
    if not results:
        return f"### {section_name}\n暂无相关信息\n"
    
    text = f"### {section_name}\n"
    for i, result in enumerate(results, 1):
        title = result.get('title', '无标题')
        url = result.get('url', '无链接')
        content = result.get('content', '无内容')
        
        text += f"\n{i}. **{title}**\n"
        text += f"   🔗 {url}\n"
        text += f"   📝 {content}\n"
    
    return text

def main():
    """主函数"""
    print("🔍 开始新加坡信息调研...")
    print("=" * 60)
    
    client = get_tavily_client()
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 调研内容
    research_data = {
        "date": today,
        "ep_news": [],
        "ep_cases": [],
        "ep_analysis": [],
        "immigration_policy": [],
        "tax_policy": [],
        "employment_policy": [],
        "other_policy": [],
        "social_news": [],
        "life_trends": [],
        "local_hotspots": []
    }
    
    # 1. 新加坡自雇EP 动态
    print("\n📋 搜索新加坡自雇EP相关信息...")
    research_data["ep_news"] = search_info(client, "新加坡自雇EP EntrePass 2025 2026 最新政策 新闻", 5)
    research_data["ep_cases"] = search_info(client, "新加坡自雇EP 成功案例 申请经验", 4)
    research_data["ep_analysis"] = search_info(client, "新加坡自雇EP 政策解读 分析 趋势", 4)
    
    # 2. 新加坡政府最新政策
    print("\n📋 搜索新加坡政府政策...")
    research_data["immigration_policy"] = search_info(client, "新加坡移民政策 2025 2026 最新", 4)
    research_data["tax_policy"] = search_info(client, "新加坡税务政策 2025 2026 最新", 4)
    research_data["employment_policy"] = search_info(client, "新加坡就业政策 2025 2026 最新", 4)
    research_data["other_policy"] = search_info(client, "新加坡政府最新政策 2025 2026", 4)
    
    # 3. 新加坡生活热点
    print("\n📋 搜索新加坡生活热点...")
    research_data["social_news"] = search_info(client, "新加坡社会新闻 热点 2025 2026", 4)
    research_data["life_trends"] = search_info(client, "新加坡生活趋势 消费 文化 2025 2026", 4)
    research_data["local_hotspots"] = search_info(client, "新加坡本地热点 话题 讨论 2025 2026", 4)
    
    # 生成报告
    print("\n📝 生成调研报告...")
    report = f"# 素材包：{today}\n"
    report += f"日期：{today}\n"
    report += "\n## 一、新加坡自雇EP 动态\n"
    report += format_results(research_data["ep_news"], "新闻与政策")
    report += "\n"
    report += format_results(research_data["ep_cases"], "成功案例")
    report += "\n"
    report += format_results(research_data["ep_analysis"], "解读与分析")
    
    report += "\n## 二、新加坡政府最新政策\n"
    report += format_results(research_data["immigration_policy"], "移民政策")
    report += "\n"
    report += format_results(research_data["tax_policy"], "税务政策")
    report += "\n"
    report += format_results(research_data["employment_policy"], "就业政策")
    report += "\n"
    report += format_results(research_data["other_policy"], "其他重要政策")
    
    report += "\n## 三、新加坡生活热点\n"
    report += format_results(research_data["social_news"], "社会新闻")
    report += "\n"
    report += format_results(research_data["life_trends"], "生活趋势")
    report += "\n"
    report += format_results(research_data["local_hotspots"], "本地热点")
    
    # 选题建议
    report += "\n## 四、选题建议\n"
    report += "1. 新加坡自雇EP薪资门槛提升对申请者的影响分析\n"
    report += "2. 2025-2026新加坡移民政策变化趋势解读\n"
    report += "3. 新加坡后疫情时代的生活方式变化与消费趋势\n"
    
    # 信息来源
    report += "\n## 五、信息来源\n"
    all_sources = []
    for key in research_data:
        if isinstance(research_data[key], list):
            for result in research_data[key]:
                url = result.get('url')
                if url and url not in all_sources:
                    all_sources.append(url)
    
    for i, url in enumerate(all_sources, 1):
        report += f"- {url}\n"
    
    # 保存报告
    filename = f"singapore-research-{today}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✅ 调研报告已保存: {filename}")
    print(f"\n{'=' * 60}")
    print("🎉 新加坡信息调研完成！")
    print("\n📊 调研统计:")
    print(f"   - 自雇EP相关: {len(research_data['ep_news']) + len(research_data['ep_cases']) + len(research_data['ep_analysis'])} 条")
    print(f"   - 政府政策: {len(research_data['immigration_policy']) + len(research_data['tax_policy']) + len(research_data['employment_policy']) + len(research_data['other_policy'])} 条")
    print(f"   - 生活热点: {len(research_data['social_news']) + len(research_data['life_trends']) + len(research_data['local_hotspots'])} 条")
    print(f"   - 信息来源: {len(all_sources)} 个")

if __name__ == "__main__":
    main()
