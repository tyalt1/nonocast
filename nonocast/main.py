# Copyright 2016 Tyler Alterio, YuetLong Leung, Matthew Wolf, Allison Ober
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

from streamer_engine import stream
from frontend import run as run_server
from multiprocessing import Process
from vid_queue import VidQueue as Queue
from signal import *
from sys import exit

q = Queue(64)

def url_listener():
    while True:
        url = q.get()
        stream(url)

def cleanup(*args):
    exit(0)

def main():
    for sig in (SIGABRT, SIGINT, SIGTERM, SIGILL, SIGSEGV):
        signal(sig, cleanup)

    frontend = Process(target=run_server, args=[q.put_nowait])
    backend = Process(target=url_listener)
    for proc in (frontend, backend):
        proc.daemon = True
        proc.start()

    pause()

if __name__ == "__main__":
    main()
