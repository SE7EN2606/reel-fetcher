import openai
from transformers import pipeline

# Set up OpenAI API key (Make sure you set your key here)
openai.api_key = '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'

# Initialize Hugging Face Zero-shot classifier
classifier = pipeline("zero-shot-classification")

# Possible topics to detect
possible_labels = ["cooking", "finance", "travel", "home improvement", "fitness", "self-development"]

def classify_topic(text):
    result = classifier(text, candidate_labels=possible_labels)
    return result['labels'][0]  # Return the most likely topic

def generate_summary(text):
    # Request GPT to summarize the text in 3-4 bullet points
    response = openai.Completion.create(
        model="gpt-4",
        prompt=f"Summarize the following content in 3-4 key bullet points:\n\n{text}",
        max_tokens=100
    )
    return response.choices[0].text.strip()
