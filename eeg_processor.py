import numpy as np
from scipy.signal import welch
from eeg_device_api import EEGDevice  # Replace with actual EEG SDK wrapper

class EEGProcessor:
    def __init__(self, device=None):
        self.eeg = device or EEGDevice()
        self.eeg.start_stream()

    def calculate_focus(self, window):
        psd_freqs, psd_vals = welch(window, fs=self.eeg.sampling_rate, nperseg=256)
        beta = np.mean(psd_vals[12:30])
        alpha = np.mean(psd_vals[8:12])
        theta = np.mean(psd_vals[4:8])
        focus_score = beta / (alpha + theta + 1e-6)
        return min(max(focus_score, 0), 1)

    def get_focus_score(self):
        window = self.eeg.get_window(2)  # 2 seconds of EEG data
        return self.calculate_focus(window)
