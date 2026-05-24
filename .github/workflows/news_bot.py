import requests
import re

def get_hot_news():
    # 直接抓取百度热搜主页，不使用第三方代理
    url = "https://news.baidu.com/?cmd=1&page=index"
    
    # 模拟浏览器请求头，防止被拦截
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    try:
        res = requests.get(url, headers=headers, timeout=10)
        res.raise_for_status()  # 请求失败直接抛出异常
        html = res.text

        # 正则提取百度热搜标题
        news_list = []
        items = re.findall(r'<li class="hotsearch-item[^>]*>.*?<span class="title-content">(.*?)</span>', html, re.S)
        
        # 取前15条
        for i, title in enumerate(items[:15], 1):
            news_list.append(f"{i}. {title.strip()}")

        return "\n".join(news_list)

    except Exception as e:
        return f"获取新闻失败：{str(e)}"

# 生成新闻内容
news_content = f"""
# 🔥 百度热点新闻（自动推送）
每日自动更新，无需人工操作

## 今日热点
{get_hot_news()}

---
> 由 GitHub Actions 自动发布
"""

# 保存到文件
with open("news.md", "w", encoding="utf-8") as f:
    f.write(news_content)
