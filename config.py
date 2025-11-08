from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Настройки приложения"""
    
    # Настройки сервера
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    WORKERS: int = 1
    RELOAD: bool = False
    
    # Настройки модели
    MODEL_NAME: str = "seara/rubert-tiny2-russian-sentiment"
    
    # Настройки логирования
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# Создаем экземпляр настроек
settings = Settings()