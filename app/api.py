from fastapi import FastAPI, Depends
from models.schemas import TextRequest, SentimentResponse, HealthResponse
from app.dependencies import get_sentiment_analyzer
from core.sentiment import SentimentAnalyzer

app = FastAPI(
    title="Sentiment Analysis API",
    version="1.0.0",
    description="API для анализа тональности русского текста"
)

@app.post("/analyze-sentiment", response_model=SentimentResponse)
async def analyze_sentiment(
    request: TextRequest,
    analyzer: SentimentAnalyzer = Depends(get_sentiment_analyzer)
):
    """
    Анализ тональности текста
    
    - **context**: Текст для анализа тональности
    """
    sentiment_score = analyzer.get_sentiment(request.context)
    return SentimentResponse(sentiment=sentiment_score)

@app.get("/", response_model=HealthResponse)
async def root():
    return HealthResponse(status="active")

@app.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(status="healthy")