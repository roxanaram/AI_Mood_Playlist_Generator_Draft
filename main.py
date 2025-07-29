import streamlit as st
from mood_ai import MoodAI
from playlist_generator import PlaylistGenerator

mood_ai = MoodAI()
playlist_gen = PlaylistGenerator()

st.title("🎵 AI Mood Playlist Generator")

user_input = st.text_area("Describe your current mood or vibe:", placeholder="Example: I'm feeling relaxed and want some chill evening music...")

if st.button("Generate Playlist"):
    if user_input.strip() == "":
        st.warning("Please enter a description of your mood.")
    else:
        mood_tags = mood_ai.analyze_mood(user_input)
        st.subheader("🎯 Mood Tags:")
        st.write(mood_tags)

        tracks = playlist_gen.search_tracks(mood_tags)

        if tracks:
            st.subheader("🎧 Recommended Songs:")
            for track in tracks:
                st.markdown(f"- [{track['name']} - {track['artist']}]({track['url']})")
        else:
            st.error("No songs found. Try changing your mood description.")
