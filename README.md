# Identity Service Provider (IDSP) Project

## Introduction

Welcome to the Identity Service Provider (IDSP) project. This project aims to create a robust and scalable Identity Service Provider tailored for financial services. It focuses on implementing secure user authentication using SAML (Security Assertion Markup Language) and Multi-Factor Authentication (MFA). This project is designed as a learning experience to understand the intricacies of Identity and Access Management (IAM) in an enterprise context.

## Technologies Used

- **Programming Language**: Python 3.12
- **Web Framework**: Django
- **Authentication Protocol**: SAML
- **Multi-Factor Authentication**: Email and Authenticator Apps
- **Database**: PostgreSQL
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Cloud Provider**: AWS (EKS, RDS, IAM, SNS)
- **Linting**: Flake8

## Current Implementation

### Completed

1. **Project Setup**
   - Python and Django installed.
   - Django project and `authentication` app created.

2. **SAML Authentication**
   - `djangosaml2` library installed and configured.
   - SAML settings added to `settings.py`.
   - SAML views and URLs implemented.

3. **Multi-Factor Authentication (MFA)**
   - Basic structure for MFA using email and authenticator apps.
   - Functions for generating and verifying MFA tokens.

4. **Code Quality**
   - Flake8 installed and configured.
   - Pre-commit hooks set up for linting with Flake8.

## TODO

### Short-Term Goals

1. **Database Setup**
   - PostgreSQL to be configured.
   - Database schemas for `Users` and `MFA_Tokens` to be created.

2. **Containerization**
   - Dockerfile for containerizing the Django application.

3. **Complete MFA Integration**
   - Finalize the integration of email and authenticator app MFA.
   - Implement token sending via AWS SNS for email.

4. **Testing**
   - Implement unit and integration tests for SAML and MFA functionalities.
   - Perform end-to-end testing to ensure seamless user authentication flow.

5. **Documentation**
   - Write detailed documentation for setting up and configuring the project.
   - Create user guides for administrators and end-users.

### Medium-Term Goals

1. **Deployment to AWS**
   - Set up AWS EKS cluster.
   - Deploy PostgreSQL using AWS RDS.
   - Configure IAM roles and policies.
   - Deploy the Django application to EKS.

2. **Scalability and Performance**
   - Implement horizontal scaling using Kubernetes.
   - Optimize database queries and application performance.

### Long-Term Goals

1. **Feature Enhancements**
   - Implement OpenID Connect for additional authentication support.
   - Add more MFA methods (e.g., SMS via AWS SNS).

2. **Financial Services Integration**
   - Develop and integrate financial transaction components.
   - Ensure compliance with financial regulations such as PCI-DSS.

3. **Advanced Security Features**
   - Implement advanced security features like anomaly detection and behavioral biometrics.

## Getting Started

### Prerequisites

- Python 3.8+
- Docker
- PostgreSQL
- AWS Account (for deployment)

### Installation

1. **Clone the repository**:

    ```
    git clone git@github.com:palashsarkar18/identity_service_provider_project.git
    cd identity_service_provider_project
    ```

2. **Set up a virtual environment**:

    ```
    python -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```
    pip install -r requirements.txt
    ```

4. **Run database migrations**:
    ```
    python manage.py migrate
    ```

5. **Run the development server**:
    ```
    python manage.py runserver
    ```

### Docker Setup

1. **Build the Docker image**:
    ```
    Describe the steps here
    ```

2. **Run the Docker container**:
    ```
    Describe the steps here.
    ```

### Running Flake8

To enforce coding standards, run Flake8:

    ```
    flake8 .
    ```

