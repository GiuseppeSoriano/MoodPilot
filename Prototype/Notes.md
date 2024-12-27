# Prototype Notes

## Requirements for the Prototype

### Evaluate Different FER (Facial Expression Recognition) Models
Identify and test various FER systems that can all be implemented on a Raspberry Pi, comparing their performance.  

**Suggested FER models to explore:**  
- **DeepFace**  
- **Other FER frameworks**  
- **EmoNet** (resource-intensive, suitable for data collection purposes only)  

### Research Paper  
Review the paper titled *"Using Emotion Recognition and Temporary Mobile Social Network in On-Board Services for Car Passengers"* for insights and methodologies.  

### **Infrastructure for Data Collection**  
Design a system for collecting data to support future model training. Key considerations:  
- **Logging**: Maintain detailed records for building an emotion dataset, along with responses from a questionnaire completed at the end of the ride.  
- **Timestamps**: Ensure emotions are logged with precise timestamps to keep track of the sequence and context.  

### Propose Different Models for Experimentation and Deployment  
Develop a two-phase approach for FER model usage:  
1. **Experimentation Phase**: Use a resource-intensive model to collect and analyze data during initial testing.  
2. **Deployment Phase**: Use a lightweight model optimized for real-time FER on the deployed system.  



---


## FER Models
Already tested and with working code (see fer.ipynb):
- [Facial Expression Recognition using Residual Masking Network](https://github.com/phamquiluan/ResidualMaskingNetwork) 
- [DeepFace](https://github.com/serengil/deepface) 
- [Vision Transformer (ViT) for Facial Expression Recognition Model Card](https://huggingface.co/trpakov/vit-face-expression)

To be tested:
- https://github.com/tomas-gajarsky/facetorch (piccoli modelli ma efficienti, da considerare)
- [EmoNet](https://github.com/face-analysis/emonet)


Alla fine non uso facetorch perché è davvero complesso e al suo interno non viene fatta solamente face expression recognition. Come dice nel repository:

    Facetorch is a Python library designed for facial detection and analysis, leveraging the power of deep neural networks. Its primary aim is to curate open-source face analysis models from the community, optimize them for high performance using TorchScript, and integrate them into a versatile face analysis toolkit. 

Quindi è tipo una raccolta di modelli open source per la face analysis... Perciò al suo interno c'è un po' di tutto. Quello che sono andato a fare io è in pratica, sempre guardando al loro repository, di andare nella sezione di fer del readme e vedere quale fosse il modello utilizzato internamente ed alla fine ho visto che è questo https://github.com/HSE-asavchenko/face-emotion-recognition. Per cui mi sono focalizzato direttamente su quello. 

Facetorch comunque oltre alla classe di emozione resituisce anche valence and arsousal quindi alla fine è davvero molto completo.


Quindi a questo punto sono entrato in quel repository [HSEmotion (High-Speed face Emotion recognition) library](https://github.com/av-savchenko/face-emotion-recognition) e mi sono focalizzato più sulla versione onnx (  pip install hsemotion-onnx), aderente quindi al Open Neural Network Exchange (ONNX) standard..





