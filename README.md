# Python_project_1

![Python](https://img.shields.io/badge/Python-3.8-blue.svg)
![Flask](https://img.shields.io/badge/Flask-1.1.2-green.svg)
![Docker](https://img.shields.io/badge/Docker-ready-blue.svg)

## 📋 Description

**Python_project_1** — This is a simple Flask web application designed to demo a CI/CD pipeline using Docker and Jenkins.
This project can be used as a template to customize your own applications with continuous delivery and deployment integration.

## 🚀 Start of work

### 1. Clone the repository

```bash
git clone https://github.com/YanaDevOps/Python_project_1.git
cd Python_project_1
```

### 2. Launching an application in Docker
```bash
docker-compose up --build
```

### 3. Access to the application
Open your browser and go to:
```bash
http://localhost:5000
```

## 📂 Project structure
```bash
Python_project_1/
├── Dockerfile
├── docker-compose.yml
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── style.css
```

Dockerfile: Configuration file for creating a Docker image.
docker-compose.yml: The file for orchestration of Docker containers.
app.py: The main Flask application file.
requirements.txt: A file containing Python dependencies.
README.md: Project documentation.

## 🌟 Functionality
A simple web application that returns a message on the home page.
Sample project to demonstrate CI/CD process using Jenkins and Docker.

## 💻 Technology
Python 3.8
Flask 1.1.2
Docker

## 👤 Author
Name: Yana Lysenko
GitHub: YanaDevOps
