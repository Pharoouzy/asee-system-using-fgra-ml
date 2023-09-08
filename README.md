# Agile Software Effort Estimation System (ASEE System)

[![Agile Software Effort Estimation System CI](https://github.com/Pharoouzy/msc-dissertation/actions/workflows/main.yaml/badge.svg?branch=master)](https://github.com/Pharoouzy/msc-dissertation/actions/workflows/main.yaml)

## Overview
The Agile Software Effort Estimation System is a sophisticated, data-driven solution tailored to predict the effort required for software tasks within an Agile environment. By harnessing the power of machine learning and incorporating techniques like Fuzzy Grey Relational Analysis (FGRA) for feature selection, this system offers both accuracy and efficiency in project estimations. Its integration with FastAPI and Jupyter notebooks ensures interactive engagement, enabling users to intuitively assess and fine-tune their estimations.

## Key Features

- **Fuzzy Grey Relational Analysis (FGRA)**: At the heart of the feature selection process, FGRA prioritizes and selects the most significant features from the dataset. By accounting for uncertainty and vagueness using fuzzy logic, it offers a robust method to identify the vital predictors for effort estimation, ensuring model accuracy.

- **Historical Data Processing**: The system uses past project data to make its predictions. This raw data is rigorously cleaned, preprocessed, and then fed into the modeling process.

- **Modeling & Evaluation**: Multiple Machine Learning algorithms are used to train models for estimating the software effort. These models are rigorously evaluated to ensure they deliver high accuracy and reliability.

- **API**: The integrated FastAPI interface allows users to interact with the system seamlessly, offering real-time effort estimates based on the refined model.

- **Interactive Notebooks**: Jupyter notebooks in the repository facilitate deeper data analysis, model understanding, and evaluation, allowing users to get an in-depth view of the underlying processes.

- **Docker Integration**: With Docker configurations in place, the system promises consistent performance across various environments, simplifying deployments and setups.


## Project Structure

Here is a brief overview of the project's directory structure:

- **`.github/`**: Configuration and scripts for GitHub actions.
  - **`workflow/`**: Contains GitHub action workflows like `main.yaml`.
 
- **`artifacts/`**: Holds trained machine learning models.
  - **`models/`**: Contains serialized models saved using `joblib`.
 
- **`data/`**: Contains all project data, both raw and processed. 
  - **`raw/`**: Raw data in its initial state.
  - **`processed/`**: Data that has been cleaned or transformed.

- **`docs/`**: Configuration and scripts for GitHub actions.
  - **`setip[/`**: Contains GitHub action workflows like `main.yaml`.
  
- **`notebooks/`**: Contains Jupyter notebooks for tasks like data exploration, data preprocessing, and model training.

- **`docker/`**: Files related to Docker configurations.
  - **`images/`**: Contains Dockerfiles for various services.
    - **`app/`**: Dockerfile for the main application.
    - **`fastapi/`**: Dockerfile for FastAPI service.
    - **`jupyter/`**: Dockerfile for Jupyter notebook service.
  - **`docker-compose.yaml`**: Docker Compose configuration file.
  - **`up.sh`**: Script to start Docker containers.
  - **`down.sh`**: Script to stop Docker containers.
  - **`ssh.sh`**: Script to SSH into the FastAPI container.

- **`src/`**: Holds the main source code for the project.
  - **`data/`**: Code for data operations.
  - **`features/`**: Code for extracting features from the data.
  - **`models/`**: Code for training and evaluating machine learning models.
  - **`api/`**: FastAPI application code.
  - **`utils/`**: Contains utility code for various project operations.
  - **`tests/`**: Test modules to ensure code functionality.

- **`configs/`**: Configuration files, such as `model_config.yaml` and `general_config.yaml`, that are used throughout the project.

- **`reports/`**: Stores generated figures, presentations, or academic papers.
  - **`figures/`**: Graphs, plots, and other visuals.
  - **`presentations/`**: Slides and related content for project presentations.
  - **`papers/`**: Academic and research papers related to the project.

- **`.dockerignore`**: Lists files/folders Docker should ignore.
  
- **`.gitignore`**: Lists files/folders Git should ignore.

- **`.env.examples`**: Template for environment variables. Rename to `.env` and fill in necessary details.

- **`requirements.txt`**: Contains required Python libraries for the project.

- **`LICENSE`**: License details of the project.

- **`README.md`**: Provides an overview of the project and setup instructions.


## Getting Started
A comprehensive setup guide, both manual and dockerized, is provided below. It walks users through the setup process, from cloning the repository to running the FastAPI and Jupyter servers.

## Prerequisites

1. Python 3.x
2. Jupyter
3. MySQL
4. Docker (Optional, but recommended for hassle-free setup)

## Setup

### Step 1. Clone the Repository
To get started, first clone the project to your local machine
```bash
git clone git@github.com:Pharoouzy/asee-system-using-fgra-ml.git asee_system
cd asee_system
```

### Step 2. Database Configuration
The dataset is stored as a relational database, dumped from MySQL. To start using the dataset, follow the instruction below:

- **Step 1**: Install MySQL database management system.

- **Step 2**: Download and unzip the dataset (.sql file) from [here](https://rdr.ucl.ac.uk/articles/dataset/The_TAWOS_dataset/21308124).

- **Step 3**: Setup the database using the downloaded file:

```bash
mysql -u [user] -p [database_name] < [filename].sql
```

- **Step 4**: Configure your database settings. Rename `.env.examples` to `.env` and update the database credentials

```bash
MYSQL_USERNAME=<your_username>
MYSQL_PASSWORD=<your_password>
MYSQL_HOST=<your_host>
MYSQL_DATABASE=<your_database_name>
```
> **Important**: It is crucial to set these details correctly before running the project as the app ingests data from the database for initialization.

### Step 3. Manual Setup

1. Install the necessary packages

```bash
pip install -r requirements.txt
```

2. Run FastAPI

```bash
# Navigate to src/api and run the FastAPI server
cd src/api
uvicorn main:app --reload
```
The API should now be running at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

The API documentation can be accessed via [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

3. Run Jupyter server

```bash
jupyter notebook --notebook-dir notebooks/
```

You can access the Jupyter notebook server at [http://127.0.0.1:8888/](http://127.0.0.1:8888/)

### Docker Setup (Optional)

1. Navigate to the Docker directory

```bash
cd asee_system/docker
```

2. Spin up the Docker services

```bash
./up.sh
```

3. If you need to access the API console

```bash
./ssh.sh
```

4. To stop the Docker services

```bash
./down.sh
```

### Access

- FastAPI can be accessed at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- API documentation can be accessed at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Jupyter notebook can be accessed at [http://127.0.0.1:8888/](http://127.0.0.1:8888/)
