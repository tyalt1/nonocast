#!/usr/bin/env python

rules = []

def any_is_in(matches, target):
    for match in matches:
        if match in target:
            return True
    return False

def add_rule(tokens, command):
    rules.append((tokens, command))

def get_play_command(url):
    for tokens, command in rules:
        if any_is_in(tokens, url):
            return command.replace('{url}', url)
    raise IndexError

# Add your rules here!

add_rule(
    ['youtube.com', 'twitch.tv'],
    'vlc "{url}" --fullscreen'
)
add_rule(['.html'], 'firefox "{url}"')
add_rule(['.mkv'], 'vlc "{url}" --fullscreen --play-and-exit')
add_rule(['.mp3'], 'omxplayer "{url}"')
add_rule(['.txt'], 'gedit "{url}" --new-window')
