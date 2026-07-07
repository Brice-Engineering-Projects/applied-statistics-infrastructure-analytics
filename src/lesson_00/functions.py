

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

def descriptive_statistics(df:pd.DataFrame) -> dict:
    """
    Calculates descriptive statistics for the dataset.

    Args:
       df:
            A pandas DataFrame containing a numeric dataset.

    Raises:
        TypeError:
            If the input is not a Pandas Dataframe
        ValueError:
            If the Pandas DataFrame is empty.

    Returns:
        A dictionary with the following values:
            observations:
                Provides the number of observations in the dataset
            mean
                Arithmetic mean of the data
            median
                The median (middle) value in the dataset
            minimum
                The minimum value in the dataset
            maximum
                The maximum value in the dataset
            range
                The difference between the maximum and minimum.
            variance
                Average of the squared distances of the observations from the mean.
            std_dev
                The standard deviation, which is the square root of the variance.
    """
    # Error handling
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Passed argument must be a Pandas DataFrame.")
    if df.empty:
        raise ValueError("Dataframe must contain values.")

    flow = df["peak_flow_cfs"]
    observations = df.shape[0]
    sample_mean = float(flow.mean())
    sample_median = float(flow.median())
    sample_max = int(flow.max())
    sample_min = int(flow.min())
    sample_range = int(sample_max - sample_min)
    sample_variance = float(flow.var())
    sample_standard_deviation = float(flow.std())

    summary = {
        "observations": observations,
        "sample_mean": sample_mean,
        "sample_median": sample_median,
        "sample_max": sample_max,
        "sample_min": sample_min,
        "sample_range": sample_range,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
    }

    return summary
