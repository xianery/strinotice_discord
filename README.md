# Installation
1. `git clone https://github.com/xianery/strinotice_discord.git`
2. `cd strinotice_discord-main`
3. `pip install -r requirements.txt`
4. `python main.py`

# JSON files format
#### JSON file what contain server's feed channel
```json
{
    "<server_id>": {
        "selected_channel": "<channel_id>"
    }
}
```
#### JSON file what contain bot settings
```json
{
    "token": "<bot_token>",     // Bot token
    "prefix": "/"               // Prefix for commands
}
```