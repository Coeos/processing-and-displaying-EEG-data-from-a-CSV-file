import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

# Function to read EEG data from CSV file
def read_eeg_data(csv_file):
    return pd.read_csv(csv_file)

# Butterworth Filter
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    return lfilter(b, a, data)

# Simple Artifact Rejection
def reject_artifacts(data, threshold=100):
    return data[np.abs(data) < threshold]

# Frequency bands
bands = {
    'Delta': (0.5, 4),
    'Theta': (4, 8),
    'Alpha': (8, 12),
    'Beta': (12, 30),
    'Gamma': (30, 45)
}

# Main execution
csv_file = 'C://Users//eliot//Desktop//CreaTech//EXPETECH//archive//s00.csv'  # Replace with your CSV file path
eeg_data = read_eeg_data(csv_file)
fs = 256  # Sampling frequency

# Plot original data
plt.figure(figsize=(15, 10))
for i, col in enumerate(eeg_data.columns):
    plt.subplot(len(eeg_data.columns), 1, i+1)
    plt.plot(eeg_data[col], label=f'Electrode {col}')
    plt.title(f'Original Data - Electrode {col}')
    plt.legend()
plt.tight_layout()
plt.show()

# Preprocess and plot processed data
plt.figure(figsize=(15, 10))
for band, (lowcut, highcut) in bands.items():
    for i, col in enumerate(eeg_data.columns):
        # Artifact rejection
        clean_data = reject_artifacts(eeg_data[col])

        # Bandpass filter
        filtered_data = butter_bandpass_filter(clean_data, lowcut, highcut, fs, order=6)

        plt.subplot(len(eeg_data.columns), 1, i+1)
        plt.plot(filtered_data, label=f'{band} band - Electrode {col}')
        plt.title(f'{band} Band - Electrode {col}')
        plt.legend()
    plt.tight_layout()
    plt.show()

                        