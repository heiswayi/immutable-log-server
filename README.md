# Immutable Log Server

Immutable Log Server is a simple server to store logs in an immutable blockchain. It is built using FastAPI and stores logs in a JSON file.

## Features

- Add logs to the blockchain
- Retrieve all logs
- Validate the integrity of the blockchain
- Health check endpoint

## Project Structure

```
.
├── .dockerignore
├── .flake8
├── .gitignore
├── .vscode/
│   └── settings.json
├── blockchain.py
├── data/
│   ├── .gitkeep
│   └── blockchain.json
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── main.py
├── models.py
├── requirements.txt
└── venv/
```

## Getting Started

### Prerequisites

- Python 3.12
- Docker (optional)

### Installation

1. Clone the repository:

```sh
git clone https://github.com/yourusername/immutable-log-server.git
cd immutable-log-server
```

2. Create a virtual environment and activate it:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

### Running the Server

To run the server locally, use the following command:

```sh
uvicorn main:app --host 0.0.0.0 --port 3000
```

### Using Docker

1. Build the Docker image:

```sh
docker-compose build
```

2. Run the Docker container:

```sh
docker-compose up
```

### API Endpoints

- `GET /healthcheck`: Health check endpoint
- `POST /api/add_log`: Add a log to the blockchain
- `GET /api/get_logs`: Retrieve all logs
- `GET /api/validate_chain`: Validate the integrity of the blockchain

### Example Request

To add a log, send a POST request to `/api/add_log` with the following JSON body:

```json
{
  "message": "This is a log message",
  "metadata": {
    "key": "value"
  }
}
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.