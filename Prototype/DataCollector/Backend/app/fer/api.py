import os
import tempfile
from flask import request, jsonify, Blueprint
from app.fer.ai import process_video

from app.fer.db import insert_report

# Crea un Blueprint per le API del fer
fer_bp = Blueprint('fer', __name__)

@fer_bp.route('/', methods=['GET'])
def test():
    return jsonify({"message": "FER API works!"}), 200


@fer_bp.route('/report', methods=['POST'])
def report():
    """
    Riceve un report dal frontend, salva il video in una cartella temporanea,
    lo processa e salva il report nel database.
    """
    print("Received report")
    
    # Verifica se il file video è presente nella richiesta
    if 'video' not in request.files:
        return jsonify({"error": "File video mancante"}), 400
    
    video_file = request.files['video']
    
    # Controlla la dimensione del file ricevuto
    if video_file and video_file.filename:
        print("File name:", video_file.filename)
        video_content = video_file.read()  # Legge il contenuto del file
        print("File size (read):", len(video_content))
        
        # Verifica che il contenuto del file non sia vuoto
        if len(video_content) == 0:
            return jsonify({"error": "Il file è vuoto"}), 400
    else:
        return jsonify({"error": "File non ricevuto o nome non valido"}), 400
    
    try:
        # Salva il video in una directory temporanea
        with tempfile.TemporaryDirectory() as temp_dir:
            video_path = os.path.join(temp_dir, video_file.filename)
            print("Temporary video path created:", video_path)
            
            # Scrive il contenuto del file
            with open(video_path, 'wb') as f:
                f.write(video_content)
            
            print("Video file successfully saved in temporary directory")
            
            # Salva il video in una directory permanente per debugging
            permanent_path = os.path.join("/Users/giuseppesoriano/Documents", video_file.filename)
            with open(permanent_path, 'wb') as f:
                f.write(video_content)
            
            print("Video file successfully saved in permanent directory:", permanent_path)
            
            emotional_report = process_video(video_path, show_preview=False)
        
        # Processa il report e il video (modifica secondo necessità)
        report = request.form.to_dict()
        print("Report received:", report)
        
        
        # emotional_report = process_video(permanent_path, show_preview=False)
        # emotional_report = []  # Placeholder per i risultati elaborati
        
        # Inserisci il report nel database
        insert_report(report, emotional_report)
        print("Report inserted successfully")
        
        return jsonify({"message": "Report received and video processed"}), 200

    except Exception as e:
        print("Error processing report:", str(e))
        return jsonify({"error": str(e)}), 500
