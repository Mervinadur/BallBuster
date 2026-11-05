"""Streamlit wrapper for BallBuster.

The game runs entirely in the player's browser from game.html. Streamlit only
serves the page, because a server round trip per frame would be far too slow
for a real-time game.
"""

from pathlib import Path

import streamlit as st

GAME_FILE = Path(__file__).parent / "game.html"
GAME_HEIGHT = 680

st.set_page_config(page_title="BallBuster", page_icon="🧱", layout="centered")

# Trim Streamlit's page chrome so the game fits on screen, especially on phones.
st.markdown(
    """
    <style>
      .block-container { padding: 0.5rem 0.5rem 1rem; max-width: 760px; }
      header[data-testid="stHeader"] { display: none; }
      #MainMenu, footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.iframe(GAME_FILE, height=GAME_HEIGHT, alt="BallBuster game")

st.caption("Free to play, with no login or credits. Click the game first to use the keyboard.")
