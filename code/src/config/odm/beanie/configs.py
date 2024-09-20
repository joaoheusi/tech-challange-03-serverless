import os
from typing import Any

from dotenv import load_dotenv
from src.gateways.repositories.beanie.documents.customer_document import (
    CustomerDocument,
)

load_dotenv()


MONGODB_URL = os.getenv("MONGODB_URL")

DOCUMENT_MODELS: list[Any] = [
    CustomerDocument,
]
