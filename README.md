# AI Real-Time BigQuery Pipeline

## Overview

Production-style real-time data engineering project using:
- GCP Pub/Sub
- BigQuery
- Apache Airflow
- Python
- OpenAI API
- Docker

This pipeline streams events in real time, enriches them using an AI agent, validates data quality, and stores the results in BigQuery.

## Architecture

Producer -> Pub/Sub -> Consumer -> AI Agent -> BigQuery

## Features

- Real-time streaming ingestion
- AI-powered enrichment
- BigQuery streaming inserts
- Airflow orchestration
- Dockerized services
- Data validation

## Setup

```bash
pip install -r requirements.txt
```

```bash
gcloud auth application-default login
```

Run producer:
```bash
python producer/producer.py
```

Run consumer:
```bash
python consumer/consumer.py
```
