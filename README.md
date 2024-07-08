# FTI Consulting Sample-backend
The backend application for icognition

# Python Environment & Local Development 
1. Install conda
1. Create conda environment `conda create -n {NAME} python=3.9`
2. Install dependencies `pip install -r requirements.txt`

# Running with Docker
1. Turn on Docker Desktop 
2. Build the Docker Container `docker build -t financial_data_api .`
3. RUn the Docker Contianer `docker run -d -p 8000:8000 financial_data_api`