import rumps
import subprocess


class Berlin(rumps.App):
    def __init__(self):
        super(Berlin, self).__init__("Berlin")

    @rumps.timer(1)
    def update_title(self, _):
        # TODO: learn how to use subprocess lol 🙃
        # this was the only i could make it work
        title = subprocess.run(
            ["osascript", "-e",
                "tell application \"Spotify\" to name of current track as string"],
            stdout=subprocess.PIPE).stdout.decode("utf-8")
        artist = subprocess.run(
            ["osascript", "-e",
                "tell application \"Spotify\" to artist of current track as string"],
            stdout=subprocess.PIPE).stdout.decode("utf-8")

        # cutting off title after the first - (dash)
        # usually this slice is worthless
        # the two - (dash) can make people confused
        title = title.split(" - ")[0]
        self.title = "🎵 " + \
            title.join(title.splitlines()) + " - " + \
            artist.join(artist.splitlines())


if __name__ == '__main__':
    Berlin().run()
