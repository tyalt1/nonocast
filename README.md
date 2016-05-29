# nonocast

[![Join the chat at https://gitter.im/tyalt1/nonocast](https://badges.gitter.im/tyalt1/nonocast.svg)](https://gitter.im/tyalt1/nonocast?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
Web server for universal media casting.

## Overview

Run a headless media sever.
The program hosts a website which can be used
to play/queue videos via their URLs.
These videos are streamed directly to the device,
without any unnecessary overhead.

The most common use case for this service is
running on a [Raspberry Pi](https://www.raspberrypi.org/) connected to a
living room TV. This way videos can be easily
displayed on the screen, and can be chosen by any
device on the network.

## Usage

#### To install onto your operating system
```
python2 setup.py install
```

#### To launch the app (which starts the web server)
```
python2 ./nonocast/main.py
```

#### Webpage is hosted on port 8000, simply open up a browser within local network
```
assume device ip is 192.168.1.3
http://192.168.1.3:8000
```

### Supported Media
- YouTube Videos
- Twitch Live Streams

## Dependencies

The service is built using the  [Liverstreamer](http://docs.livestreamer.io/) API.

## License

Copyright (C) 2016 Tyler Alterio, YuetLong Leung, Matthew Wolf, Allison Ober

Distributed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0.html).
