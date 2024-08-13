# Organism Simulation Application

## Overview

This application simulates biological processes using Django, Celery, and Redis. It includes Docker and Ansible setups for deployment and configuration.


organism-simulation/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── ansible/
│   ├── playbook.yml
│   └── inventory
├── manage.py
├── simulation/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── app/
│   ├── migrations/
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── tests.py
│   └── ...
└── README.md


## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Ansible

### Setup

1. **Clone the Repository**

    ```bash
    git clone <your-repo-url>
    cd organism-simulation
    ```

2. **Build and Start Services**

    ```bash
    docker-compose up --build
    ```

3. **Run Ansible Playbook**

    The Ansible playbook is automatically run by the `ansible` service in Docker Compose. You can manually trigger it if needed:

    ```bash
    docker-compose run ansible
    ```

### Configuration

- **Database**: Configured in `docker-compose.yml`
- **Django Settings**: Modify `your_project_name/settings.py`
- **Celery**: Configured with Redis as the broker

### Testing

- Access the application at `http://localhost:8000`
- The Celery worker logs can be seen using `docker-compose logs celery`
- The Celery beat logs can be seen using `docker-compose logs celery-beat`

## Deployment

For deployment, ensure all configurations are set in `docker-compose.yml`, and use Docker and Ansible as described.

## License

This project is licensed under the MIT License.
