from abc import ABCMeta, abstractmethod


class ABCBuilder(metaclass=ABCMeta):
    @abstractmethod
    def save(self, filename):
        raise NotImplementedError

    @abstractmethod
    def add_body(self):
        raise NotImplementedError

    @abstractmethod
    def add_wheels(self):
        raise NotImplementedError

    @abstractmethod
    def add_windows(self):
        raise NotImplementedError

    @abstractmethod
    def add_emblem(self):
        raise NotImplementedError
