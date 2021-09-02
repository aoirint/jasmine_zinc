from urllib.parse import urljoin
import json
import requests
from typing import Dict, List, Any
from dataclasses import dataclass

@dataclass(frozen=True)
class TalkEffects:
    volume: float = 1
    speed: float = 1
    pitch: float = 1
    intonation: float = 1
    shortpause: int = 150
    longpause: int = 370

@dataclass(frozen=True)
class TalkEmotions:
    joy: float = 0
    anger: float = 0
    sadness: float = 0

@dataclass
class Talk:
    talktext: str
    effects: TalkEffects = TalkEffects()
    emotions: TalkEmotions = TalkEmotions()

@dataclass
class TalkResponse:
    message: str

def talk_on_server(
    server_url: str,
    cid: int,
    talk: Talk,
) -> TalkResponse:
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

    ret = TalkResponse(
        message=response['message'],
    )

    return ret
