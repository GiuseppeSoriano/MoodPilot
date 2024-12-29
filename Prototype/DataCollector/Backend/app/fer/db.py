from app.extensions import mongodb

def insert_report(report, emotional_report):
    """
    Inserisce un report nel database MongoDB con la struttura specificata.

    :param report: Dizionario contenente i dati del report (es. comfort, safety, ...).
    :param emotional_report: Lista di dizionari con i dati emozionali.
    :return: ID del documento inserito o None in caso di errore.
    """
    try:
        # Accedi alla connessione MongoDB
        db = mongodb.db
        if db is None:  # Confronto esplicito con None
            raise ConnectionError("Connessione a MongoDB non disponibile.")

        # Collezione (modifica con il nome desiderato)
        collection = db["reports"]

        # Documento da inserire
        document = {
            **report,  # Aggiunge i campi del report come campi principali
            "emotional_report": emotional_report  # Lista dei dati emozionali
        }

        # Inserisci il documento nella collezione
        result = collection.insert_one(document)
        print(f"Report inserito con ID: {result.inserted_id}")
        return result.inserted_id

    except Exception as e:
        print(f"Errore durante l'inserimento del report: {e}")
        return None
