"""
Schemas for Breast Cancer Prediction.

This module aggregates various schemas used in the Breast Cancer Prediction application.

Modules:
    Health: Schema for health information.
    BreastCancerPredictDataInputs: Schema for input data for breast cancer prediction.
    PredictionResults: Schema for prediction results.
"""
from .health import Health
from .predict import BreastCancerPredictDataInputs, PredictionResults
