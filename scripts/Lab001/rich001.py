import rich
from rich.progress import track
import rich.traceback
import time

rich.traceback.install()

# 3 / 0

rich.get_console().clear()
rich.get_console().rule('My Awesome Script v 1.0')
rich.print('Hello :smiley: [red b]world[/red b]!')

for i in track(range(10)):
    time.sleep(1)
