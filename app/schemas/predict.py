"""
Schema for Breast Cancer Prediction.

This module defines the schema for Breast Cancer Prediction results and input data.

Classes:
    PredictionResults: Schema for prediction results.
    BreastCancerPredictDataInputs: Schema for input data for breast cancer prediction.
"""
from typing import Any, List, Optional

from pydantic import BaseModel
from log_reg_model.processing.validation import DataInputSchema


class PredictionResults(BaseModel):
    """
    Schema for prediction results.

    Attributes:
        errors (Optional[Any]): Any errors encountered during prediction.
        version (str): The version of the model used for prediction.
        predictions (Optional[List[float]]): The predicted values.
    """
    errors: Optional[Any]
    version: str
    predictions: Optional[List[float]]


class BreastCancerPredictDataInputs(BaseModel):
    """
    Schema for input data for breast cancer prediction.

    Attributes:
        inputs (List[DataInputSchema]): List of input data points for prediction.

    Config:
        schema_extra (dict): Extra schema information for documentation purposes.
    """
    inputs: List[DataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "radius_mean": 13.2,
                        "texture_mean": 29.3,
                        "perimeter_mean": 88.1,
                        "area_mean": 500.9,
                        "smoothness_mean": 0.105,
                        "compactness_mean": 0.12,
                        "concavity_mean": 0.15,
                        "concave_points_mean": 0.05,
                        "symmetry_mean": 0.188,
                        "fractal_dimension_mean": 0.0678,
                        "radius_se": 0.395,
                        "texture_se": 0.99,
                        "perimeter_se": 3.05,
                        "area_se": 33.2,
                        "smoothness_se": 0.0056,
                        "compactness_se": 0.0156,
                        "concavity_se": 0.0223,
                        "concave_points_se": 0.015,
                        "symmetry_se": 0.0165,
                        "fractal_dimension_se": 0.0035,
                        "radius_worst": 15.82,
                        "texture_worst": 25.2,
                        "perimeter_worst": 95.05,
                        "area_worst": 691,
                        "smoothness_worst": 0.1567,
                        "compactness_worst": 0.252,
                        "concavity_worst": 0.273,
                        "concave_points_worst": 0.152,
                        "symmetry_worst": 0.38,
                        "fractal_dimension_worst": 0.095,
                    }
                ]
            }
        }
