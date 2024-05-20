import os
import dotenv

# Bot setup
PREFIX = "$"
BOT_NAME = "JdR Assistant"
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# BOT Authorized Channels
BASE_CHANNEL = os.environ.get("BASE_CHANNEL")

# Test Guild ID
GUILD_ID = os.environ.get('GUILD_ID')

# Test ROLE IDs
MEMBER_ROLE_ID = os.environ.get('MEMBER_ROLE_ID')
