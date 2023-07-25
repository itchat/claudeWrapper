import sqlite3
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='bot.log', level=logging.ERROR)


class User:
    def __init__(self, user_id, conversation_count, context = ''):
        self.user_id = user_id
        self.conversation_count = conversation_count
        self.context = context

    def __str__(self):
        return f"User ID: {self.user_id}, Conversation Count: {self.conversation_count}, Context: {self.context}"


class UserManager:
    def __init__(self):
        self.conn = sqlite3.connect('user_data.db')
        self.create_table()

    def create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    conversation_count INTEGER,
                    context TEXT
                )
            ''')
            self.conn.commit()
        except Exception as e:
            logger.error(f"Error creating table: {e}")

    def add_user(self, user_id):
        try:
            if not self.has_user(user_id):
                cursor = self.conn.cursor()
                cursor.execute('INSERT INTO users VALUES (?, ?, ?)', (user_id, 0, ''))
                self.conn.commit()
            else:
                logger.error(f"User with ID {user_id} already exists in the database.")
        except Exception as e:
            logger.error(f"Error adding user: {e}")

    def delete_user(self, user_id):
        try:
            if self.has_user(user_id):
                cursor = self.conn.cursor()
                cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
                self.conn.commit()
                return cursor.rowcount > 0
            else:
                logger.error(f"User with ID {user_id} does not exist in the database.")
                return False
        except Exception as e:
            logger.error(f"Error deleting user: {e}")
            return False

    def has_user(self, user_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
            return cursor.fetchone() is not None
        except Exception as e:
            logger.error(f"Error checking user existence: {e}")
            return False

    def get_user(self, user_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
            row = cursor.fetchone()
            if row:
                return User(row[0], row[1], row[2])
            return None
        except Exception as e:
            logger.error(f"Error retrieving user: {e}")
            return None

    def get_users(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT user_id, conversation_count FROM users')
            rows = cursor.fetchall()
            users = []
            for row in rows:
                users.append(User(row[0], row[1]))
            return users
        except Exception as e:
            logger.error(f"Error retrieving users: {e}")
            return []

    def get_conversation_count(self, user_id):
        try:
            user = self.get_user(user_id)
            if user:
                return user.conversation_count
            return 0
        except Exception as e:
            logger.error(f"Error retrieving conversation count: {e}")
            return 0

    def update_conversation_count(self, user_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('UPDATE users SET conversation_count = conversation_count + 1 WHERE user_id = ?', (user_id,))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Error updating conversation count: {e}")

    def get_context(self, user_id):
        try:
            user = self.get_user(user_id)
            if user:
                return user.context
            return ''
        except Exception as e:
            logger.error(f"Error retrieving context: {e}")
            return ''

    def update_context(self, user_id, context):
        try:
            cursor = self.conn.cursor()
            cursor.execute('UPDATE users SET context = ? WHERE user_id = ?', (context, user_id))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Error updating context: {e}")

    def clear_context(self, user_id):
        try:
            self.clear_conversation_count(user_id)
            self.update_context(user_id, '')
        except Exception as e:
            logger.error(f"Error clearing context: {e}")

    def clear_conversation_count(self, user_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute('UPDATE users SET conversation_count = 0 WHERE user_id = ?', (user_id,))
            self.conn.commit()
        except Exception as e:
            logger.error(f"Error clearing conversation count: {e}")


if __name__ == '__main__':
    logging.basicConfig(filename='bot.log', level=logging.ERROR)
    user_manager = UserManager()
    user_manager.create_table()
