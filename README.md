# Responsible ML Analysis – Recommendation System

## Overview
This project extends a movie recommendation system by incorporating responsible machine learning analysis. The focus is on evaluating fairness, identifying feedback loops, and assessing security risks in a production-style deployment.

## System
- FastAPI-based recommendation API  
- Deployed on Azure Container Apps  
- Docker containerized for consistent deployment  
- Metrics exposed via Prometheus for monitoring  

## Fairness Analysis
During testing, I observed that the system returns identical recommendations for different users, indicating a lack of personalization.

### Key Findings
- Diversity Score = **0.20** (low diversity)  
- Top-5 Exposure Share = **1.0** (high concentration)  
- Same items recommended across all users  

This shows strong **popularity bias** and **unfair exposure distribution**.

## Feedback Loops
Two key feedback loops were identified:

- **Popularity Feedback Loop**  
  Popular items receive more exposure → more interactions → higher ranking → repeated exposure  

- **Tail Starvation**  
  Less popular items receive low exposure → no interaction data → remain unranked  

These loops can reinforce bias over time if not addressed.

## Security Analysis
A basic threat model was evaluated across API and model components.

### Observations
- No abnormal behavior detected during testing (null finding)  
- System handled requests successfully with stable performance  

### Potential Risks
- API abuse (DoS attacks)  
- Data poisoning (rating manipulation)  

### Suggested Mitigations
- Rate limiting  
- Authentication & validation  
- Anomaly detection  

## How to Run Analysis
```bash
python analysis/fairness_analysis.py

Video Demo

https://youtu.be/SVtEY_fNTaQ

Deliverables
Report: report/responsible_ml_report.pdf
Slides: slides/AI and ML product.pptx
Analysis code: analysis/
Telemetry data: telemetry/
Figures: figures/
Summary

From my observation, this system demonstrates how lack of personalization can lead to fairness issues such as popularity bias and exposure imbalance. This project highlights that building effective ML systems requires not only performance but also fairness, robustness, and continuous monitoring.
