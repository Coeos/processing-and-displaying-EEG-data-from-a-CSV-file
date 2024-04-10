
# EEG Data Analysis Script

This script analyzes EEG data, providing functionalities for filtering, artifact rejection, and visualization. It uses Pandas, NumPy, Matplotlib, and SciPy for data manipulation and plotting.

## Prerequisites

- Python 3.11
- pandas
- numpy
- matplotlib
- scipy

## Installation

Install the required libraries using pip:

```
pip install pandas numpy matplotlib scipy
```

## Usage

1. Update the `csv_file` variable in the script to the path of your EEG data CSV.
2. Run the script with Python:

## Features

- **Read EEG Data:** Load EEG data from a CSV file.
- **Butterworth Bandpass Filter:** Apply a bandpass filter to isolate specific frequency bands.
- **Reject Artifacts:** Remove artifacts based on amplitude threshold.
- **Visualize Data:** Plot original and processed EEG data for each electrode.
