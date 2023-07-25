# Claude-2 Multi-User Bot

**Claude-2 Multi-User Bot** is a Telegram bot that utilizes the Claude-2 language model to provide natural language responses to user prompts. The bot is designed to support multiple users, each with their own conversation history and context.

## Features

- **Multi-User Support**: The bot allows multiple users to interact with it separately, maintaining individual conversation histories and contexts.

- **Claude-2 Language Model**: The bot uses the powerful Claude-2 language model to generate natural and contextually relevant responses to user prompts.

- **File Processing**: Users can upload text files (.txt or .md) privately to have the bot process and respond to the content.

- **Super Admin Controls**: Super admin users have additional commands to manage users, such as listing all users, searching for a user, adding a new user, and deleting users.

## Requirements

- Python 3.8 or higher
- Telegram API token (for the Telegram bot)
- Claude-2 API token (for the language model)
- SQLite database (for user data storage)

## Setup

1. Clone the repository from GitHub.

2. Install the required Python packages.

3. Create a `config.py` file and provide the necessary configuration variables:
   - `BOT_TOKEN`: Your Telegram bot token.
   - `ANTHROPIC_TOKEN`: Your Claude-2 API token.
   - `SUPER_ADMIN_IDS`: List of Telegram user IDs for super admin users.

4. Create the SQLite database file (`user_data.db`) to store user data. Run `database.py` to create the necessary table.

5. Run `bot.py` to start the bot.

## Usage

The bot responds to commands and messages in both private chats and supergroups.

**Commands**:
- `/c <message>`: Send a message to initiate a conversation with the bot.
- `/clear`: Clear your conversation history and context.
- `/list` (Super Admin Only): List all users and their conversation counts.
- `/search <user_id>` (Super Admin Only): Search for a user and retrieve their information.
- `/delete <user_id>` (Super Admin Only): Delete a user and their data.
- `/add <user_id>` (Super Admin Only): Add a new user.

**File Processing**:
- In a private chat, upload a text file (.txt or .md) to have the bot process and respond to the content.

**Super Admins**:

- Super admins are users specified in the `SUPER_ADMIN_IDS` list in `config.py`. They have additional commands for user management.

## Important Notes

- The bot will automatically clear a user's conversation history after 50 interactions to avoid excessive data accumulation.

- If the Claude-2 API encounters an error, the bot will attempt to retry up to three times before notifying the user of an empty response.

- The bot will only process text files (.txt or .md) of size between 5 bytes and 30MB.

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

- [Claude-2](https://docs.anthropic.com/claude/docs) is a language model developed by Anthropic Technology Ltd. 

## Contact

For any inquiries or questions regarding this bot, you can reach us at [nar3tsn3p@mozmail.com](mailto:your-email@example.com).

