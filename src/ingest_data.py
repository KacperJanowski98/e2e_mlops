import os
import zipfile
from abc import ABC, abstractmethod
from pyprojroot import here

import pandas as pd


class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, path: str) -> pd.DataFrame:
        """Abstract method to ingest data from a given file."""
        pass


class ZipDataIngestor(DataIngestor):
    def ingest(self, path: str) -> pd.DataFrame:
        """Extracts a zip file and returns the contents as a DataFrame."""
        if not path.endswith(".zip"):
            raise ValueError("File is not a zip file.")
        
        with zipfile.ZipFile(path, "r") as zip_file:
            zip_file.extractall("extracted_data")

        extracted_files = os.listdir("extracted_data")
        csv_files = [file for file in extracted_files if file.endswith(".csv")]

        if len(csv_files) == 0:
            raise FileNotFoundError("No CSV files found in the extracted zip file.")
        if len(csv_files) > 1:
            raise ValueError(
                "Multiple CSV files found in the extracted zip file. Please specify which file to use."
            )

        csv_file_path = os.path.join("extracted_data", csv_files[0])
        df = pd.read_csv(csv_file_path)

        return df
    

class DataIngestorFactory:
    @staticmethod
    def get_ingestor(file_extension: str) -> DataIngestor:
        if file_extension == ".zip":
            return ZipDataIngestor()
        else:
            raise ValueError(f"Unsupported file type: {file_extension}")


# Example usage:
if __name__ == "__main__":
    file = here("data/archive.zip")
    # # Determine the file extension
    file_extension = os.path.splitext(file)[1]
    print(file_extension)
    # # Get the appropriate DataIngestor
    data_ingestor = DataIngestorFactory.get_ingestor(file_extension)
    # # Ingest the data and load it into a DataFrame
    df = data_ingestor.ingest(str(file))
    # # Now df contains the DataFrame from the extracted CSV
    print(df.head())  # Display the first few rows of the DataFrame
    # pass
