from datetime import datetime
from dataclasses import dataclass, field
from typing import List

from data_model.sample_data import measurement_obj, measurement_df

def validate_email(email: str) -> str:
    if "@" not in email or "." not in email.split("@")[1]:
        raise ValueError(f"Invalid email: {email}")
    return email

def validate_age(age: int) -> int:
    if not (0 <= age <= 100):
        raise ValueError(f"Invalid age: {age}")
    return age

@dataclass
class User:
    id: List[int]
    name: List[str]
    email: List[str] = field(metadata={"validate": validate_email})
    age: List[int] = field(metadata={"validate": validate_age})

    def __post_init__(self):
        for email in self.email:
            validate_email(email)
        for age in self.age:
            validate_age(age)


@dataclass
class ParticleMeasurementDC:
    timestamp: str
    particle: str
    energy: float

    def __post_init__(self):
        datetime.strptime(self.timestamp, "%Y-%m-%d %H:%M")
        assert self.particle in ["electron", "proton", "neutron"]
        assert self.energy > 0



if __name__ == '__main__':
    
    
    # User validation
    user = User(id=[1, 2, 3], name=["Alice", "Bob", "Charlie"], 
            email=["alice@example.com", "bob@domain.com", "charlie@web.net"], 
            age=[25, 30, 35])
    
    
    # sample_data validation
    sample_data = {
        "timestamp": "2023-08-01 12:01",
        "particle": "electron",
        "energy": 1.5
        }
    
    sample_particle = ParticleMeasurementDC(**sample_data)
    
    
    # Validate df --
    records = measurement_df.to_dict(orient='records')
    particles = [ParticleMeasurementDC(**record) for record in records]


    # Validate obj ++
    validated_data = ParticleMeasurementDC(**measurement_obj.__dict__)
