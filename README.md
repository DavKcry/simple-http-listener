# Simple HTTP GET/POST Listener for Data Exfiltration

A simple Python script designed to receive and visualize exfiltrated data on port 8000 by default. 

## Overview

This script acts as a lightweight HTTP server, very similar to Python's standard module (python3 -m http.server), but optimized for CTFs and pentesting.

Unlike the standard module, this script provides:

* **POST Support:** Accepts and prints data from forms, fetch, or curl requests.
* **Request Decoding:** Automatically URL-decodes the incoming data.

Optionally, you can pick the port you want to listen.

## Usage

```bash
python3 web.py [port]
```

## Examples
```bash
python3 web # Listen on port 8000
python3 web 4455 # Listen on port 4455
```

## Disclaimer
Only for educational purpose and authorized testing.
