from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/freeze', methods=['POST'])
def freeze():
    data = request.get_json()
    port = data.get("port")
    duration = data.get("duration")

    try:
        subprocess.Popen(["bash", "freeze_network.sh", port, duration])
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
