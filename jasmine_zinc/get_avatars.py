from urllib.parse import urljoin
import requests
from typing import Dict, List, Any
from dataclasses import dataclass

@dataclass
class Avatar:
    cid: int
    name: str
    platform: str
    prod: str

def get_avatars(
    server_url: str,
) -> Dict[str, Any]:
    api_url = urljoin(server_url, 'AVATOR2')
    r = requests.get(api_url, timeout=3)

    avatar_list = r.json()
    avatars: List[Avatar] = []

    for avatar in avatar_list:
        avatars.append(Avatar(
            cid=avatar['cid'],
            name=avatar['name'],
            platform=avatar['platform'],
            prod=avatar['prod'],
        ))

    return avatars
