# BallBuster

A free brick-breaking arcade game that runs in the browser. There's no login, no credits and nothing to install.

## How to play

| Action | Mouse | Touch | Keyboard |
|---|---|---|---|
| Move the paddle | Move the mouse | Slide your finger | Left/Right arrows or A/D |
| Launch the ball | Click | Tap | Space or Enter |
| Pause | Top-right button | Top-right button | P or Esc |
| Sound on/off | ♪ button | ♪ button | M |

Click the game once before using the keyboard, so that it has focus.

Clear every brick to finish a level. Steel bricks can't be broken and don't need to be. After level 8, the levels repeat with tougher bricks.

### Bricks

- **Coloured:** one hit
- **Dotted:** one hit per dot
- **Orange with a star:** explodes and destroys the bricks around it
- **Steel with two rivets:** unbreakable

### Capsules

| Capsule | Effect |
|---|---|
| M | Multi-ball: every ball in play splits into three |
| E | Wide paddle |
| L | Laser: the paddle fires automatically |
| B | Fireball: smashes through breakable bricks |
| C | Catch: the paddle holds the ball until you launch it, or for 3 seconds |
| W | Slow ball |
| + | Extra life |
| S | Tiny paddle (bad) |
| F | Fast ball (bad) |

## Run it locally

Requires Python 3.11 or newer.

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

You can also open `game.html` directly in a browser, because the whole game is in that one file.

## Deploy it for free

1. Sign in with GitHub at [share.streamlit.io](https://share.streamlit.io).
2. Select **Create app**, then choose to deploy from an existing repo.
3. Set the repository to `Mervinadur/BallBuster`, the branch to `main` and the main file to `streamlit_app.py`.
4. Choose an app URL, then select **Deploy**.
5. In the app's sharing settings, check that anyone with the link can view it.

Community Cloud puts apps to sleep after a period without traffic. The next visitor can wake the app with one click.

## How it works

The game is plain HTML5 Canvas and JavaScript in `game.html`, and runs entirely in the player's browser. `streamlit_app.py` only serves that page. All graphics are drawn in code and all sounds are synthesised, so there are no asset files.

## License

[MIT](LICENSE)
