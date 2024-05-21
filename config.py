import os
import dotenv

# Bot setup
PREFIX = "$"
BOT_NAME = "JdR Assistant"
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# BOT Authorized Channels
BOT_CHANNEL = int(os.environ.get("BOT_CHANNEL"))

# Test Guild ID
GUILD_ID = int(os.environ.get('GUILD_ID'))

# Test ROLE IDs
MEMBER_ROLE_ID = int(os.environ.get('MEMBER_ROLE_ID'))

# CHANNELS
RULES_CHANNEL = int(os.environ.get('RULES_CHANNEL'))
INFO_CHANNEL = int(os.environ.get('INFO_CHANNEL'))
TEST_CHANNEL = int(os.environ.get('TEST_CHANNEL'))
