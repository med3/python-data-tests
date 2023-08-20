import pandas as pd

data = {
    "timestamp": ["2023-08-01 12:01", "2023-08-01 12:02", "2023-08-01 12:03"],
    "particle": ["electron", "proton", "neutron"],
    "energy": [0.511, 938.272088, 939.565413]  # energy in MeV
}

measurement_df = pd.DataFrame(data)


class ParticleMeasurement:
    def __init__(self, timestamp, particle, energy):
        self.timestamp = timestamp
        self.particle = particle
        self.energy = energy

measurement_obj = ParticleMeasurement("2023-08-01 12:01", "electron", 0.511)
