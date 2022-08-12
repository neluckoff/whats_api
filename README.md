<div align="center">
    <h1>Whats API</h1>
    Open source module for sending messages to WhatsApp based on Selenium
</div>
&nbsp;

<div align="center">
    <a href="https://github.com/neluckoff/social_spam/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/neluckoff/social_spam?style=flat-square"></a>
    <a href="https://github.com/neluckoff/social_spam/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/neluckoff/social_spam?style=flat-square"></a>
    <a href="https://github.com/neluckoff/social_spam"><img alt="GitHub license" src="https://img.shields.io/github/license/neluckoff/social_spam?style=flat-square"></a>
    <a href="https://github.com/neluckoff/social_spam/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/neluckoff/social_spam?style=flat-square"></a>
</div>

## Installation
You can install the latest version with the command:

```shell
pip install whats-api
```
Or you can install from GitHub:

```shell
pip install -U https://github.com/neluckoff/whats_api/archive/master.zip
```

## Sending a message
**[More detailed example here](https://github.com/neluckoff/whats_api/tree/master/examples)**

```python
from whats_api import Client, User

client = Client()
user = User(client)

name = user.get_name()
status = user.get_status()

message = f"Hello, this is {name}.\n" \
          f"Have you seen my status - ({status})?"

client.message_send("+79266569989", message)
```

## Contributing
I have a positive attitude towards PR and pull requests. Glad to see that people like the package.

In the plans: add the ability to send messages with an image and video

- Creator: [@neluckoff](https://github.com/neluckoff)

## License

- Copyright © 2022 [neluckoff](https://github.com/neluckoff).
- This project is [MIT](https://github.com/neluckoff/whats_api/blob/master/LICENSE) licensed.
