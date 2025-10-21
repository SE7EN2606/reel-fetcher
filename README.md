# Instagram Reel Summarizer

A Flask application that analyzes and summarizes Instagram Reels using AI models.

## Features

- Video upload and processing
- Audio transcription using OpenAI Whisper
- Topic classification using Hugging Face Transformers
- 4-bullet point summary generation

## API Endpoints

- `POST /summarize` - Summarize a video or text content
- `GET /health` - Health check endpoint

## Usage

Upload a video file:
```bash
curl -X POST http://localhost:8080/summarize \
     -F "file=@reel.mp4" \
     -F "type=reel"
