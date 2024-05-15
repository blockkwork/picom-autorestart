import os
import subprocess
import time

START_CMD = "picom &"

def is_downed() -> bool:
    res = subprocess.run(
        ["pgrep", "picom"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    if res.stdout.decode("utf-8") == "":
        return True
    return False


if __name__ == "__main__":
    while True:
        downed = is_downed()
        if downed:
            os.system(START_CMD)
        time.sleep(0.1)
