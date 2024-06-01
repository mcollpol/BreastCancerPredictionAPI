This app uses the package built in [BreastCancerPrediction repo](https://github.com/mcollpol/BreastCancerPrediction/tree/master/production) to deploy the Machine Learning model via REST API (FastAPI).

# Using Tox

Tox is a tool for automating and managing testing environments in Python projects. It helps ensure consistent behavior across different Python versions and environments.

## Prerequisites

Make sure you have Python and Tox installed on your system. You can install Tox using pip:

```bash
pip install tox
```
Note: Expected Tox version 4.

## Usage

### Run the app

To run the app, use the following command:
```bash
tox run -e run
```
This command will use Uvicorn to start the app in hhtp//:localhost:8001 from where you can modify the values for the different parameters described in [Breast Cancer Prediction dataset](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data), to predict the expected diagnosis. 

Predictions:
- 0 -> Benign
- 1 -> Malignant

The expected results: 

![image](https://github.com/mcollpol/BreastCancerPredictionAPI/assets/159550482/fb672138-049d-4e3e-83b4-803d123eb9ba)

![image](https://github.com/mcollpol/BreastCancerPredictionAPI/assets/159550482/3923accd-6960-4c42-b279-6b5321dff768)


### Running Tests

To run unit tests and code quality checks, use the following command:

```bash
tox -e test_app
```

For checking only code quality, use the following command:

```bash
tox -e checks
```
