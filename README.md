# Shadow Toolkit: Week 1 Security Suite

A modular, professional-grade security reconnaissance toolkit developed in Python. This project was built to demonstrate core competencies in network protocols, web architecture, and defensive security analysis as part of my **Security Testing Portfolio**.

## 🛠 Features

The toolkit provides a unified command-line interface (CLI) to access three distinct security modules:

* **TCP Port Scanner:** Identifies open services on a target host using socket-level connection attempts. Supports both single ports and custom ranges.
* **HTTP Header Analyzer:** Fingerprints web servers and identifies critical security gaps by checking for missing headers like `CSP`, `X-Frame-Options`, and `HSTS`.
* **Web Link Crawler:** Automates the mapping of a target's attack surface by extracting links and flagging sensitive paths like `/admin`, `/login`, or `/config`.

## 🏗 Project Architecture

The toolkit is built with modularity in mind, allowing each component to be used as a standalone script or imported as a module into the main manager.

```text
fuzzing-portfolio/
├── shadow.py           # Master CLI Entry Point
├── src/                # Source Logic
│   ├── scanner.py      # TCP Scanning Logic
│   ├── headers.py      # Header Analysis Logic
│   ├── crawler.py      # Web Crawling Logic
│   └── util.py         # Shared Utility Functions (Parsing/Validation)
└── Shadow_toolkit.log  # Automated Session Logging
