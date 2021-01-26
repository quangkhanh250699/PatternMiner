# Created by quangkhanh at 13/01/2021
# File: factory_base.py

from abc import ABCMeta, abstractmethod


class Factory(metaclass=ABCMeta):

    @abstractmethod
    def contain(self, code: str) -> bool:
        pass

    @abstractmethod
    def count(self) -> int:
        pass
