import subprocess
import time

engineSound = subprocess.Popen(['play', 'v8.mp3'])

time.sleep(2)

engineSound.kill()
print("Killed")
