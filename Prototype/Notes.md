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

## FER-2013 Dataset
Available on Kaggle (https://www.kaggle.com/datasets/msambare/fer2013). In my mind we can use the dataset to evaluate the performance of the identified FER models on the Raspberry PI. The performance index that we will consider are:
- the accuracy
- the inference time, to calculate the maximum number of frames per second that the model can process.

## FER Models
Already tested and with working code (see fer.ipynb):
- [Facial Expression Recognition using Residual Masking Network](https://github.com/phamquiluan/ResidualMaskingNetwork) 
- [DeepFace](https://github.com/serengil/deepface) (it has a lot of functionalities we can further explore): 
- [Vision Transformer (ViT) for Facial Expression Recognition Model Card](https://huggingface.co/trpakov/vit-face-expression)

To be tested:
- https://github.com/tomas-gajarsky/facetorch (piccoli modelli ma efficienti, da considerare)
- [EmoNet](https://github.com/face-analysis/emonet)

Alla fine non uso facetorch perché è davvero complesso e al suo interno non viene fatta solamente face expression recognition. Come dice nel repository:

    Facetorch is a Python library designed for facial detection and analysis, leveraging the power of deep neural networks. Its primary aim is to curate open-source face analysis models from the community, optimize them for high performance using TorchScript, and integrate them into a versatile face analysis toolkit. 

Quindi è tipo una raccolta di modelli open source per la face analysis... Perciò al suo interno c'è un po' di tutto. Quello che sono andato a fare io è in pratica, sempre guardando al loro repository, di andare nella sezione di fer del readme e vedere quale fosse il modello utilizzato internamente ed alla fine ho visto che è questo https://github.com/HSE-asavchenko/face-emotion-recognition. Per cui mi sono focalizzato direttamente su quello. 

Facetorch comunque oltre alla classe di emozione resituisce anche valence and arsousal quindi alla fine è davvero molto completo.

Quindi a questo punto sono entrato in quel repository [HSEmotion (High-Speed face Emotion recognition) library](https://github.com/av-savchenko/face-emotion-recognition) e mi sono focalizzato più sulla versione onnx (  pip install hsemotion-onnx), aderente quindi al Open Neural Network Exchange (ONNX) standard..

## Details
All the models were pre-trained for face identification task using [VGGFace2 dataset](https://github.com/ox-vgg/vgg_face2). In order to train PyTorch models, [SAM code](https://github.com/davda54/sam) was borrowed.

We upload several [models](models/affectnet_emotions) that obtained the state-of-the-art results for [AffectNet dataset](http://mohammadmahoor.com/affectnet/). The facial features extracted by these models lead to the state-of-the-art accuracy of face-only models on video datasets from EmotiW [2019](https://sites.google.com/view/emotiw2019), [2020](https://sites.google.com/view/emotiw2020) challenges: [AFEW (Acted Facial Expression In The Wild)](https://cs.anu.edu.au/few/AFEW.html), [VGAF (Video level Group AFfect)](https://ieeexplore.ieee.org/document/8925231),  [EngageWild](https://ieeexplore.ieee.org/document/8615851); and ABAW [CVPR 2022](https://ibug.doc.ic.ac.uk/resources/cvpr-2022-3rd-abaw/) and [ECCV 2022](https://ibug.doc.ic.ac.uk/resources/eccv-2023-4th-abaw/) challenges: Learning from Synthetic Data (LSD) and Multi-task Learning (MTL).

Here are the performance metrics (accuracy on AffectNet, AFEW and VGAF), F1-score on LSD, on the validation sets of the above-mentioned datasets and the mean inference time for our models on Samsung Fold 3 device with Qualcomm 888 CPU and Android 12:

| Model | AffectNet (8 classes)  | AffectNet (7 classes)   | AFEW  | VGAF  | LSD | MTL | Inference time, ms | Model size, MB
| :---:   | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| [mobilenet_7.h5](models/affectnet_emotions/mobilenet_7.h5) | -  |  64.71   | 55.35 | 68.92  | - | 1.099 | 16 ± 5| 14 |
| [enet_b0_8_best_afew.pt](models/affectnet_emotions/enet_b0_8_best_afew.pt) | 60.95  | 64.63  | 59.89  | 66.80  | 59.32 | 1.110 |59 ± 26 | 16 |
| [enet_b0_8_best_vgaf.pt](models/affectnet_emotions/enet_b0_8_best_vgaf.pt) | 61.32   | 64.57   | 55.14  | 68.29  | 59.72 | 1.123 |59 ± 26 | 16 |
| [enet_b0_8_va_mtl.pt](models/affectnet_emotions/enet_b0_8_va_mtl.pt) | 61.93   | 64.94   | 56.73  | 66.58  | 60.94 | 1.276 |60 ± 32 | 16 |
| [enet_b0_7.pt](models/affectnet_emotions/enet_b0_7.pt) | -    | 65.74   | 56.99  | 65.18  | - | 1.111 |59 ± 26 | 16 | 16 |
| [enet_b2_7.pt](models/affectnet_emotions/enet_b2_7.pt) | -    | 66.34   | 59.63  | 69.84  | - | 1.134 |191 ± 18 | 30 |
| [enet_b2_8.pt](models/affectnet_emotions/enet_b2_8.pt) | 63.03  | 66.29 | 57.78  | 70.23  | 52.06 | 1.147 |191 ± 18 | 30 |
| [enet_b2_8_best.pt](models/affectnet_emotions/enet_b2_8_best.pt) | 63.125  | 66.51 | 56.73  | 71.12  | - | - |191 ± 18 | 30 |

Please note, that we report the accuracies for AFEW and VGAF only on the subsets, in which MTCNN detects facial regions. The code contains also computation of overall accuracy on the complete testing set, which is slightly lower due to the absence of faces or failed face detection.

Guardare poi ai paper da includere nella bibliografia per tutte le repository a cui si fa riferimento...

Poi pensavo di usare il enet_b2_8 perché ha una accuracy maggiore ma alla fine sto usando enet_b0_8_best_vgaf perché permette di raggiungere FPS maggiori anche 20fps e alla fine la differenza di accuracy è minima.
---



To DO.
- Pulire per bene codice e preparare i diversi modelli.
- Fare in modo che ricevano in input un video e che loggino tutte le emozioni rilevate con relativo timestamp da inizio video per vedere quante vengono rilevate nel complesso del video, poi da qui si potrà capire FPS che Raspberry riesce a gestire facendo formula opportuna. 
- Provare Emonet e anche facetorch che sembra interesante per la piccola dimensione del modello.
- In output cercare di capire i vari formati e formattare tutto allo stesso modo anche come valence and arousal (l'emozione alla fine viene rappresentata come un punto in un piano cartesiano con valence e arousal).





--- 





### EmoNet
We provide two pretrained models : one on 5 emotional classes and one on 8 classes. In addition to categorical emotions, both models also predict valence and arousal values as well as facial landmarks.

To evaluate the pretrained models on the cleaned AffectNet test set, you need to first download the [AffectNet dataset](http://mohammadmahoor.com/affectnet/). 

Results on AffectNet cleaned test set for 5 classes
 Expression
  ACC=0.82

 Valence
  CCC=0.90, PCC=0.90, RMSE=0.24, SAGR=0.85
 Arousal
  CCC=0.80, PCC=0.80, RMSE=0.24, SAGR=0.79


Results on AffectNet cleaned test set for 8 classes
  Expression
    ACC=0.75

  Valence
    CCC=0.82, PCC=0.82, RMSE=0.29, SAGR=0.84
  Arousal
    CCC=0.75, PCC=0.75, RMSE=0.27, SAGR=0.80


Class number to expression name
For 8 emotions :

0 - Neutral
1 - Happy
2 - Sad
3 - Surprise
4 - Fear
5 - Disgust
6 - Anger
7 - Contempt

For 5 emotions :

0 - Neutral
1 - Happy
2 - Sad
3 - Surprise
4 - Fear


@article{toisoul2021estimation,
  author  = {Antoine Toisoul and Jean Kossaifi and Adrian Bulat and Georgios Tzimiropoulos and Maja Pantic},
  title   = {Estimation of continuous valence and arousal levels from faces in naturalistic conditions},
  journal = {Nature Machine Intelligence},
  year    = {2021},
  url     = {https://www.nature.com/articles/s42256-020-00280-0}
}


In the emonet code as taken from the example code of the repository the face detection is done before the emotion detection and in particular the detector used is SFD Detector (from https://github.com/1adrianb/face-alignment). In the latter repository of face-alignment there are several face detectors that can be used, but what they say for the SFD is that: # SFD (likely best results, but slowest).



AffectNet

Existing annotated databases of facial expressions in the wild are small and mostly cover **discrete emotions** (aka the **categorical model**). There are very limited annotated facial databases for affective computing in the **continuous dimensional model** (e.g., valence and arousal).

To meet this need, we have created AffectNet, a new database of facial expressions in the wild, by collecting and annotating facial images. AffectNet contains more than 1M facial images collected from the Internet by querying three major search engines using 1250 emotion related keywords in six different languages. About half of the retrieved images (~440K) were **manually** annotated for the presence of seven discrete facial expressions (categorial model) and the intensity of valence and arousal (dimensional model). AffectNet is by far the largest database of facial expressions, valence, and arousal in the wild enabling research in automated facial expression recognition in two different emotion models. Two baseline deep neural networks are used to classify images in the categorical model and predict the intensity of valence and arousal. Various evaluation metrics show that our deep neural network baselines can perform better than conventional machine learning methods and off-the-shelf facial expression recognition systems.



--- 

### Facetorch
Facetorch is a Python library designed for facial detection and analysis, leveraging the power of deep neural networks. Its primary aim is to curate open-source face analysis models from the community, optimize them for high performance using TorchScript, and integrate them into a versatile face analysis toolkit. The library offers the following key features:

Accelerated Performance: Enjoy enhanced performance on both CPU and GPU with TorchScript optimization.

