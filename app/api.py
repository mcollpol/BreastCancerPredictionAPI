"""
API routes for the Breast Cancer Prediction application.

This module defines API routes for health check and prediction endpoints
for the Breast Cancer Prediction application.

Functions:
    health(): Endpoint for health check.
    predict(input_data: schemas.BreastCancerPredictDataInputs): Endpoint for making
    breast cancer predictions.
"""
import json
from typing import Any

import numpy as np
import pandas as pd
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from log_reg_model import __version__ as ml_model_version
from log_reg_model.predict import make_prediction
from loguru import logger

from app import __version__, schemas
from app.config import settings

api_router = APIRouter()


@api_router.get("/health", response_model=schemas.Health, status_code=200)
def health() -> dict:
    """
    Endpoint for health check.

    Returns:
        dict: A dictionary containing health information including project name, API version,
            and model version.
    """
    health_schemas = schemas.Health(
        name=settings.PROJECT_NAME,
        api_version=__version__,
        ml_model_version=ml_model_version,
    )

    return health_schemas.dict()


@api_router.post("/predict", response_model=schemas.PredictionResults, status_code=200)
def predict(input_data: schemas.BreastCancerPredictDataInputs) -> Any:
    """
    Endpoint for making breast cancer predictions.

    Args:
        input_data (schemas.BreastCancerPredictDataInputs): Input data for making predictions.

    Returns:
        Any: Results of the prediction including predictions, version information,
        and any errors encountered.
    """
    input_df = pd.DataFrame(jsonable_encoder(input_data.inputs))

    logger.info(f"Making prediction on inputs: {input_data.inputs}")
    results = make_prediction(input_data=input_df.replace({np.nan: None}))

    if results["errors"] is not None:
        logger.warning(f"Prediction validation error: {results.get('errors')}")
        raise HTTPException(status_code=400, detail=json.loads(results["errors"]))

    logger.info(f"Prediction results: {results.get('predictions')}")
    logger.info(f"Predictions type: {type(results.get('predictions'))}")
    return results
