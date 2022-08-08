import rumps
import subprocess


class Berlin(rumps.App):
    def __init__(self):
        super(Berlin, self).__init__("Berlin")

    @rumps.timer(1)
    def update_title(self, _):
        # i only could make subprocess work in this way
        title = subprocess.run(
            ["osascript", "-e",
                "tell application \"Spotify\" to name of current track as string"],
            stdout=subprocess.PIPE).stdout.decode("utf-8")
        artist = subprocess.run(
            ["osascript", "-e",
                "tell application \"Spotify\" to artist of current track as string"],
            stdout=subprocess.PIPE).stdout.decode("utf-8")

        self.title = "▶︎  " + \
            title.join(title.splitlines()) + " - " + \
            artist.join(artist.splitlines())


if __name__ == '__main__':
    Berlin().run()
