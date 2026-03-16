import requests
import time
import sys

def test_docker_api():
    """Test the API running in Docker container"""
    
    base_url = "http://localhost:8080"
    
    # Wait for container to be ready
    print("Waiting for API to be ready...")
    time.sleep(2)
    
    # Test health endpoint
    try:
        health_response = requests.get(f"{base_url}/health")
        if health_response.status_code == 200:
            print("✅ Health check passed")
        else:
            print("❌ Health check failed")
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Is the container running?")
        sys.exit(1)
    
    # Test octocat endpoint
    print("\nTesting /octocat endpoint...")
    response = requests.get(f"{base_url}/octocat")
    
    if response.status_code == 200:
        data = response.json()
        print(f"✅ API returned 200 OK")
        print(f"   Username: {data['username']}")
        print(f"   Gist count: {data['gist_count']}")
        
        if data['gists']:
            print(f"   First gist: {data['gists'][0]['description']}")
    else:
        print(f"❌ API returned {response.status_code}")
    
    # Test non-existent user
    print("\nTesting error handling...")
    response = requests.get(f"{base_url}/nonexistentuser12345")
    if response.status_code == 404:
        print("✅ Correctly returned 404 for non-existent user")
    else:
        print(f"❌ Expected 404, got {response.status_code}")

if __name__ == "__main__":
    test_docker_api()
