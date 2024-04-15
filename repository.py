import configparser

config = configparser.ConfigParser()
config.read('settings/config.ini')


def get_bot_name():
    return config["BOT"]["bot_name"]


def get_bot_token():
    return config["BOT"]["bot_token"]
