---
header-includes: |
    \usepackage{graphicx}
    \usepackage{seqsplit}
    \usepackage{fvextra}
    \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
    \usepackage{caption}
    \usepackage{subcaption}
    \usepackage{xcolor}
    \usepackage{lscape}

    \usepackage{tabularx}
    \usepackage{booktabs}
    \usepackage{caption}
    \usepackage{geometry}
    \usepackage{xltabular}


bibliography: references.bib
csl: ieee.csl
---


<!--
How to write the project documentation (prototype document)
- Abstract (resume the document)
- Introduction 
  - Aims and Scope of the document
  - System description and highlights
  - Problem Formulation (if relevant) 
- Related Work (if relevant)
  - Description of the work relevant for your application/system
- System Description
  - What are the components of your system and how it works 
  - Main modules description and their interaction
- Algorithm description (if any)
- Prototype and Demo set-up and description
  - Hardware description (hardware modules that we are utilizing in our system) - No manuals, just the reference to them
  - Allocation of software modules to the hardware (relevant if you utilize a cloud/distributed solution)
- Performance evaluation and optimization (if relevant)
  - E.g. in "ScheduleAndGo" there are different scheduling algorithms.
  - For performance reason you need to parallelize your code. 
  - You can measure the performance of your system and try to explain if the prototype is able to sustain the real-time requirements of your application.
- Structure of the Demo
- Conclusions.
- References.
- Video of the Demo.
- Code 
  - You can add a code section 
  - Specify the imported library 
  - GitHub repository link
-->

\title{Industrial Applications}

\begin{figure}[!htb]
    \centering
    \includegraphics[keepaspectratio=true,scale=0.4]{Resources/"cherub.eps"}
\end{figure}

