from typing import Optional

from pydantic import BaseModel

from src.models.products import Product
from src.models.users import User


class ShoppingCart(BaseModel):
    """
    This class is a model for the table ShoppingCart

    Attributes:
    id (int): This camp is an int which represents the id
    user (User): This camp is a foreigner key which represents the table User
    product (Product): This camp is a foreigner key which represents the table Product
    total_value (float): This camp is a float which represents the monetary value of all products
    amount (int): This camp represents the amount of products
    observations (Optional[str]): This camp represents the observations made at the request
    address (str): This camp represents the address for the shipping
    shipping (bool): This camp represents if the product must be shipped

    """

    id: int
    user: User
    product: Product
    total_value: float
    amount: int
    observations: Optional[str] = "Sem observações."
    address: str
    shipping: bool = False
