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

