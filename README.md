# nonocast
Web server for universal media casting.

## Overview

Run a headless media sever.
The program hosts a website which can be used
to play/queue videos via their URLs.
These videos are streamed directly to the device,
without any unnecessary overhead.

The most common use case this is intended to be
running on a [Raspberry Pi](https://www.raspberrypi.org/) connected to the
living room TV. This way videos can be easily
displayed on the screen, and can be chosen by any
device on the network.

### Supported Media
- YouTube Videos
- Twitch Live Streams

## Dependencies

The service is built using the  [Liverstreamer](http://docs.livestreamer.io/) API.

## License

Copyright (C) 2016 Tyler Alterio

Distributed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0.html).
