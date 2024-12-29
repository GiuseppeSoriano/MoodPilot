# extensions.py
from pymongo import MongoClient
from config import Config  # Assicurati che Config sia importabile

class MongoDBConnection:
    """Gestisce la connessione a MongoDB."""

    def __init__(self):
        self.client = None
        self.db = None

    def connect(self):
        """Crea una connessione a MongoDB."""
        try:
            if Config.MONGO_USER and Config.MONGO_PASSWORD:
                uri = f"mongodb://{Config.MONGO_USER}:{Config.MONGO_PASSWORD}@{Config.MONGO_HOST}:{Config.MONGO_PORT}/{Config.MONGO_DB}"
            else:
                uri = f"mongodb://{Config.MONGO_HOST}:{Config.MONGO_PORT}/{Config.MONGO_DB}"

            self.client = MongoClient(uri)
            self.db = self.client[Config.MONGO_DB]
            print(f"Connesso al database MongoDB: {Config.MONGO_DB}")
        except Exception as e:
            raise ConnectionError(f"Errore nella connessione a MongoDB: {e}")

    def close(self):
        """Chiude la connessione a MongoDB."""
        if self.client:
            self.client.close()
            print("Connessione a MongoDB chiusa.")


# Istanza condivisa per l'app Flask
mongodb = MongoDBConnection()
