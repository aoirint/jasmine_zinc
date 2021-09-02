from urllib.parse import urljoin
import json
import requests
from dataclasses import dataclass

from .Talk import Talk

@dataclass
class TalkOnServerResponse:
    message: str

def talk_on_server(
    server_url: str,
    cid: int,
    talk: Talk,
) -> TalkOnServerResponse:
    api_url = urljoin(server_url, f'PLAY2/{cid}')

    headers = {
        'Content-Type': 'application/json',
    }

    data = {
        'talktext': talk.talktext,
        'effects': {
            'volume': talk.effects.volume,
            'speed': talk.effects.speed,
            'pitch': talk.effects.pitch,
            'intonation': talk.effects.intonation,
            'shortpause': talk.effects.shortpause,
            'longpause': talk.effects.longpause,
        },
        'emotions': {
            '喜び': talk.emotions.joy,
            '怒り': talk.emotions.anger,
            '悲しみ': talk.emotions.sadness,
        },
    }

    r = requests.post(api_url, headers=headers, data=json.dumps(data), timeout=3)

    response = r.json()

    ret = TalkOnServerResponse(
        message=response['message'],
    )

    return ret
