import os
from flask import Flask, request, jsonify
from summarize import classify_topic, generate_summary

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    content = data.get("content", "")

    if not content:
        return jsonify({"error": "Content is required"}), 400

    topic = classify_topic(content)
    summary = generate_summary(content)

    return jsonify({
        "topic": topic,
        "summary": summary
    })

if __name__ == '__main__':
    # Ensure to log minimal details in case of issues
    port = int(os.environ.get('PORT', 8080))
    print(f"Starting Flask app on port {port}")
    app.run(debug=True, host='0.0.0.0', port=port)
