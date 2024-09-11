from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

# API anahtarlarını güvenli bir şekilde al
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Google Cloud kimlik doğrulama dosyası için ortam değişkeni ayarla
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = GOOGLE_APPLICATION_CREDENTIALS
