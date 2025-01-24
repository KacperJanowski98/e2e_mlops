from steps.data_ingestion_step import data_ingestion_step
from pyprojroot import here
from zenml import Model, pipeline, step


@pipeline(
    model=Model(
        name="prices_predictor"
    ),
)
def ml_pipeline():
    """Define an end-to-end machine learning pipeline."""
    # Data Ingestion Step
    raw_data = data_ingestion_step(file_path=here("data/archive.zip"))
