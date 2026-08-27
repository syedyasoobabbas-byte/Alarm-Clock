"""
Alarm Clock (IST, 12-hour format)
----------------------------------
A simple command-line alarm clock that:
- Works in 12-hour format (e.g. 07:30 AM / 09:45 PM)
- Always checks time in Indian Standard Time (IST), regardless of
  the system's local timezone
- Plays a sound (and prints an alert) when the alarm time is reached
 
Author: Syed Yasoob Abbas
"""
 
import time
from datetime import datetime
 
try:
    import pytz
except ImportError:
    raise SystemExit(
        "Missing dependency 'pytz'. Install it with: pip install -r requirements.txt"
    )
 
IST = pytz.timezone("Asia/Kolkata")
 
 
def get_current_ist_time_str() -> str:
    """Return the current time in IST as a 12-hour formatted string (e.g. 07:30:15 AM)."""
    return datetime.now(IST).strftime("%I:%M:%S %p")
 
 
def get_current_ist_hm_str() -> str:
    """Return current IST time truncated to hours:minutes (e.g. 07:30 AM), for comparison."""
    return datetime.now(IST).strftime("%I:%M %p")
 
 
def validate_alarm_time(alarm_time: str) -> bool:
    """Check that the given string matches 12-hour format like '07:30 AM'."""
    try:
        datetime.strptime(alarm_time.strip().upper(), "%I:%M %p")
        return True
    except ValueError:
        return False
 
 
def play_alarm_sound(repeats: int = 5):
    """
    Play an alert sound. Uses 'playsound' with a bundled/local audio file if
    available, otherwise falls back to the terminal bell character.
    """
    try:
        from playsound import playsound
        import os
 
        sound_file = os.path.join(os.path.dirname(__file__), "alarm.mp3")
        if os.path.exists(sound_file):
            for _ in range(repeats):
                playsound(sound_file)
            return
    except Exception:
        pass
 
    # Fallback: terminal bell
    for _ in range(repeats):
        print("\a", end="", flush=True)
        time.sleep(0.5)
 
 
def run_alarm(alarm_time: str):
    """Continuously check current IST time against the target alarm time."""
    alarm_time = alarm_time.strip().upper()
    print(f"\nAlarm set for {alarm_time} IST.")
    print("Waiting... (Press Ctrl+C to cancel)\n")
 
    try:
        while True:
            current_time = get_current_ist_hm_str()
            print(f"\rCurrent IST time: {get_current_ist_time_str()}", end="", flush=True)
 
            if current_time == alarm_time:
                print(f"\n\n⏰ WAKE UP! It's {alarm_time} IST — alarm ringing! ⏰\n")
                play_alarm_sound()
                break
 
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\nAlarm cancelled by user.")
 
 
def main():
    print("=" * 45)
    print("        PYTHON ALARM CLOCK (IST)")
    print("=" * 45)
    print(f"Current IST time: {get_current_ist_time_str()}\n")
 
    while True:
        alarm_time = input("Enter alarm time in 12-hour format (e.g. 07:30 AM): ")
        if validate_alarm_time(alarm_time):
            break
        print("Invalid format. Please use HH:MM AM/PM, e.g. 09:15 PM.\n")
 
    run_alarm(alarm_time)
 
 
if __name__ == "__main__":
    main()
