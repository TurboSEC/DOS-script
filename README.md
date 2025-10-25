# DOS-script

A small Python learning tool that demonstrates basic TCP client behavior, thread control, timeouts, and exception handling.  
**Designed for educational use only** — test **only** on machines and networks you own or have explicit permission to test.

## Key Points
- Teaches: `socket`, `threading`, `sendall`, `settimeout`, and exception handling.
- **Do not** use against networks or devices you don't own. Misuse may be illegal.
- Start with `localhost` and very small thread counts while learning.

## Requirements
- Python 3.7+
- No external dependencies

## Quick Start
1. Start a local HTTP server in one terminal:
   ```bash
   python -m http.server 8000
   ```
2. Edit the script to use `TARGET_HOST="127.0.0.1"` and `TARGET_PORT=8000`.
3. Run the client script:
   ```bash
   python safe_test_client.py
   ```

## Configuration
You can adjust the following settings inside the script:
- `TARGET_HOST` / `TARGET_PORT` — target IP and port.
- `MAX_THREADS` — number of threads (start small, e.g., 5).
- `SOCKET_TIMEOUT` — timeout in seconds (e.g., 2.0).

## Troubleshooting
- **ConnectionRefusedError**: Target not listening. Start the server or check IP/port.
- **socket.timeout**: Increase timeout or check connectivity.
- **Slow system**: Reduce `MAX_THREADS`.

## Legal Disclaimer (READ CAREFULLY)
This repository is for **educational purposes only**. Use this code **only** for testing on networks and devices that you **own and control**, or where you have **explicit written permission** to test. Do **not** use this code against third‑party networks, public servers, or devices you do not own. Misuse can cause service disruption and may be illegal.

## License
Free for educational use. Please use responsibly.
