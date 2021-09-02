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
