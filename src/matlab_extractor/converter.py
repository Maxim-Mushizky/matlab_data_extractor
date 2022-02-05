from typing import (
    Union,
    Dict,
    Optional
)


class Converter:

    def __init__(self, data: Optional[Dict]):
        self._data = data
        if isinstance(data, Dict):
            self.__dict__ = data  # Dynamically generate attributes

    def keys_into_attributes(self, data: Dict):
        for key in data.keys():
            if isinstance(data[key], Dict):
                self.__dict__[key] = data[key]
                data = data[key]
                return self.keys_into_attributes(data)
            else:
                return data[key]
