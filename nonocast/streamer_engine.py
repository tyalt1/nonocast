# Copyright 2016 Tyler Alterio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# see http://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true

import rules

from os import system
import os
import time
import signal
import subprocess

process = None

def stream(url):
    global process

    command = rules.get_play_command(url)
    if command:
        if process:
            os.killpg(
                os.getpgid(process.pid),
                signal.SIGTERM
            )

        print('running {}'.format(command))
        process = subprocess.Popen(
            command,
            shell=True,
            preexec_fn=os.setsid
        )

    else:
        print("I don't know how to open that :(")

if __name__ == "__main__":
    from sys import argv

    if len(argv) > 1:
        stream(argv[1])
    else:
        print 'usage: ./streamer_engine.py "your_url_here"'
