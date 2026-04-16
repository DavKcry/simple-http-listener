# Simple HTTP GET/POST Listener for Data Exfiltration

A simple Python script designed to receive and visualize exfiltrated data on port 8000. 

## Overview

This script acts as a lightweight HTTP server, very similar to Python's standard module (python3 -m http.server), but optimized for CTFs and pentesting.

Unlike the standard module, this script provides:

* **POST Support:** Accepts and prints data from forms, fetch, or curl requests.
* **Request Decoding:** Automatically URL-decodes the incoming data for real-time readability.

## Usage

```bash
python3 web.py
```

## Disclaimer
Only for educational purpose and authorized testing.
