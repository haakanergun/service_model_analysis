# Service Model Analysis

This repository provides basic utilities for analyzing service model data.

## Features
- Define `ServiceRecord` dataclass to store service information.
- Calculate average service duration using `average_duration`.

## Installation

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage
```python
from service_model_analysis.analysis import ServiceRecord, average_duration

records = [ServiceRecord(service_id=1, duration_minutes=30), ServiceRecord(service_id=2, duration_minutes=45)]
print(average_duration(records))  # Output: 37.5
```

## Demo Web Application

A simple Flask application is provided for demonstration purposes. Run it with:

```bash
python -m service_model_analysis.app
```

It exposes two routes:
- `/` shows a welcome page.
- `/analyze` returns a JSON payload with a placeholder root cause analysis.
