from flask import Flask
from flask_cors import CORS
from app.fer.api import fer_bp
from app.extensions import mongodb

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Configura CORS
    CORS(app, origins=app.config['CORS_ORIGINS'])
    
    # Inizializza la connessione a MongoDB
    mongodb.connect()

    # Chiudi la connessione al termine dell'app
    @app.teardown_appcontext
    def close_connection(exception):
        mongodb.close()

    # Registra le rotte
    app.register_blueprint(fer_bp, url_prefix='/api/fer')

    return app