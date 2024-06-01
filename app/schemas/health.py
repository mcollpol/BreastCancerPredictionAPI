"""
Schema for Health information.

This module defines the schema for Health information including project name, API version,
and model version.

Classes:
    Health: Schema for health information.
"""

from pydantic import BaseModel


class Health(BaseModel):
    """
    Schema for health information.

    Attributes:
        name (str): The name of the project.
        api_version (str): The version of the API.
        model_version (str): The version of the model.
    """
    name: str
    api_version: str
    model_version: str
