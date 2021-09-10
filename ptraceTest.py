import subprocess
import signal
import os
import time


def handler(signal, frame):
    print('python: she say hello to me.')

for i in range(100):
    she = subprocess.Popen(['./test', str(os.getpid())])

    signal.signal(5, handler)
    signal.pause()
    time.sleep(0.001)
    she.send_signal(1)
    print('python: I say hello to her.')
    she.wait()
    she.poll()
    print(she.returncode)