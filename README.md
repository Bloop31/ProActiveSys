# ProActiveSys

**AI-Driven System Failure Prediction Platform**

ProActiveSys is an intelligent system monitoring platform that predicts potential system failures before crashes occur by learning normal OS and network behavior from system telemetry.

## Features

- Real-time monitoring of system resources
- Anomaly detection using Isolation Forest
- Detection of abnormal CPU, memory, disk, and network activity
- Root cause identification for potential system failures
- Time-series storage of system telemetry

## Tech Stack

Python, Machine Learning (Isolation Forest), SQLite, Operating System Metrics, Network Telemetry, Time-Series Analysis

## How It Works

1. System metrics such as CPU, memory, disk I/O, and network usage are continuously collected.
2. Telemetry data is stored as time-series data in SQLite.
3. An Isolation Forest model learns normal system behavior.
4. Detected anomalies trigger root cause analysis to identify possible failure sources.

## Future Improvements

- Real-time monitoring dashboard
- Support for distributed systems
- Advanced anomaly detection models