\begin{center}
    \LARGE{UNIVERSITY OF PISA}
    \vspace{5mm}
    \\ \large{MASTER'S DEGREE IN COMPUTER ENGINEERING}\vspace{3mm}
    \\ \large{Industrial Applications}
    \vspace{10mm}
    \\ \LARGE\textbf{MoodPilot}
\end{center}

\vspace{25mm}

\begin{minipage}[t]{0.47\textwidth}
	{\large{Professors:}{\normalsize\vspace{3mm} \bf\\ \large{Pierfrancesco Foglia}\vspace{3mm}
 \\ \large{Antonio Cosimo Prete} }}
\end{minipage}
\hfill
\begin{minipage}[t]{0.47\textwidth}\raggedleft
 {\large{Students:}\raggedleft
 {\normalsize\vspace{2mm}
	\bf\\ \large{Giovanni Ligato}\raggedleft\vspace{3mm}
    \\ \large{Giuseppe Soriano}\raggedleft }}
\end{minipage}

\vspace{45mm}

\hrulefill

\begin{center}
\normalsize{ACADEMIC YEAR 2024/2025}
\end{center}

\pagenumbering{gobble}

\renewcommand*\contentsname{Index}
\tableofcontents


\newpage

\pagenumbering{arabic}


<!-- Provare a mettere l'abstract direttamente nel frontespizio in piccolo -->
# 1. Abstract

\newpage


# 2. Theoretical Background on Emotions


Emotions are complex psychological states that encompass subjective experiences, physiological responses, and behavioral expressions. They significantly influence human cognition and social interactions, affecting decision-making, perception, and relationships.

## 2.1. Emotion Classifications

Various models have been developed to categorize emotions:

- **Discrete Emotion Theory**: This theory suggests that humans possess a set of basic emotions that are universally recognizable. Paul Ekman's research identified six fundamental emotions: anger, disgust, fear, happiness, sadness, and surprise. Each is associated with distinct facial expressions and physiological patterns [@WikipediaEmotionClassification].

- **Dimensional Models**: These models represent emotions along *continuous* dimensions rather than discrete categories. The *Circumplex Model* is a prominent example, organizing emotions within a circular space defined by two axes: *valence* and *arousal* [@Murphy2024].


## 2.2. Discrete Emotion Theory: Roots, Universality, and Significance

Discrete Emotion Theory posits that humans experience a set of fundamental emotions, each with distinct characteristics and evolutionary purposes. This theory has its roots in Charles Darwin's work on the expression of emotions, where he argued that emotions serve adaptive functions for survival. Paul Ekman's modern research built on this foundation, identifying six core emotions—anger, disgust, fear, happiness, sadness, and surprise—through cross-cultural studies [@WikipediaEmotionClassification].

### 2.2.1. Characteristics of Basic Emotions

Each of the six core emotions has distinguishing features:

- **Anger**: Triggered by perceived threats or injustices, anger is characterized by increased arousal, narrowed attention, and physiological changes such as increased heart rate and adrenaline release.
- **Disgust**: Often a response to contaminants or morally offensive behavior, disgust manifests through a distinctive facial expression involving nose wrinkling and lip curling.
- **Fear**: A reaction to danger or threat, fear prompts the fight-or-flight response, enhancing focus and physiological readiness.
- **Happiness**: Associated with positive experiences and satisfaction, happiness is expressed through smiles and other outward signs of well-being.
- **Sadness**: Elicited by loss or disappointment, sadness is marked by lowered energy and slower cognitive processes.
- **Surprise**: Triggered by unexpected events, surprise is characterized by widened eyes and raised eyebrows, facilitating rapid information processing.

### 2.2.2. Facial Expression Recognition and Universality

Ekman’s studies demonstrated that these emotions are universally recognized through facial expressions, even in cultures isolated from global influences. For instance, widened eyes and raised eyebrows universally signal surprise, while smiles denote happiness. This universality suggests a biological basis for basic emotions, enabling effective nonverbal communication.

### 2.2.3. Evolutionary Significance

Basic emotions play critical roles in survival and social interaction:

- **Survival**: Emotions like fear and anger prepare the body for immediate action.
- **Communication**: Facial expressions convey emotional states, facilitating understanding and cooperation.
- **Social Bonding**: Emotions like happiness and sadness strengthen relationships by eliciting empathy and support.

By providing a structured understanding of emotions, Discrete Emotion Theory lays the groundwork for practical applications such as Facial Expression Recognition (FER), enhancing human-computer interaction and social robotics.

## 2.3. The Circumplex Model: Valence and Arousal

Developed by James Russell, the Circumplex Model (depicted in Figure \ref{fig:circumplex_model}) maps emotions based on two dimensions:

- **Valence**: Represented on the horizontal (X) axis, valence measures the positivity or negativity of an emotion. Positive valence indicates pleasant emotions (e.g., happiness), while negative valence corresponds to unpleasant emotions (e.g., sadness).

- **Arousal**: Represented on the vertical (Y) axis, arousal gauges the intensity or activation level of an emotion, ranging from low (calmness) to high (excitement).

By plotting emotions within this two-dimensional space, the Circumplex Model illustrates how different emotions relate to one another. For instance, emotions like excitement (high arousal, positive valence) and calmness (low arousal, positive valence) are positioned accordingly, highlighting the continuous nature of emotional experiences.

Understanding these models is essential for fields such as Facial Expression Recognition (FER), as they provide frameworks for interpreting and categorizing human emotions based on observable cues.

\begin{figure}
    \centering
    \includegraphics[width=0.5\textwidth]{Resources/Circumplex_model_of_emotion.png}
    \caption{The Circumplex Model of Emotion maps emotions within a two-dimensional space defined by valence (X-axis) and arousal (Y-axis). Positive and negative valence correspond to pleasant and unpleasant emotions, respectively, while arousal indicates emotional intensity. Image taken from \url{en.wikipedia.org/wiki/Emotion_classification}}
    \label{fig:circumplex_model}
\end{figure} 


\newpage

# 3. Facial Expression Recognition (FER)

## 3.1. Datasets

The datasets described here will be referenced later in the Models section to indicate their use in training and evaluating the models. Below is a summary of the datasets:

### 3.1.1. FER2013  
[@FER2013] is a dataset comprising 32,298 grayscale images of faces, each sized 48x48 pixels, labeled with seven emotions: Angry (0), Disgust (1), Fear (2), Happy (3), Sad (4), Surprise (5), and Neutral (6). Images are centered and uniformly scaled. The dataset includes 28,709 training samples and 3,589 test samples, with the task being to classify facial expressions into one of the seven categories.

### 3.1.2. AffectNet  
[@AffectNet] addresses the scarcity of annotated facial expression datasets in the wild, particularly for the **continuous dimensional model** (e.g., valence and arousal) alongside **discrete emotions** (categorical model). It contains over 1 million facial images collected from the internet using 1,250 emotion-related keywords in six languages. Approximately 440,000 images were manually annotated for eight discrete emotions and valence/arousal intensity. The dataset also includes "contempt" as an eighth emotion, making it more comprehensive than FER2013. AffectNet facilitates research in both categorical and dimensional emotion models.

<!-- Migliorare il formato in cui vengono presentati i diversi modelli che non mi piace molto... specialmente in termini grafici nel pdf finale. -->
## 3.2. Models
This section introduces several models for Facial Expression Recognition (FER). Each model is presented with a brief description, the dataset it utilizes (if not otherwise specified, for both training and testing), and its performance metrics on that dataset.

### 3.2.1. DeepFace  
**Description:** DeepFace [@DeepFace], [@serengil2021lightface] is a lightweight Python framework for face recognition and facial attribute analysis, including emotion detection, age, gender, and ethnicity prediction. It integrates various state-of-the-art models such as VGG-Face, FaceNet, and ArcFace.  
**Dataset Used:** FER2013  
**Accuracy:** 57.42%

### 3.2.2. HSEmotionONNX  
**Description:** [@savchenko2023facial], [@savchenko2021facial], [@Savchenko_2022_CVPRW], [@Savchenko_2022_ECCVW], [@savchenko2022classifying] A collection of ONNX-compatible (Open Neural Network Exchange standard) models *pre-trained* for face identification using [VGGFace2](https://github.com/ox-vgg/vgg_face2) (Dataset for Face Recognition) and optimized for emotion recognition on AffectNet.  
**Dataset Used for Fine-Tuning:** AffectNet  
**Accuracy:**  

- enet_b0_8_best_vgaf.pt: 61.32% (8 classes), 64.57% (7 classes)  
- enet_b2_8.pt: 63.03% (8 classes), 66.29% (7 classes)  

**Inference Times:**  

- enet_b0_8_best_vgaf.pt: 59 $\pm$ 26 ms  
- enet_b2_8.pt: 191 $\pm$ 18 ms  

**Model Sizes:**

- enet_b0_8_best_vgaf.pt: 16 MB
- enet_b2_8.pt: 30 MB

The enet_b0_8_best_vgaf model is preferred due to its faster inference time, achieving higher FPS with minimal accuracy trade-offs.

### 3.2.3. Vision Transformer (ViT) for Facial Expression Recognition  
**Description:** [@todor_pakov_2024] A Vision Transformer model fine-tuned (from [vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k)) for emotion recognition on facial images.  
**Dataset Used for Fine-Tuning:** FER2013  
**Accuracy:**  

- Validation Set: 71.13%  
- Test Set: 71.16%  

### 3.2.4. Residual Masking Network (RMN)  
**Description:** RMN [@pham2021facial] leverages Residual Masking Blocks to process facial features across multiple scales, ending with a 7-class softmax for emotion classification.  
**Dataset Used:** FER2013  
**Accuracy:** 74.14%  

### 3.2.5. EmoNet  
**Description:** [@toisoul2021estimation] Trained models available for 5 and 8 emotional classes, also predicting valence, arousal, and facial landmarks.  
**Dataset Used:** AffectNet 

**Accuracy:**  

- 5 Classes: 82%  
- 8 Classes: 75%  

**Face Detection:** Utilizes the SFD detector from the [face-alignment](https://github.com/1adrianb/face-alignment) repository, noted for its high accuracy but slower performance.  


\newpage

# 4. References

<div id="refs"></div>