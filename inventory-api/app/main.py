from flask import Flask, jsonify

app = Flask(__name__)

# Data structure resembling a DB
servers = [
    {"id": 1, "hostname": "web-prod-01", "ip": "10.0.0.1", "status": "up"},
    {"id": 2, "hostname": "db-prod-01", "ip": "10.0.0.2", "status": "down"}
]

@app.route('/api/v1/health', methods=['GET'])
def health_check():
    return jsonify({"status": "OK", "version": "1.0"})

@app.route('/api/v1/servers', methods=['GET'])
def list_servers():
    return jsonify({"servers": servers, "count": len(servers)})

@app.route('/api/v1/servers/<int:server_id>', methods=['GET'])
def get_server(server_id):
    server = next((s for s in servers if s["id"] == server_id), None)
    if server:
        return jsonify(server)
    return jsonify({"error": "Server not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
