"""Lock platform for Wyze Locks."""

from homeassistant.components.lock import LockEntity

from .const import DEFAULT_NAME, DOMAIN, LOCK
from .entity import WyzeLocksEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup lock platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([MultiZoneReceiverMediaPlayer(coordinator, entry)])


class MultiZoneReceiverMediaPlayer(WyzeLocksEntity, LockEntity):
    """wyze_locks lock class. Based on https://github.com/home-assistant/core/blob/dev/homeassistant/components/lock/__init__.py"""

    @property
    def name(self):
        """Return the name of the lock."""
        return f"{DEFAULT_NAME}_{LOCK}"

    @property
    def device_class(self):
        """Return the device class of the sensor."""
        return "wyze_locks__custom_lock_device_class"
