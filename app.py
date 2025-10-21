import os
from flask import Flask, request, jsonify
from summarize import classify_topic, generate_summary

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():
    # Get the content from the request
    data = request.get_json()
    content = data.get("content", "")

    if not content:
        return jsonify({"error": "Content is required"}), 400

    # Classify the topic
    topic = classify_topic(content)

    # Generate the summary
    summary = generate_summary(content)

    # Return the response as JSON
    return jsonify({
        "topic": topic,
        "summary": summary
    })

if __name__ == '__main__':
    # Use the port that Cloud Run automatically sets, default to 8080 if not set
    port = int(os.environ.get('PORT', 8080))  # Cloud Run sets this environment variable
    app.run(debug=True, host='0.0.0.0', port=port)
