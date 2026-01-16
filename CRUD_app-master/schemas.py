from pydantic import BaseModel
from typing import Optional

# Схема для создания элемента
class ItemCreate(BaseModel):
    title: str
    description: Optional[str] = None
    price: Optional[int] = None

# Схема для обновления элемента
class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None

# Схема для ответа (чтения)
class ItemResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    price: Optional[int]
    
    class Config:
        orm_mode = True