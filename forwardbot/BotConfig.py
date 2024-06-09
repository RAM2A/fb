from os import environ
class Config(object):
    API_ID = environ.get("API_ID", 24665357)
    API_HASH = environ.get("API_HASH", "beb7e4b83ada668fa85f9a9b56338f1d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6710116600:AAHfY2VAo9k0PNLfbI_ypODOh11h6s8-q4w")
    STRING_SESSION = environ.get("STRING", "BQF4XQ0AMmHAQSs90w8BFOcXLMfQdTTfLL7lUGyd5pZlBEIZCTmqBEiTRxQapBxHY3XOg5xLhZCZGc-BjKs8UI96vhfT_gF_uGCqhjIf33t5lRfom_g86bdq7PsgvrTQOssfQGLU4NXChfnAHE9I7HGEFJ8QePkPSIJPdj36HeaNCOAD4opBRapD4wwZnFIM0Vhi5cYmlCUfZXBwj7kEAB3DLVq5aVnvLtbdIq6Zk8TFDfFEqE3WwFz-uxsB1hzQLG2vg_MzfXpEkR0qspRS_SpoQxZcNnBoqsV1gWNFpN_pQZ3azTae5TPGLa7_0qiFt-TYJtS5956d54wuaDUD5yPjWX4tkgAAAABmXyPCAA")
    SUDO_USERS = environ.get("SUDO_USERS", None)
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    The Commands in the bot are:
    
    **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    **Command :** /reset
    **Usage : ** Resets the message count to 0.
    **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    **Command :** /join
    **Usage : ** Joins the channel.
    **Command :** /help
    **Usage : ** Get the help of this bot.
    **Command :** /status
    **Usage :** Check current status of Bot.
    **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    Bot is created by @lal_bakthan and @subinps
    """
