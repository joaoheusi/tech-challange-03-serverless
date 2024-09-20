from injector import Injector
from src.config.injector.modules import CustomersRepositoryModule

container = Injector(
    [
        CustomersRepositoryModule,
    ]
)
