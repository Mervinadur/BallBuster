# BallBuster

A free brick-breaking arcade game that runs in the browser. There's no login, no credits and nothing to install.

**Play it now:** https://ballbuster.streamlit.app

## How to play

Move the paddle with your mouse, your finger or the arrow keys (or A and D). Click, tap or press Space to launch the ball. The buttons at the top right control sound and pausing, and you can also use M and P. Click the game once before using the keyboard, so that it has focus.

The paddle is at the top of the screen, and the ball bounces off the bottom wall. Don't let it get past your paddle. Clear every breakable brick to finish a level, and clear all 8 levels to win.

### Levels

Each level has its own scenery and animation, and its bricks form a picture that matches.

| # | World | Brick picture |
|---|---|---|
| 1 | Meadow | A flower in bloom |
| 2 | Ocean | A fish above the waves |
| 3 | Desert | A pyramid, sun and cactus |
| 4 | Arctic | A giant snowflake |
| 5 | Volcano | A volcano about to blow |
| 6 | Haunted Night | A glowing jack-o-lantern |
| 7 | Deep Space | A rocket lifting off |
| 8 | Castle Siege | The final fortress |

### Bricks

- **Plain:** one hit
- **Dotted:** one hit per dot
- **Orange with a dark star:** explodes and destroys the bricks around it
- **Grey-blue with two rivets:** steel, which can't be broken and doesn't need to be

### Power-ups

Power-ups are icons with no text. Good ones have a spinning ring, and bad ones have red spikes.

| Icon | Effect |
|---|---|
| Three balls | Multi-ball: every ball in play splits into three |
| Paddle with outward arrows | Wider paddle |
| Paddle firing beams | Laser: the paddle fires automatically |
| Flame | Fireball: smashes through breakable bricks |
| Magnet | Catch: the paddle holds the ball until you launch it, or for 3 seconds |
| Snail | Slower ball |
| Heart | Extra life |
| Paddle with inward arrows (bad) | Tiny paddle |
| Lightning bolt (bad) | Faster ball |

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
