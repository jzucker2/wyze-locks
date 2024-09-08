"""WyzeLocksEntity class"""

from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, NAME, VERSION


class WyzeLocksEntity(CoordinatorEntity):
    def __init__(self, coordinator, config_entry):
        super().__init__(coordinator)
        self.config_entry = config_entry

    @property
    def config_entry_id(self):
        return self.config_entry.entry_id

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        return self.config_entry_id

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.config_entry_id)},
            "name": NAME,
            "model": VERSION,
            "manufacturer": NAME,
        }
