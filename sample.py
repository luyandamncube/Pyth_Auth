"""Python console app with device flow authentication."""
# Copyright (c) Microsoft. All rights reserved. Licensed under the MIT license.
# See LICENSE in the project root for license information.
import pprint

import config

from helpers import api_endpoint, device_flow_session


def find_manager(session):

    # print('\nGet user profile ---------> https://graph.microsoft.com/v1.0/me')
    user_profile = session.get(api_endpoint('me'))
    # print(28*' ' + f'<Response [{user_profile.status_code}]>',
    #       f'bytes returned: {len(user_profile.text)}\n')
    # if not user_profile.ok:
    #     pprint.pprint(user_profile.json())  # display error
    #     return
    user_data = user_profile.json()
    email = user_data['mail']
    # display_name = user_data['displayName']

    # print(f'Your name ----------------> {display_name}')
    # print(f'Your email ---------------> {email}')
    user_search = input(f'Search-for (ENTER=self) -->') or email
    search_response = session.get(api_endpoint(f'users/{user_search}/manager'))
    # print(f'\nUser manager ----------> https://graph.microsoft.com/v1.0/users/{user_search}/manager')
    print(f'<Response [{search_response.status_code}]>')
    pprint.pprint(search_response.json())

if __name__ == '__main__':
    GRAPH_SESSION = device_flow_session(config.CLIENT_ID)
    if GRAPH_SESSION:
        find_manager(GRAPH_SESSION)
