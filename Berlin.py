import rumps
import subprocess
import pyperclip

class Berlin(rumps.App):
    def __init__(self):
        super(Berlin, self).__init__("Berlin")
        self.song_name = ""

    @rumps.clicked("Copy Title")
    def copy_title(self, _):
        pyperclip.copy(self.song_name)

    @rumps.timer(3)
    def update_title(self, _):
        is_running = subprocess.run(
            ["osascript", "-e",
                "get running of application \"Spotify\""], capture_output=True)
        out, err = is_running.stdout.decode("utf-8").strip(), is_running.stderr.decode("utf-8").strip()

        if out == "false" and err != 0:
            self.title = "Berlin (Spotity is closed)"
            return

        title = subprocess.run(
            ["osascript", "-e",
                "tell application \"Spotify\" to name of current track as string"],
            stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
        artist = subprocess.run(
            ["osascript", "-e",
                "tell application \"Spotify\" to artist of current track as string"],
            stdout=subprocess.PIPE).stdout.decode("utf-8").strip()

        if title.strip() == "Advertisement" and len(artist.strip()) == 0:
            self.title = "▶︎  Ad"
            return

        self.song_name = title 
        self.title = "▶︎  " + title + " - " + artist


if __name__ == '__main__':
    Berlin().run()
