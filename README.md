## Setup steps

1. Clone this repo      `git clone https://github.com/vladpochuev/music_event_monitor`
2. Create virtual environment      `python3 -m venv .venv`
3. Run virtual environment      `source .venv/bin/activate`
4. Install dependencies      `pip install -r requirements.txt`

## How to run the script

Just run the main.py file `python3 main.py`

There is INTERVAL_MS variable in .env that responsible for how often `adb shell dumpsys media_session` command checks in milliseconds. You can change it if you want
