import os
import openai
from dotenv import load_dotenv

load_dotenv()

class MoodAI:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("❌ Error: OPENAI_API_KEY is missing. Please check your .env file.")

        openai.api_key = api_key

    def analyze_mood(self, text: str) -> str:

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that extracts 3–6 music-related keywords (genres, mood, style) based on the user's description."},
                    {"role": "user", "content": text}
                ],
                max_tokens=50,
                temperature=0.7
            )

            if response and response.choices:
                mood_tags = response.choices[0].message["content"].strip()
                return mood_tags
            else:
                return "calm music"

        except Exception as e:
            print("⚠ Mood analysis error:", str(e))
            return "calm music"
