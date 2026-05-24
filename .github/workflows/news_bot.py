import requests
import re

def get_hot_news():
    url = "https://top.baidu.com/board?tab=realtime"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        res = requests.get(url, headers=headers, timeout=15)
        res.raise_for_status()
        html = res.text

        # 稳定正则匹配百度热搜
        items = re.findall(r'<div class="c-single-text-ellipsis">(.*?)</div>', html)
        news_list = []

        for i, title in enumerate(items[:15], 1):
            news_list.append(f"{i}. {title.strip()}")

        return "\n".join(news_list)

    except Exception as e:
        return f"获取失败：{str(e)}"

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
