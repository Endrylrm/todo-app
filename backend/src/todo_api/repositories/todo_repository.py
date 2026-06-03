from abc import ABC, abstractmethod


class TodoRepository(ABC):
    @abstractmethod
    def get_all[T](self) -> T:
        pass

    @abstractmethod
    def get_one[T](self, id: str) -> T:
        pass

    @abstractmethod
    def insert_one[T](self, entity: T) -> T:
        pass

    @abstractmethod
    def insert_many[T](self, entities: list[T]) -> T:
        pass

    @abstractmethod
    def update[T](self, id: str, entity: T) -> T:
        pass

    @abstractmethod
    def update_everything[T](self, id: str, entity: T) -> T:
        pass

    @abstractmethod
    def delete[T](self, id: str) -> T:
        pass
