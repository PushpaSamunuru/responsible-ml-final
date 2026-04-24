# Responsible ML Analysis – Recommendation System

## Overview
This project extends a movie recommendation system by incorporating responsible ML analysis, including fairness evaluation, feedback loop detection, and security analysis.

## System
- FastAPI-based recommendation API
- Deployed on Azure Container Apps
- Docker containerized
- Metrics exposed via Prometheus

## Fairness
- Identified popularity bias and low personalization
- Measured:
  - Diversity Score = 0.20
  - Top-5 Exposure Share = 1.0
- Found identical recommendations across users

## Feedback Loops
- Popularity feedback loop identified
- Tail starvation observed

## Security
- Threat model defined (API + model)
- No attacks detected (null finding)
- Suggested mitigations:
  - rate limiting
  - anomaly detection
  - validation

## How to Run Analysis
```bash
python analysis/fairness_analysis.py