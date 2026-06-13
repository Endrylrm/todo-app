from abc import ABC, abstractmethod


class TodoRepository(ABC):
    @abstractmethod
    async def get_all[T](self) -> T:
        pass

    @abstractmethod
    async def get_one[T](self, id: str) -> T:
        pass

    @abstractmethod
    async def insert_one[T](self, entity: T) -> T:
        pass

    @abstractmethod
    async def insert_many[T](self, entities: list[T]) -> T:
        pass

    @abstractmethod
    async def update_one[T](self, id: str, entity: T) -> T:
        pass

    @abstractmethod
    async def update_many[T](self, entities: list[T]) -> T:
        pass

    @abstractmethod
    async def upsert_one[T](self, id: str, entity: T) -> T:
        pass

    @abstractmethod
    async def upsert_many[T](self, entities: list[T]) -> T:
        pass

    @abstractmethod
    async def delete_one[T](self, id: str) -> T:
        pass

    @abstractmethod
    async def delete_many[T](self, ids: list[str]) -> T:
        pass
