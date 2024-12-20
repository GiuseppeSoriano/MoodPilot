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
- https://github.com/tomas-gajarsky/facetorch
- EmoNet (couldn't find any relevant implementation)