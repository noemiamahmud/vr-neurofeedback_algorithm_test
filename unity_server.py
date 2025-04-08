import socket
import threading

class UnitySocketServer:
    def __init__(self, host='localhost', port=9999):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(1)
        print(f"[UnitySocketServer] Waiting for Unity to connect on {host}:{port}...")
        self.client, addr = self.sock.accept()
        print(f"[UnitySocketServer] Unity connected from {addr}")

    def send_focus(self, focus_score):
        try:
            msg = f"{focus_score:.3f}\n".encode('utf-8')
            self.client.sendall(msg)
        except (BrokenPipeError, ConnectionResetError):
            print("[UnitySocketServer] Lost connection to Unity.")
