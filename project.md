---
slug: github-flask-test
id: github-flask-test
title: Flask RESTful API for Weather Data Management
repo: justin-napolitano/flask_test
githubUrl: https://github.com/justin-napolitano/flask_test
generatedAt: '2025-11-24T21:34:47.034Z'
source: github-auto
summary: >-
  Explore a minimal Flask-based API for ingesting and updating weather data,
  featuring Docker support and data processing with pandas.
tags:
  - flask
  - rest api
  - docker
  - pandas
  - google cloud bigquery
  - python
  - gunicorn
  - weather data
  - bigquery
seoPrimaryKeyword: flask weather data api
seoSecondaryKeywords:
  - flask rest api example
  - dockerize flask app
  - weather data ingestion
  - pandas data processing
  - gunicorn deployment
  - google cloud bigquery integration
seoOptimized: true
topicFamily: null
topicFamilyConfidence: null
kind: project
entryLayout: project
showInProjects: true
showInNotes: false
showInWriting: false
showInLogs: false
---

A minimal Flask-based RESTful API service designed to ingest and update weather data. This project provides an endpoint to receive weather parameters and store or process them, with supporting scripts for data streaming and Docker containerization.

## Features

- REST API endpoint `/weather` accepting GET requests with weather data parameters.
- Data parsing and type conversion using pandas.
- Dockerfile for containerized deployment using Gunicorn as the WSGI server.
- A separate Python script for streaming weather data from an external API.

## Tech Stack

- Python 3.9
- Flask
- pandas
- Gunicorn
- Docker
- Google Cloud BigQuery (implied by imports, though usage details are partial)

## Getting Started

### Prerequisites

- Docker (optional, for containerized deployment)
- Python 3.9 environment

### Installation

Clone the repository:

```bash
git clone https://github.com/justin-napolitano/flask_test.git
cd flask_test
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Running Locally

Run the Flask app directly:

```bash
python main.py
```

The API will be available at `http://localhost:5000/weather`.

### Running with Docker

Build the Docker image:

```bash
docker build -t flask_test .
```

Run the container:

```bash
docker run -p 8080:8080 flask_test
```

The API will be available at `http://localhost:8080/weather`.

## Project Structure

- `Dockerfile`: Defines the container image setup using Python 3.9 slim and Gunicorn.
- `main.py`: Flask app with `/weather` GET endpoint to receive and process weather data.
- `requirements.txt`: Python dependencies.
- `restful_api.ipynb`: (Not described, assumed to be a Jupyter notebook related to the API.)
- `weather_data_stream.py`: Script to fetch weather data from an external API, process it, and presumably send updates to the Flask service.

## Future Work / Roadmap

- Complete and document integration with Google Cloud BigQuery for data storage.
- Add POST method support for more secure and flexible data submission.
- Implement authentication and validation on API endpoints.
- Expand `weather_data_stream.py` to automate periodic data fetching and updating.
- Add error handling and logging for robustness.
- Document `restful_api.ipynb` usage and purpose.
- Container orchestration and deployment automation.

---

*Note: Some functionality and integration details are inferred based on partial code snippets and imports.*
