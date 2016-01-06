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

from streamer_engine import stream
from frontend import run as run_server
from multiprocessing import Process, Queue

q = Queue(64)

def url_listener():
    while True:
        url = q.get()
        stream(url)

def main():
    frontend = Process(target=run_server, args=[q.put_nowait])
    backend = Process(target=url_listener)
    frontend.start()
    backend.start()

if __name__ == "__main__":
    main()