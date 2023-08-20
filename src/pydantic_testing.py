from pydantic import BaseModel, validator
from datetime import datetime
from data_model.sample_data import measurement_df, measurement_obj
import pandas as pd


class ParticleMeasurementPydantic(BaseModel):
    timestamp: datetime
    particle: str
    energy: float

    @validator("particle")
    def validate_particle(cls, v):
        assert v in ["electron", "proton", "neutron"]
        return v

    @validator("energy")
    def validate_energy(cls, v):
        assert v > 0
        return v


if __name__ == '__main__':
    
    # Validate obj ++
    validated_data = ParticleMeasurementPydantic(**measurement_obj.__dict__)
    print("Validate obj:\n", validated_data)


    # Validate df --
    
    # print(measurement_df.to_dict(orient="list"))
    # print(measurement_df.to_dict(orient="records"))

    records = measurement_df.to_dict(orient='records')
    particles = [ParticleMeasurementPydantic(**record) for record in records]
    print("Validate df:\n", particles)