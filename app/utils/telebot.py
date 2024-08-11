import telegram
import os

class Telebot:
    def __init__(self, config_file='../config/config.ini'):
        """Starts the telegram bot with it's configurations."""
        from configparser import ConfigParser

        config = ConfigParser()
        config.read(config_file)

        self.bot_token = config.get('telegram', 'bot_token')
        self.chat_id = config.get('telegram', 'chat_id')
        self.bot = telegram.Bot(token=self.bot_token)

    def send_text_msg(self, msg: str) -> telegram.Message:
        """Sends a text message to a especified chat."""
        try:
            return self.bot.sendMessage(chat_id=self.chat_id, text=msg)
        except telegram.error.TelegramError as e:
            print(f"Sending text message error: {e}")
            raise

    def send_photos(self, photos: list) -> list:
        """Sends a list of photos to a especified chat."""
        try:
            media = [telegram.InputMediaPhoto(photo) for photo in photos]
            return self.bot.send_media_group(chat_id=self.chat_id, media=media, disable_notification=True)
        except telegram.error.TelegramError as e:
            print(f"Sending photos error: {e}")
            raise
