from abc import ABC, abstractmethod


class BaseModel(ABC):
    @abstractmethod
    def call_me(self):
        """Must be called"""
