from newspaper import Article

def extract_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print("Scraping error:", e)
        return None