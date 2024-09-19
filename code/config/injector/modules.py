from code.gateways.repositories.beanie.beanie_customers_repository import (
    BeanieCustomersRepository,
)
from code.interfaces.repositories.customers_repository import CustomersRepository

from injector import Module, provider, singleton


class CustomersRepositoryModule(Module):
    @singleton
    @provider
    def provide_customers_repository(self) -> CustomersRepository:
        return BeanieCustomersRepository()
