# Jasmine Zinc

## Usage: Console Scripts
### Environment Variables
```env
SERVER_URL=http://user:password@server_ip:7180
```

### jaz_get_avatars
Fetch avatar list (`cid`, `name`, etc.).

```shell
jaz_get_avatars --server-url=http://user:password@server_ip:7180

export SERVER_URL=http://user:password@server_ip:7180
jaz_get_avatars
```

### jaz_talk_on_server
Talk on server.

```shell
jaz_talk_on_server 5201 読み上げ文字列 --server-url=http://user:password@server_ip:7180

export SERVER_URL=http://user:password@server_ip:7180
jaz_talk_on_server 5201 読み上げ文字列
```

### jaz_record_talk
Record a talk voice on server, download as a wave file and play on client.

```shell
jaz_record_talk 5201 読み上げ文字列 --server-url=http://user:password@server_ip:7180

export SERVER_URL=http://user:password@server_ip:7180
jaz_record_talk 5201 読み上げ文字列
```

## Development: Test Console Scripts
### Create .env file
```env
SERVER_URL=http://user:password@server_ip:7180
```

### Execute
```shell
./scripts/get_avatars

./scripts/talk_on_server 5201 てすと

./scripts/record_talk 5201 てすと
```
