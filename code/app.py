import os
from contextlib import asynccontextmanager
from typing import Any, Union

import uvicorn
from beanie import init_beanie
from fastapi import FastAPI
from mangum import Mangum
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from src.config.odm.beanie.configs import DOCUMENT_MODELS, MONGODB_URL
from src.controllers.customers_controller import CustomersUseCasesController
from src.entities.customer import Customer


async def start_beanie() -> None:
    print("Starting beanie")
    database: AsyncIOMotorDatabase[Any] = AsyncIOMotorClient(MONGODB_URL).fiap
    await init_beanie(database=database, document_models=DOCUMENT_MODELS)
    print("Finished starting beanie")


@asynccontextmanager
async def lifespan(app: FastAPI):  # type: ignore
    await start_beanie()
    yield


app = FastAPI(lifespan=lifespan)


@app.get(
    "/api/customer/{identifier}",
    response_model=Customer,
    description="Identifier can be either the customer's id, email or cpf.",
)
async def get_customer(identifier: str) -> Union[Customer, None]:
    await start_beanie()
    customer = await CustomersUseCasesController.get_customer_by_identifier(
        identifier=identifier
    )
    return customer


handler = Mangum(app, lifespan="off")

if __name__ == "__main__":
    uvicorn_app = f"{os.path.basename(__file__).removesuffix('.py')}:app"
    uvicorn.run(uvicorn_app, host="0.0.0.0", port=80, reload=True)
