#!/usr/bin/env python3
"""Tavily测试脚本"""

import os
import sys

try:
    from tavily import TavilyClient
except ImportError:
    print("❌ Tavily未安装，请运行: pip install tavily-python")
    sys.exit(1)

def test_tavily(api_key):
    """测试Tavily API"""
    try:
        client = TavilyClient(api_key=api_key)
        
        print("✅ Tavily客户端创建成功")
        print("\n🔍 正在测试搜索...")
        
        # 测试搜索新加坡相关信息
        response = client.search(
            query="新加坡自雇EP最新政策",
            search_depth="basic",
            max_results=3
        )
        
        print(f"\n✅ 搜索成功！找到 {len(response.get('results', []))} 条结果")
        
        if response.get('results'):
            print("\n📋 搜索结果预览:")
            for i, result in enumerate(response['results'][:3], 1):
                print(f"\n{i}. {result.get('title', '无标题')}")
                print(f"   🔗 {result.get('url', '无链接')}")
                print(f"   📝 {result.get('content', '无内容')[:150]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        return False

if __name__ == "__main__":
    print("🔧 Tavily测试工具")
    print("=" * 50)
    
    api_key = os.environ.get('TAVILY_API_KEY')
    
    if not api_key:
        print("\n⚠️  未找到TAVILY_API_KEY环境变量")
        print("请设置环境变量: export TAVILY_API_KEY='your-api-key'")
        sys.exit(1)
    
    print(f"\n🔑 使用API密钥: {api_key[:10]}...{api_key[-4:]}")
    
    success = test_tavily(api_key)
    
    if success:
        print("\n🎉 Tavily配置成功！")
        sys.exit(0)
    else:
        print("\n❌ Tavily配置失败")
        sys.exit(1)
