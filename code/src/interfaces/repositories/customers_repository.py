from abc import ABC, abstractmethod
from typing import Union

from src.entities.customer import Customer
from src.types.dtos.create_customer_dto import CreateCustomerDto


class CustomersRepository(ABC):

    @abstractmethod
    async def find_customer_by_id(self, customer_id: str) -> Union[Customer, None]:
        raise NotImplementedError

    @abstractmethod
    async def find_customer_by_email(self, email: str) -> Union[Customer, None]:
        raise NotImplementedError

    @abstractmethod
    async def find_customer_by_cpf(self, cpf: str) -> Union[Customer, None]:
        raise NotImplementedError

    @abstractmethod
    async def create_customer(self, customer: CreateCustomerDto) -> Customer:
        raise NotImplementedError
