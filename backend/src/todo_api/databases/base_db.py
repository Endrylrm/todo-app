from abc import ABC, abstractmethod


class BaseDB(ABC):
    @abstractmethod
    def create_connection[T](self) -> T:
        pass

    @abstractmethod
    def init_db(self):
        pass
