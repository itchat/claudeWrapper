# Claude-2 Multi-User Bot

采用 SQL Lite 与 python-telegram-bot 设计的 Telegram Claude 问答机器人

## Maintenance

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate
npm install pm2 -g
pm2 start bot.py --interpreter venv/bin/python3.11
```

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

- [Claude-2.1](https://docs.anthropic.com/claude/docs) is a language model developed by Anthropic Technology Ltd. 

## Contact

For any inquiries or questions regarding this bot, you can reach us at [nar3tsn3p@mozmail.com](mailto:your-email@example.com).

