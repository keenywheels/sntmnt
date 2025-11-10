import logging
from transformers import pipeline
from config import settings

logger = logging.getLogger(__name__)

class SentimentAnalyzer:
    def __init__(self, model_name: str = settings.MODEL_NAME_OR_PATH):
        """
        Инициализация пайплайна для анализа тональности
        """
        logger.info(f"Инициализация модели: {model_name}")
        try:
            self.pipe = pipeline(
                task="sentiment-analysis",
                model=model_name,
                top_k=None
            )
            logger.info("Модель успешно загружена")
        except Exception as e:
            logger.error(f"Ошибка загрузки модели: {e}")
            raise
    
    def _convert_to_score(self, result: list) -> int:
        """
        Конвертация результата в число по формуле:
        negative_score * (-100) + positive_score * 100
        """
        try:
            scores_dict = {item['label']: item['score'] for item in result[0]}
            
            negative_score = scores_dict.get('negative', 0)
            positive_score = scores_dict.get('positive', 0)
            
            final_score = negative_score * (-100) + positive_score * 100
            
            return round(final_score)
        except Exception as e:
            logger.error(f"Ошибка конвертации результата: {e}")
            return 0
    
    def get_sentiment(self, text: str) -> int:
        """
        Получение численной оценки тональности текста
        """
        if not text or not text.strip():
            return 0.0
            
        try:
            pipe_result = self.pipe(text)
            numeric_score = self._convert_to_score(pipe_result)
            logger.debug(f"Проанализирован текст: '{text[:50]}...' -> {numeric_score}")
            return numeric_score
        except Exception as e:
            logger.error(f"Ошибка анализа текста: {e}")
            return 0
