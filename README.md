## Alexis Bot

This Python script sets up a Discord bot capable of generating memes and providing affirmations to specific users based on their messages. The bot listens for specific triggers and responds accordingly.

### Installation

1. Clone the repository.
2. Install the required dependencies:

   ```bash
   pip install discord.py Pillow flask

## Set up environment variables:

Please ensure you have a Bot_Token environment variable set with your bot token.

## Usage
Run the script.
``` bash
python main.py
```
Interact with the bot on your Discord server by using the defined triggers:

When a specific user mentions "hate," the bot generates a meme and sends an affirmation to them.
A specific user with a designated ID triggering "ping" will receive a tailored response.

## Configuration

Replace 'YOUR_BOT_TOKEN' with your actual bot token.

Modify the allowed_user_id list to include the IDs of users you want to respond to.

Customize or expand the affirmations dictionary with your preferred messages.

## Functionality

The bot utilizes the Discord API, handles events like on_ready() and on_message(), and processes commands using the defined prefixes.

## Keep Alive

The bot utilizes Flask to keep itself alive. The keep_alive.py script provides a simple web server that responds to requests, preventing the bot from shutting down due to inactivity.

Make sure to replace the placeholder URL in your UptimeRobot configuration with the generated Flask URL
