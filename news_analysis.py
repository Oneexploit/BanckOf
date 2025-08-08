# news_analysis.py
from newsapi import NewsApiClient
from transformers import pipeline

# تنظیمات News API
newsapi = NewsApiClient(api_key='YOUR_NEWS_API_KEY')

# دریافت اخبار مرتبط با سهام
def get_news(query):
    all_articles = newsapi.get_everything(q=query,
                                          language='en',
                                          sort_by='publishedAt',
                                          page_size=5)
    return all_articles['articles']

# تحلیل احساسات اخبار
def analyze_sentiment(news_articles):
    sentiment_analyzer = pipeline('sentiment-analysis')

    sentiments = []
    for article in news_articles:
        sentiment = sentiment_analyzer(article['title'] + ". " + article['description'])
        sentiments.append((article['title'], sentiment[0]['label']))

    return sentiments

# مثال استفاده
if __name__ == "__main__":
    articles = get_news("AAPL")
    sentiments = analyze_sentiment(articles)
    for title, sentiment in sentiments:
        print(f"Title: {title}, Sentiment: {sentiment}")
