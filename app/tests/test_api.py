"""
Test module for predicting breast cancer.

This module contains tests for predicting breast cancer using the API endpoint.

Functions:
    test_make_prediction(client: TestClient, test_data: pd.DataFrame) -> None:
        Test function to verify the prediction of breast cancer using the API endpoint.
"""

import math

import numpy as np
import pandas as pd
from fastapi.testclient import TestClient


async def test_make_prediction(client: TestClient, test_data: pd.DataFrame) -> None:
    """
    Test function to verify the prediction of breast cancer using the API endpoint.

    Args:
        client (TestClient): The FastAPI test client.
        test_data (pd.DataFrame): The test dataset.

    Returns:
        None
    """
    # Given
    payload = {
        # ensure pydantic plays well with np.nan
        "inputs": test_data.replace({np.nan: None}).to_dict(orient="records")
    }

    # When
    response = await client.post(
        "http://localhost:8001/api/v1/predict",
        json=payload,
    )

    # Then
    assert response.status_code == 200
    prediction_data = response.json()
    assert prediction_data["predictions"]
    assert prediction_data["errors"] is None
    assert math.isclose(prediction_data["predictions"][0], 113422, rel_tol=100)
