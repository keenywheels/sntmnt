import uvicorn
from analyzer.app.api import app
from config import settings

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=False,
        workers=1,
        log_level=settings.LOG_LEVEL.lower()
    )