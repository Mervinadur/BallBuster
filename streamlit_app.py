"""Streamlit wrapper for BallBuster.

The game runs entirely in the player's browser from game.html. Streamlit only
serves the page, because a server round trip per frame would be far too slow
for a real-time game.
"""

from pathlib import Path

import streamlit as st

GAME_FILE = Path(__file__).parent / "game.html"
FALLBACK_HEIGHT = 680

st.set_page_config(page_title="BallBuster", page_icon="🧱", layout="centered")

# Remove Streamlit's page chrome and stretch the game over the visible screen.
# The game adapts its playfield to whatever height the frame ends up with.
st.markdown(
    """
    <style>
      header[data-testid="stHeader"], #MainMenu, footer { display: none; }
      .block-container, [data-testid="stMainBlockContainer"] {
        padding: 0 !important;
        max-width: 760px;
      }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      [data-testid="stElementContainer"]:has(style) { display: none; }
      [data-testid="stElementContainer"]:has(iframe),
      [data-testid="stElementContainer"]:has(iframe) * {
        height: 100vh !important;
        height: 100dvh !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.iframe(GAME_FILE, height=FALLBACK_HEIGHT, alt="BallBuster game")
