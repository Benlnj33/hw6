from abc import ABC, abstractmethod

class Plugin(ABC):
    #Interface for calculator plugins.

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_commands(self):
        pass