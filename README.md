# ⏰ Python Alarm Clock (IST, 12-hour format)

A simple command-line alarm clock built in Python. It always checks time in
**Indian Standard Time (IST)**, no matter what timezone your system is set to,
and accepts alarm times in standard **12-hour format** (e.g. `07:30 AM`).

## Features
- 12-hour time input and display (`HH:MM AM/PM`)
- Always uses IST (`Asia/Kolkata`) via `pytz`, regardless of system timezone
- Live current-time display while waiting
- Plays a sound when the alarm goes off (with a terminal-bell fallback if no
  sound file is found)
- Input validation with retry on bad format

## Requirements
- Python 3.7+
- Packages listed in `requirements.txt`

## Installation
```bash
git clone https://github.com/syedyasoobabbas-byte/alarm-clock.git
cd alarm-clock
pip install -r requirements.txt
```

## Usage
```bash
python alarm_clock.py
```
You'll be prompted to enter the alarm time, for example:
```
Enter alarm time in 12-hour format (e.g. 07:30 AM): 09:45 PM
```
The program will then display the live IST time and ring an alarm once the
clock reaches the time you entered. Press `Ctrl+C` at any time to cancel.

### Optional: custom alarm sound
Place an `alarm.mp3` file in the same folder as `alarm_clock.py` to have it
play when the alarm triggers. If no file is found, the program falls back to
the terminal bell sound.

## Project Structure
```
alarm-clock/
├── alarm_clock.py     # Main program
├── requirements.txt   # Dependencies
├── README.md           # Documentation
└── .gitignore
```

## Author
**Syed Yasoob Abbas**
GitHub: [syedyasoobabbas-byte](https://github.com/syedyasoobabbas-byte)
