from abc import ABC, abstractmethod
from typing import Any


class Input(ABC):
    @classmethod
    @abstractmethod
    def parse_input(cls) -> Any:
        pass
