# GMares escanfile test

This is a simple FastAPI application deployed using Docker. Follow the instructions below to set up and run the application.

## Prerequisites

- Ensure you have [Docker](https://www.docker.com/) installed on your system.
- Clone the repository to your local machine.

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone git@github.com:G9Mares/GMares_prueba_tecnica.git
   cd GMares_prueba_tecnica
   ```

2. **Build the Docker image**
   ```bash
   docker build -t escanapp .
   ```

3. **Run the Docker container**
   ```bash
   docker run -d -p 8000:4000 escanapp
   ```

## Access the Application

- Once the container is running, the FastAPI application will be accessible at: 
  ```
  http://localhost:8000

## Notes

- The application listens on port `4000` inside the container, but it is mapped to port `8000` on the host machine.
- The application binds to `0.0.0.0`, allowing it to be accessible from other devices on the local network.
- Documentation of the API for usage and testing is available in the Postman collection file included in this repository.
