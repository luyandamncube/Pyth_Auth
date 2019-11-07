"""Configuration settings for console app using device flow authentication
"""

CLIENT_ID = 'ENTER_YOUR_CLIENT_ID'

AUTHORITY_URL = 'https://login.microsoftonline.com/common'
RESOURCE = 'https://graph.microsoft.com'
API_VERSION = 'v1.0'
EMAIL='ENTER_YOUR_EMAIL_ADDRESS'
PASSWORD='ENTER_YOUR_PASSWORD'
# This code can be removed after configuring CLIENT_ID and CLIENT_SECRET above.
if 'ENTER_YOUR' in CLIENT_ID:
    print('ERROR: config.py does not contain valid CLIENT_ID.')
    import sys
    sys.exit(1)
