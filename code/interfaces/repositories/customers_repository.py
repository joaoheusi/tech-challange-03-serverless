from abc import ABC, abstractmethod
from code.entities.customer import Customer
from code.types.dtos.create_customer_dto import CreateCustomerDto
from typing import Union


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
