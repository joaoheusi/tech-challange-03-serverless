import os
from code.controllers.customers_controller import CustomersUseCasesController
from code.entities.customer import Customer
from typing import Union

import uvicorn
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
def index():
    return "Hello, from AWS Lambda!"


@app.get(
    "/{identifier}",
    response_model=Customer,
    description="Identifier can be either the customer's id, email or cpf.",
)
async def get_customer(identifier: str) -> Union[Customer, None]:
    customer = await CustomersUseCasesController.get_customer_by_identifier(
        identifier=identifier
    )
    return customer


handler = Mangum(app, lifespan="off")

if __name__ == "__main__":
    uvicorn_app = f"{os.path.basename(__file__).removesuffix('.py')}:app"
    uvicorn.run(uvicorn_app, host="0.0.0.0", port=8000, reload=True)
