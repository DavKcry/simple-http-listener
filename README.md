# Simple HTTP Listener for Data Exfiltration

A simple Python script designed to receive and visualize exfiltrated data on port 8000. 

## Overview

This script acts as a lightweight HTTP server, very similar to Python's standard module (`python3 -m http.server`), but optimized for **Capture The Flag (CTF)** challenges and security testing.

Unlike the standard module, which fails to handle data submissions, this script provides:

* ✅ **POST Support:** Accepts and prints data from forms, `fetch`, or `cURL` requests (standard module returns `501 Unsupported method`).
* ✅ **Request Decoding:** Automatically URL-decodes the incoming data for real-time readability.
* ✅ **Lightweight:** Built using only the standard library. No external dependencies or `pip install` required.

## Usage

Simply run the script with Python 3:

```bash
python3 web.py
```

## Disclaimer
This tool has been created solely for educational purposes and for testing in controlled environments (such as CTFs, Bug Bounties, or authorized penetration tests). The author is not responsible for any misuse.