from core.sentiment import SentimentAnalyzer

def get_sentiment_analyzer():
    """
    Dependency injection для SentimentAnalyzer
    """
    return SentimentAnalyzer()