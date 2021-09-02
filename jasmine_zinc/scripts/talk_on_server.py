import os
from jasmine_zinc import (
    talk_on_server,
    Talk,
    add_talk_arguments,
)

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('cid', type=int)
    parser.add_argument('talktext', type=str)
    parser.add_argument('--server-url', type=str, default=os.environ.get('SERVER_URL'), help='AssistantSeika HTTP Server')
    add_talk_arguments(parser=parser)
    args = parser.parse_args()

    cid = args.cid
    talktext = args.talktext
    server_url = args.server_url

    result = talk_on_server(
        server_url=server_url,
        cid=cid,
        talk=Talk(
            talktext=talktext,
        ),
    )

    print(result)

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()

    main()