# Translator-Bot

Translator Bot is designed to be the only translator bot that any server needs. It comes equipped with fully customizable settings and features that are necessary for running a successful server!

## Features

# Commands
- `/translate message languages`: Translates the message into one, or multiple languages. Languages are split by `,`.

`/translate Hello world! es,fr`
>>> ¡Hola Mundo!
>>> Bonjour le monde!

## Getting Started

To use this bot in your server, follow these steps:

1. **Setup The Bot:**
  - Select `Presence Intent`, `Server Members Intent`, and `Message Content Intent` from the Discord Developer Portal.
  - Generate a Bot Token and put it in `config.yml`
  - Generate an OAuth2 URL with `bot`, `applications.command`, and necessary permissions (Administrator recommended).

2. **Invite The Bot:**
  - Invite the bot with the generated OAuth2 URL to your Discord server(s).

3. **Configure Bot Settings:**
  - Configure all information located in `config.yml`.