from pydantic import BaseModel, Field
from typing import Literal


class UserData(BaseModel):
    """Данные о клиенте"""

    gender: Literal['Female', 'Male']
    partner: Literal['Yes', 'No']
    dependents: Literal['Yes', 'No']
    phone_service: Literal['Yes', 'No']
    multiple_lines: Literal['Yes', 'No']
    online_security: Literal['Yes', 'No']
    online_backup: Literal['Yes', 'No']
    device_protection: Literal['Yes', 'No']
    tech_support: Literal['Yes', 'No']
    streaming_tv: Literal['Yes', 'No']
    streaming_movies: Literal['Yes', 'No']
    paperless_billing: Literal['Yes', 'No']
    internet_service: Literal['DSL', 'Fiber optic', 'No']
    contract: Literal['Month-to-month', 'One year', 'Two year']
    payment_method: Literal['Electronic check', 'Mailed check', 
                            'Bank transfer (automatic)', 'Credit card (automatic)']
    senior_citizen: Literal[0, 1]
    tenure: int = Field(ge=0)
    monthly_charges: float = Field(ge=0)
    total_charges: float = Field(ge=0)