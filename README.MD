Gist API Server
A simple HTTP web server that interacts with the GitHub API to fetch and display a user's public gists. Built with Flask and containerized with Docker.

📋 Prerequisites
Docker installed on your system

Python 3.9+ (for local development)

curl (for testing the API)

jq (optional, for pretty-printed JSON)

🚀 Quick Start with Docker
1. Clone and Setup



```git clone https://github.com/abhijeetnikam1995/equalexperts-assignment.git ```

move into the folder "equalexperts-assignment"

```cd equalexperts-assignment```

2. Build the Docker Image

```docker build -t gist-api .```

3. Run the Container

```docker run -d \
  --name gist-api \
  -p 8080:8080 \
  --restart unless-stopped \
  gist-api```

4. Verify it's Running
# Check if container is running

```docker ps```

# View container logs
```docker logs gist-api```
5. Test the API

# Basic test with curl
```curl http://localhost:8080/octocat```

# Pretty-printed output (requires jq)
```curl http://localhost:8080/octocat | jq .```

# Test health endpoint
```curl http://localhost:8080/health```

# Test error handling (non-existent user)
```curl http://localhost:8080/nonexistentuser```
🧪 Testing
Using the Test Script

# Create and activate a virtual environment
```python3 -m venv venv```

```source venv/bin/activate```  # On Windows: venv\Scripts\activate

# Install test dependencies
```pip install pytest requests```

# Run the test script
```python3 test_it.py```

Expected output:

text
Waiting for API to be ready...
✅ Health check passed

Testing /octocat endpoint...
✅ API returned 200 OK
   Username: octocat
   Gist count: 8
   First gist: Hello world!

Testing error handling...
✅ Correctly returned 404 for non-existent user
Sample API Response
json
{
  "username": "octocat",
  "gist_count": 8,
  "gists": [
    {
      "id": "aa5a315d61ae9438b18d",
      "description": "Hello world!",
      "url": "https://gist.github.com/aa5a315d61ae9438b18d",
      "created_at": "2024-01-15T12:00:00Z",
      "updated_at": "2024-01-15T12:00:00Z",
      "files": ["hello.py", "hello.js"]
    }
  ]
}
📁 Project Structure
text
newenv/
├── app.py          # Main Flask application
├── test_it.py      # Test script
├── Dockerfile      # Docker configuration
├── requirements.txt # Python dependencies
└── README.md       # This file

