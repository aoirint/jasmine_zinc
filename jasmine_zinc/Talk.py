from dataclasses import dataclass
from typing import Dict, Any

@dataclass(frozen=True)
class TalkEffects:
    volume: float = 1 # 0-2, step 0.01
    speed: float = 1 # 0.5-4, step 0.01
    pitch: float = 1 # 0.5-2, step 0.01
    intonation: float = 1 # 0-2, step 0.01
    shortpause: int = 150 # 80-500, step 1
    longpause: int = 370 # 100-2000, step 1

@dataclass(frozen=True)
class TalkEmotions:
    joy: float = 0 # 0-1, step 0.01
    anger: float = 0 # 0-1, step 0.01
    sadness: float = 0 # 0-1, step 0.01

@dataclass
class Talk:
    talktext: str
    effects: TalkEffects = TalkEffects()
    emotions: TalkEmotions = TalkEmotions()

def talk2dict(talk: Talk) -> Dict[str, Any]:
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
    return data
