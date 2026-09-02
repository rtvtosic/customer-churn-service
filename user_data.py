from pydantic import BaseModel, ConfigDict, Field
from typing import Literal


class UserData(BaseModel):
    """Данные о клиенте"""

    model_config = ConfigDict(populate_by_name=True)

    gender: Literal['Female', 'Male'] = Field(alias="gender")
    partner: Literal['Yes', 'No'] = Field(alias="Partner")
    dependents: Literal['Yes', 'No'] = Field(alias="Dependents")
    phone_service: Literal['Yes', 'No'] = Field(alias="PhoneService")
    multiple_lines: Literal['Yes', 'No'] = Field(alias="MultipleLines")
    online_security: Literal['Yes', 'No'] = Field(alias="OnlineSecurity")
    online_backup: Literal['Yes', 'No'] = Field(alias="OnlineBackup")
    device_protection: Literal['Yes', 'No'] = Field(alias="DeviceProtection")
    tech_support: Literal['Yes', 'No'] = Field(alias="TechSupport")
    streaming_tv: Literal['Yes', 'No'] = Field(alias="StreamingTV")
    streaming_movies: Literal['Yes', 'No'] = Field(alias="StreamingMovies")
    paperless_billing: Literal['Yes', 'No'] = Field(alias="PaperlessBilling")
    internet_service: Literal['DSL', 'Fiber optic', 'No'] = Field(alias="InternetService")
    contract: Literal['Month-to-month', 'One year', 'Two year'] = Field(alias="Contract")
    payment_method: Literal['Electronic check', 'Mailed check', 
                            'Bank transfer (automatic)', 'Credit card (automatic)'] = Field(alias="PaymentMethod")
    senior_citizen: Literal[0, 1] = Field(alias="SeniorCitizen")
    tenure: int = Field(ge=0, alias="tenure")
    monthly_charges: float = Field(ge=0, alias="MonthlyCharges") 
    total_charges: float = Field(ge=0, alias="TotalCharges")
