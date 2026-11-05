# BallBuster

A free brick-breaking arcade game that runs in the browser. There's no login, no credits and nothing to install.

**Play it now:** https://ballbuster.streamlit.app

## How to play

The paddle is at the top of the screen, and the ball bounces off the bottom wall. Don't let it get past your paddle. Clear every breakable brick to finish a level, and clear all 8 levels to win.

### Controls

| Action | Mouse | Touch | Keyboard |
|---|---|---|---|
| Move the paddle | Move the mouse | Slide a finger anywhere on the screen | Left/Right arrows or A/D |
| Launch the ball | Click | Tap | Space or Enter |
| Pause or resume | Top-right button | Top-right button | P or Esc |
| Sound on or off | Speaker button | Speaker button | M |

Click the game once before using the keyboard, so that it has focus. The game pauses itself if you switch to another tab or window.

### Lives and scoring

You start with 3 lives and can hold up to 6. You lose a life when your last ball gets past the paddle, and that also ends any active power-ups.

| Event | Points |
|---|---|
| Breaking a brick | 10, plus 2 for each brick in your current streak (up to 40 in total) |
| Hitting a multi-hit brick without breaking it | 2 |
| Catching any power-up | 50 |
| Clearing a level | 100 × the level number |

Your streak resets each time the ball touches the paddle. Your best score and sound setting are saved in your browser.

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

Broken bricks sometimes release a power-up, which travels to the paddle for you to catch. Power-ups are icons with no text. Good ones have a spinning ring, and bad ones have red spikes. Timed effects show at the bottom left, with a ring that runs down.

| Icon | Effect | Lasts |
|---|---|---|
| Three balls | Multi-ball: every ball in play splits into three, up to 12 balls | Until lost |
| Paddle with outward arrows | Wider paddle | 15 seconds |
| Paddle firing beams | Laser: the paddle fires automatically | 10 seconds |
| Flame | Fireball: smashes through breakable bricks | 8 seconds |
| Magnet | Catch: the paddle holds the ball until you launch it, or for 3 seconds | 15 seconds |
| Snail | Slower ball | 10 seconds |
| Heart | Extra life | Permanent |
| Paddle with inward arrows (bad) | Tiny paddle | 12 seconds |
| Lightning bolt (bad) | Faster ball | 8 seconds |

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

The game is plain HTML5 Canvas and JavaScript, and runs entirely in the player's browser. Streamlit only serves the page, because a server round trip for every frame would be too slow for a real-time game. All graphics are drawn in code and all sounds are synthesised, so there are no asset files.

| File | Purpose |
|---|---|
| `game.html` | The whole game: levels, power-ups, physics, drawing and sound |
| `streamlit_app.py` | Embeds the game and stretches it to fill the screen |
| `.streamlit/config.toml` | Dark theme for the Streamlit page |
| `requirements.txt` | The pinned Streamlit version |

The playfield has a fixed logical width of 640, and its height follows the screen's shape. That's how the game fills both phones and desktops. The game logic runs with the paddle at the bottom, and `draw()` flips the view, so in the code a larger `y` means closer to the paddle.

## Edit a level

Levels are in the `LEVELS` array near the top of `game.html`. Each brick picture is a list of rows, exactly 16 characters wide, and the first row appears at the top of the screen.

```js
{
  name: 'Meadow', picture: 'A flower in bloom', accent: '#f472b6', ambient: 'petals',
  key: { p: { c: '#f472b6' }, y: { c: '#fde047', hits: 2 } },
  rows: [
    '......pppp......',
    '.....pyyyyp.....',
  ],
  paint(g) { /* draws the scenery */ },
}
```

| Field | Meaning |
|---|---|
| `key` | Your own brick letters, each with a colour (`c`) and an optional number of `hits` |
| `rows` | The picture: `.` is empty, `S` is steel and `X` is explosive, and any other letter comes from `key` |
| `accent` | The colour of the paddle details and the line under the score bar |
| `ambient` | The animation: `petals`, `bubbles`, `sand`, `snow`, `embers`, `bats`, `stars` or `rain` |
| `paint(g)` | Draws the level's scenery, which is cached as a background image |

Leave breakable bricks reachable around any steel, or the level can't be finished. The game has no automated tests, so play through any level you change. If you add or remove levels, also update the "8 worlds" and "All 8 worlds cleared" text in `game.html`.

## License

[MIT](LICENSE)
