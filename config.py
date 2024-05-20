import os

# TOKEN
BOT_TOKEN = int(os.environ.get("BOT_TOKEN"))

# BOT Authorized Channels
BASE_CHANNEL = int(os.environ.get('BASE_CHANNEL', ""))

# Test Guild ID
GUILD_ID = int(os.environ.get('GUILD_ID', ""))

# Test ROLE IDs
MEMBER_ROLE_ID = int(os.environ.get('MEMBER_ROLE_ID', ""))
