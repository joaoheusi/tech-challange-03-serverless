from code.config.injector.modules import CustomersRepositoryModule

from injector import Injector

container = Injector(
    [
        CustomersRepositoryModule,
    ]
)
