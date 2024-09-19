import os
from code.gateways.repositories.beanie.documents.customer_document import (
    CustomerDocument,
)
from typing import Any

from dotenv import load_dotenv

load_dotenv()


MONGODB_URL = os.getenv("MONGODB_URL")

DOCUMENT_MODELS: list[Any] = [
    CustomerDocument,
]
