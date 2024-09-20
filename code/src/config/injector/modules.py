from injector import Module, provider, singleton
from src.gateways.repositories.beanie.beanie_customers_repository import (
    BeanieCustomersRepository,
)
from src.interfaces.repositories.customers_repository import CustomersRepository


class CustomersRepositoryModule(Module):
    @singleton
    @provider
    def provide_customers_repository(self) -> CustomersRepository:
        return BeanieCustomersRepository()
