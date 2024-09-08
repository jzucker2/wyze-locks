"""Sample API Client."""

import asyncio
import logging

from wyze_sdk import Client

TIMEOUT = 10


_LOGGER: logging.Logger = logging.getLogger(__package__)

HEADERS = {"Content-type": "application/json; charset=UTF-8"}


class WyzeLocksApiClient:
    def __init__(self, username: str, password: str, key_id: str, api_key: str) -> None:
        """Sample API Client."""
        self._email = username
        self._password = password
        self._key_id = key_id
        self._api_key = api_key

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @property
    def key_id(self):
        return self._key_id

    @property
    def api_key(self):
        return self._api_key

    async def async_get_data(self) -> dict:
        """Get data from the API."""
        await asyncio.sleep(0)
        return await self.async_wyze_login()

    async def async_wyze_login(self):
        response = Client().login(
            email=self.email,
            password=self.password,
            key_id=self.key_id,
            api_key=self.api_key,
        )
        _LOGGER.debug("Wyze login response: %s", response)
        return response

    async def async_set_title(self, value: str) -> None:
        """Get data from the API."""
        await asyncio.sleep(0)
