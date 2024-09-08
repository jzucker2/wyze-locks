#!/usr/bin/env python3
import asyncio
import os
import pprint
import sys


from custom_components.wyze_locks.api import WyzeLocksApiClient

EMAIL = os.environ.get("WYZE_EMAIL")
PASSWORD = os.environ.get("WYZE_PASSWORD")
KEY_ID = os.environ.get("WYZE_KEY_ID")
API_KEY = os.environ.get("WYZE_API_KEY")


# https://stackoverflow.com/questions/73884117/how-to-replace-asyncio-get-event-loop-to-avoid-the-deprecationwarning
def get_current_event_loop():
    if sys.version_info < (3, 10):
        loop = asyncio.get_event_loop()
    else:
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()

        asyncio.set_event_loop(loop)
    return loop


async def main():
    bart_api = WyzeLocksApiClient(EMAIL, PASSWORD, KEY_ID, API_KEY)
    # First do wyze login
    wyze_login_response = await bart_api.async_wyze_login()
    print("Wyze login response incoming")
    pprint.pprint(wyze_login_response)
    print(f"Type of wyze_login_response => {type(wyze_login_response)}")
    print(f"Length of wyze_login_response => {len(wyze_login_response)}")


if __name__ == "__main__":
    loop = get_current_event_loop()
    loop.run_until_complete(main())
