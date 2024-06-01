"""
Test fixtures for Breast Cancer Prediction API.

This module provides test fixtures for testing the Breast Cancer Prediction API.

Fixtures:
    test_data(): Fixture to load test data.
    client(): Fixture to create a test client for API testing.
"""
from typing import Generator

import pandas as pd
import pytest
from fastapi.testclient import TestClient
from log_reg_model.config.core import config
from log_reg_model.processing.data_manager import load_dataset

from app.main import app


@pytest.fixture(scope="module")
def test_data() -> pd.DataFrame:
    """
    Fixture to load test data.

    Returns:
        pd.DataFrame: The test dataset loaded from a file.
    """
    return load_dataset(file_name=config.app_config.test_data_file)


@pytest.fixture()
def client() -> Generator:
    """
    Fixture to create a test client for API testing.

    Yields:
        TestClient: A test client for interacting with the API.
    """
    with TestClient(app) as _client:
        yield _client
        app.dependency_overrides = {}

