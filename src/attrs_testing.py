import attr
from typing import List

from data_model.sample_data import measurement_obj, measurement_df

@attr.s
class User:
    id = attr.ib(type=List[int])
    name = attr.ib(type=List[str])
    email = attr.ib(type=List[str], validator=attr.validators.deep_iterable(member_validator=attr.validators.matches_re(r"[^@]+@[^@]+\.[^@]+")))
    age = attr.ib(type=List[int], validator=attr.validators.deep_iterable(member_validator=attr.validators.in_(range(0, 101))))

@attr.s
class ParticleMeasurementAttrs:
    timestamp = attr.ib(validator=attr.validators.matches_re(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}"))
    particle = attr.ib(validator=attr.validators.in_(["electron", "proton", "neutron"]))
    energy = attr.ib(validator=attr.validators.instance_of(float))

    @energy.validator
    def check_energy(self, attribute, value):
        if value <= 0:
            raise ValueError("Energy should be positive")


if __name__ == '__main__':
    
    # User validation
    user = User(id=[1, 2, 3], name=["Alice", "Bob", "Charlie"], 
            email=["alice@example.com", "bob@domain.com", "charlie@web.net"], 
            age=[25, 30, 35])


    # sample_data validation
    sample_data = {
        "timestamp": "1992-05-01 00:00",
        "particle": "electron",
        "energy": 1.5
        }
    
    validated_sample_data = ParticleMeasurementAttrs(**sample_data)
    
    
    # Validate df --
    records = measurement_df.to_dict(orient='records')
    particles = [ParticleMeasurementAttrs(**record) for record in records]


    # Validate obj ++
    validated_data = ParticleMeasurementAttrs(**measurement_obj.__dict__)

