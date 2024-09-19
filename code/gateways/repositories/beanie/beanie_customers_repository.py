from code.entities.customer import Customer
from code.gateways.repositories.beanie.documents.customer_document import (
    CustomerDocument,
)
from code.interfaces.repositories.customers_repository import CustomersRepository
from code.types.dtos.create_customer_dto import CreateCustomerDto
from typing import Union


class BeanieCustomersRepository(CustomersRepository):

    async def find_customer_by_id(self, customer_id: str) -> Union[Customer, None]:
        customer = await CustomerDocument.find_one(
            CustomerDocument.id == customer_id
        ).project(CustomerDocument)

        if not customer:
            return None

        return customer

    async def find_customer_by_cpf(self, cpf: str) -> Union[Customer, None]:
        customer = await CustomerDocument.find_one(CustomerDocument.cpf == cpf).project(
            CustomerDocument
        )

        if not customer:
            return None

        return customer

    async def find_customer_by_email(self, email: str) -> Union[Customer, None]:
        customer = await CustomerDocument.find_one(
            CustomerDocument.email == email
        ).project(CustomerDocument)

        if not customer:
            return None

        return customer

    async def create_customer(self, customer: CreateCustomerDto) -> Customer:
        customer_to_create = CustomerDocument(**customer.model_dump())
        await customer_to_create.insert()
        return customer_to_create
