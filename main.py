import threading
from eeg_processor import EEGProcessor
from unity_server import UnitySocketServer

def eeg_processing_loop(eeg_processor, unity_server):
    while True:
        focus = eeg_processor.get_focus_score()
        print(f"[EEG] Focus Score: {focus:.3f}")
        unity_server.send_focus(focus)

if __name__ == '__main__':
    eeg_processor = EEGProcessor()
    unity_server = UnitySocketServer()

    thread = threading.Thread(target=eeg_processing_loop, args=(eeg_processor, unity_server))
    thread.start()
