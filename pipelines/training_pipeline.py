from steps.data_ingestion_step import data_ingestion_step
from steps.handle_missing_values_step import handle_missing_values_step
from steps.feature_engineering_step import feature_engineering_step
from steps.outlier_detection_step import outlier_detection_step
from pyprojroot import here
from zenml import Model, pipeline


@pipeline(
    model=Model(
        name="prices_predictor"
    ),
)
def ml_pipeline():
    """Define an end-to-end machine learning pipeline."""
    # Data Ingestion Step
    raw_data = data_ingestion_step(file_path=str(here("data/archive.zip")))

    # Handling Missing Values Step
    filled_dara = handle_missing_values_step(raw_data)

    # Feature Engineering Step
    engineered_data = feature_engineering_step(
        filled_dara, strategy="log", features=["Gr Liv Area", "SalePrice"]
    )

    # Outlier Detection Step
    clean_data = outlier_detection_step(engineered_data, column_name="SalePrice")
