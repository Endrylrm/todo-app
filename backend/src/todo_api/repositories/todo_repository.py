from abc import ABC, abstractmethod


class TodoRepository(ABC):
    @abstractmethod
    def create_table(self):
        pass

    @abstractmethod
    def get_all[T](self) -> T:
        pass

    @abstractmethod
    def get_one[T](self, id: str) -> T:
        pass

    @abstractmethod
    def save[T](self, entity: T) -> T:
        pass

    @abstractmethod
    def edit[T](self, id: str, entity: T) -> T:
        pass

    @abstractmethod
    def edit_everything[T](self, id: str, entity: T) -> T:
        pass

    @abstractmethod
    def delete[T](self, id: str) -> T:
        pass
