import os
from dotenv import load_dotenv

# Carica le variabili dal file .env
load_dotenv()

class Config:
    # Carica le credenziali dal file .env e solleva un'eccezione se mancano
    MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
    MONGO_PORT = int(os.getenv('MONGO_PORT', 27017))
    MONGO_USER = os.getenv('MONGO_USER')
    MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
    MONGO_DB = os.getenv('MONGO_DB')
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')

    @staticmethod
    def validate():
        """Verifica che tutte le variabili essenziali siano definite."""
        required_vars = ['MONGO_HOST', 'MONGO_PORT', 'MONGO_DB']
        missing_vars = [var for var in required_vars if getattr(Config, var) is None]
        if missing_vars:
            raise EnvironmentError(
                f"Le seguenti variabili d'ambiente mancano: {', '.join(missing_vars)}"
            )

# Valida la configurazione all'avvio
Config.validate()