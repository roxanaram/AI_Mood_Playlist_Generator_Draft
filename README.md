## 🎵 AI Mood Playlist Generator

> A mood-based music playlist generator powered by OpenAI API and Spotify API.  
> Enter your mood – get a personalized playlist that matches your vibe!  

---

### 📌 Features:
- 🧠 AI-powered mood analysis and playlist generation.
- 🤖 Uses OpenAI for interpreting mood and generating music suggestions.
- 🎶 Fetches songs via Spotify API (or another music database).
- 🌐 Simple web interface built with **Streamlit**.

---

### 🚀 Installation and Setup

#### 1️⃣ Clone the repository:
\`\`\`bash
git clone https://github.com/roxanaram/AI_Mood_Playlist_Generator_Draft.git
cd AI_Mood_Playlist_Generator_Draft
\`\`\`

#### 2️⃣ (Optional) Create a virtual environment:
\`\`\`bash
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
\`\`\`

#### 3️⃣ Install dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

#### 4️⃣ Create a `.env` file (not uploaded to GitHub):
\`\`\`env
OPENAI_API_KEY=your_openai_api_key_here
SPOTIFY_CLIENT_ID=your_spotify_client_id_here
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret_here
\`\`\`

> ⚠️ **Important:** `.env` is listed in `.gitignore`, so your API keys are safe and won’t be pushed to GitHub.

---

### ▶ Run the app:
\`\`\`bash
streamlit run main.py
\`\`\`
Open the link shown in your terminal (e.g., `http://localhost:8501`) to access the app.

---

### 📂 Project Structure:
\`\`\`
AI_Mood_Playlist_Generator_Draft/
│── mood_ai.py          # Core AI logic for mood analysis
│── main.py             # Streamlit main app
│── requirements.txt    # List of dependencies
│── .env.example        # Example environment variables
│── .gitignore          # Excluded files from Git
│── README.md           # Project documentation
\`\`\`

---

### ✅ Future Improvements:
- 🎵 Automatic creation of playlists directly on Spotify.
- 🎨 Improved and more stylish UI.
- 🌙 Multi-language mood detection support.

---

💡 **Author:** RoxanaRam  
📧 Contact: *(optional)*
EOF

# 2️⃣ Create an example .env file
cat << 'EOF' > .env.example
OPENAI_API_KEY=your_openai_api_key_here
SPOTIFY_CLIENT_ID=your_spotify_client_id_here
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret_here
EOF

# 3️⃣ Stage, commit, and push changes
git add README.md .env.example
git commit -m "Added English README and example .env file"
git push
