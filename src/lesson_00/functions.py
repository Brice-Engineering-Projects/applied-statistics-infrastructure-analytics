

import pandas as pd
import numpy as np
from pathlib import Path

# ============================
# Define dataset path
# ===========================

data = "../../data/raw/annual_peak_flow.csv"

# ============================
# Load Dataset
# ============================

def load_data(data: str | Path) -> pd.DataFrame:
    """
    Load a CSV dataset into a pandas DataFrame.

    Args:
        data:
            Path to a CSV file.

    Returns:
        A pandas DataFrame.

    Raises:
        TypeError:
            If data is not a string or pathlib.Path.
        FileNotFoundError:
            If the dataset cannot be found.
        ValueError:
            If the file is not a CSV or the dataset is empty.
    """

    # Error Handling
    if not isinstance(data, (str, Path)):
        raise TypeError(
            "data must be a string or pathlib.Path object."
        )

    data = Path(data)

    if data.suffix.lower() != ".csv":
        raise ValueError(
            "Dataset must be a CSV file."
        )

    if not data.exists():
        raise FileNotFoundError(
            f"Dataset not found: {data}"
        )

    # Define dataset read
    dataset = pd.read_csv(data)

    # Validate dataset is not empty
    if dataset.empty:
        raise ValueError(
            "Dataset contains no rows."
        )

    print("Dataset has been loaded as a Pandas Dataframe")

    return dataset
