🚀 ETL E-commerce Data Pipeline

Production-like ETL pipeline built with Python, Pandas, and PostgreSQL. 
Simulates real-world data engineering workflows with modular architecture and DAG-style orchestration.


## Badges
Python
Docker
PostgreSQL
ETL Pipeline
## Features
- Modular ETL architecture
- DAG-style pipeline execution
- Data transformation with Pandas
- PostgreSQL integration (Docker)
- Scalable project structure
## Tech Stack
Python
Pandas
SQLAlchemy
PostgreSQL
Docker
## Project Structure
```bash
etl/
├── generate_data.py
├── transform_data.py
├── load_data.py
├── run_pipeline.py

dags/
├── etl_pipeline.py

database/
├── .gitkeep

docker-compose.yml
requirements.txt
README.md

``` 
## Getting Started
pip install -r requirements.txt
python -m dags.etl_pipeline
## Usage
Pipeline runs ETL process:
1. Generate data
2. Transform data
3. Save results
## Future Improvements
- Add Apache Airflow
- Add logging
- Add tests
- CI/CD integration