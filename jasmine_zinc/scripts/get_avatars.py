import os
from jasmine_zinc import get_avatars

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--server-url', type=str, default=os.environ.get('SERVER_URL'), help='AssistantSeika HTTP Server')
    args = parser.parse_args()

    server_url = args.server_url

    avatars = get_avatars(
        server_url=server_url,
    )

    print(avatars)

if __name__ == '__main__':
    from dotenv import load_dotenv
    load_dotenv()

    main()