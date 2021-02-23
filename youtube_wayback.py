import argparse
import re
import requests
import sys

_RE_VALID_URL = re.compile(r'(?:(?:https?://(?:www\.)?)?(?:youtube\.com/watch\?v=|youtu\.be/))?(?P<video_id>[a-zA-Z0-9_-]{11})')
_WAYBACK_URL = 'https://web.archive.org/web/2oe_/http://wayback-fakeurl.archive.org/yt/{video_id}'

def youtube_wayback(video_id, session=None):
    session = session or requests.Session()
    response = session.head(_WAYBACK_URL.format(video_id=video_id), allow_redirects=True)
    response.raise_for_status()
    return response.url

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Check if YouTube videos are archived in the Wayback Machine')
    parser.add_argument('-x', '--proxy', metavar='URL', help='URL of the proxy server to use')
    parser.add_argument('video_urls', metavar='URL', nargs='+', help='YouTube URLs')
    args = parser.parse_args()

    session = requests.Session()
    session.proxies = {'http': args.proxy, 'https': args.proxy}

    for video_url in args.video_urls:
        video_id = _RE_VALID_URL.fullmatch(video_url).group('video_id')
        print(video_id, end=' ', flush=True)
        try:
            wayback_url = youtube_wayback(video_id, session=session)
        except requests.exceptions.HTTPError as e:
            print(e.response.status_code)
        else:
            print(wayback_url)
