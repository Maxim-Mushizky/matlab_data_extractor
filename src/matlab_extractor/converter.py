from typing import (
    Union,
    Dict,
    Optional
)


class Converter:

    def __init__(self, data: Optional[Dict]):
        if isinstance(data, Dict):
            self.__dict__ = data  # Dynamically generate attributes
