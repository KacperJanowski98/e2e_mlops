from steps.data_ingestion_step import data_ingestion_step
from steps.handle_missing_values_step import handle_missing_values_step
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
    raw_data = data_ingestion_step(file_path=here("data/archive.zip"))

    # Handling Missing Values Step
    filled_dara = handle_missing_values_step(raw_data)
