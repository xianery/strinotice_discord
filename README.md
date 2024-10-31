# Installation
1. `git clone https://github.com/xianery/strinotice_discord.git`
2. `cd strinotice_discord-main`
3. `pip install -r requirements.txt`
4. `python main.py`
5. Insert bot token into JSON where contains bot settings

# JSON files templates
JSON files contains near with `main.py`
#### JSON file what contain server's feed channel (Default: `servers.json`)
```json
{
    "<server_id>": {
        "selected_channel": "<channel_id>"
    }
}
```
#### JSON file what contain bot settings (Default: `config.json`)
```json
{
    "token": "<bot_token>",     // Bot token
    "prefix": "/"               // Prefix for commands
}
```