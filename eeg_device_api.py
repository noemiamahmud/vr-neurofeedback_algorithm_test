import numpy as np

class EEGDevice:
    def __init__(self):
        self.sampling_rate = 256  # Fake value for testing

    def start_stream(self):
        print("[EEGDevice] Started fake EEG stream")

    def get_window(self, seconds):
        # Simulate brainwave data (random noise)
        return np.random.randn(int(self.sampling_rate * seconds))
