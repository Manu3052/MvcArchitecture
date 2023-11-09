from pydantic import BaseModel


class Product(BaseModel):
    """
    This class is a model for the table Product

    Attributes:
        id (int): This camp is an int which represents the id
        name (str): This camp is a string which represents the name
        details (str): This camp is a string with the details
        price (float):  This camp is a float which represents the value
        amount (int): This camp is an int representing the amount of products left
        availability (bool):  This camp is a bool representing the availability of the product
    """

    id: int
    name: str
    details: str
    price: float
    amount: int
    availability: bool = False
