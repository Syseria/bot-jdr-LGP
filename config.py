import os

# Bot setup
PREFIX = "$"
BOT_NAME = "JdR Assistant"
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# BOT Authorized Channels
BOT_CHANNEL = int(os.environ.get('BOT_CHANNEL'))

# Test Guild ID
GUILD_ID = int(os.environ.get('GUILD_ID'))

# Test ROLE IDs
MANAGER_ROLE_ID = int(os.environ.get('MANAGER_ROLE_ID'))
BOT_ROLE_ID = int(os.environ.get('BOT_ROLE_ID'))
DM_ROLE_ID = int(os.environ.get('DM_ROLE_ID'))
MEMBER_ROLE_ID = int(os.environ.get('MEMBER_ROLE_ID'))

# Categories
BOT_CATEGORY_ID = int(os.environ.get('BOT_CATEGORY_ID'))
HOME_CATEGORY_ID = int(os.environ.get('HOME_CATEGORY_ID'))
DM_CATEGORY_ID = int(os.environ.get('DM_CATEGORY_ID'))
ONE_SHOTS_CATEGORY_ID = int(os.environ.get('ONE_SHOTS_CATEGORY_ID'))
TABLES_CATEGORY_ID = int(os.environ.get('TABLES_CATEGORY_ID'))

# Channels
RULES_CHANNEL = int(os.environ.get('RULES_CHANNEL'))
INFO_CHANNEL = int(os.environ.get('INFO_CHANNEL'))
WELCOME_CHANNEL = int(os.environ.get('WELCOME_CHANNEL'))
NEW_TABLE_CHANNEL = int(os.environ.get('NEW_TABLE_CHANNEL'))
