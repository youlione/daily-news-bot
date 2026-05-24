import requests

def get_hot_news():
    # 全球热点新闻接口（稳定免费）
    url = "https://api.allorigins.win/get?url=https://news.baidu.com/?cmd=1&page=index"
    try:
        res = requests.get(url, timeout=10)
        data = res.json()
        html = data["contents"]

        # 简单解析热点（你无需修改）
        news_list = []
        import re
        items = re.findall(r'<li class="hotsearch-item[^>]*>.*?<span class="title-content">(.*?)</span>', html)
        for i, title in enumerate(items[:15], 1):
            news_list.append(f"{i}. {title}")
        return "\n".join(news_list)
    except:
        return "获取新闻失败"

# 生成新闻内容
news_content = f"""
# 🔥 全球热点新闻（自动推送）
每日自动更新，无需人工操作

## 今日热点
{get_hot_news()}

---
> 由 GitHub Actions 自动发布
"""

# 保存到文件
with open("news.md", "w", encoding="utf-8") as f:
    f.write(news_content)
