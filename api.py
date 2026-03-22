from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

GITHUB_API_URL = "https://api.github.com/users/{}/gists"

@app.route('/<username>', methods=['GET'])
def get_user_gists(username):
    """
    Fetch and return all public gists for a given GitHub username
    """
    try:
        # Make request to GitHub API
        response = requests.get(GITHUB_API_URL.format(username))
        
        # Check if user exists
        if response.status_code == 404:
            return jsonify({
                'error': f'User "{username}" not found on GitHub'
            }), 404
        
        # Check for other API errors
        if response.status_code != 200:
            return jsonify({
                'error': f'GitHub API error: {response.status_code}'
            }), response.status_code
        
        # Parse the JSON response
        gists = response.json()
        
        # If user has no gists
        if not gists:
            return jsonify({
                'message': f'User "{username}" has no public gists',
                'gists': []
            }), 200
        
        # Format the gist data for better readability
        formatted_gists = []
        for gist in gists:
            formatted_gists.append({
                'id': gist['id'],
                'description': gist['description'] or '(no description)',
                'url': gist['html_url'],
                'created_at': gist['created_at'],
                'updated_at': gist['updated_at'],
                'files': list(gist['files'].keys())
            })
        
        return jsonify({
            'username': username,
            'gist_count': len(formatted_gists),
            'gists': formatted_gists
        }), 200
        
    except requests.exceptions.RequestException as e:
        return jsonify({
            'error': f'Error connecting to GitHub API: {str(e)}'
        }), 503

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for container orchestration"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
