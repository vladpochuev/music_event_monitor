import os
import subprocess
import time
from subprocess import CalledProcessError

from dotenv import load_dotenv

from parse_dumpsys import parse_data, parse_metadata, get_object_fields
from track import State

load_dotenv()


def is_adb_available():
    try:
        output = subprocess.check_output(["adb", "devices"], text=True)
    except FileNotFoundError:
        return False

    return any("device" in line for line in output.strip().splitlines()[1:])


def fetch_media_session_dump():
    return subprocess.check_output(
        ["adb", "shell", "dumpsys", "media_session"], text=True
    )


def extract_package_block(package, dump_text):
    strings = dump_text.splitlines()
    package_block = []
    text_shift = 0
    for line in strings:
        if text_shift != 0:
            if len(line) - len(line.lstrip()) <= text_shift:
                break
            package_block.append(line.strip())
        if package in line:
            text_shift = len(line) - len(line.lstrip())
    return "\n".join(package_block)


def parse_track_info(package_block):
    package_dict = parse_data(package_block)
    state_value = get_object_fields(package_dict["state"])
    inner_state_value = parse_data(state_value)["state"].strip()
    state = State(inner_state_value)

    track = parse_metadata(package_dict["metadata"])
    track.state = state
    return track


def report_track_changes(current_track, last_track):
    if current_track.title != last_track.title:
        print(f'New track: {current_track.title} - {current_track.artist}')

    if current_track.state != last_track.state:
        state = current_track.state
        if state == State.STOPPED:
            print("Stopped")
        elif state == State.PAUSED:
            print("Paused")
        elif state == State.PLAYING:
            print("Playing")


def is_track_valid(track):
    return (track.artist != "null"
            and track.title != "null"
            and track.state != "null")


def main():
    package_name = os.getenv("PACKAGE_NAME")
    interval = float(os.getenv("INTERVAL_MS")) / 1000

    if not is_adb_available():
        print("ADB is not found")
        return

    last_track = None
    try:
        while True:
            media_session_dump = fetch_media_session_dump()
            package_block = extract_package_block(package_name, media_session_dump)
            if not package_block.strip():
                raise ConnectionError
            current_track = parse_track_info(package_block)

            if current_track != last_track and is_track_valid(current_track):
                if last_track:
                    report_track_changes(current_track, last_track)
                last_track = current_track

            time.sleep(interval)
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except ConnectionError:
        print("Connection error.")
    except CalledProcessError:
        print("Error while executing the command.")


if __name__ == "__main__":
    main()
