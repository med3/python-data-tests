
import pandera as pa
import pandas as pd
from data_model.sample_data import measurement_df, measurement_obj


### Structured data validation ---




# Define a validation schema
schema_v1 = pa.DataFrameSchema({
    'timestamp': pa.Column(pa.DateTime),
    'particle': pa.Column(pa.String, checks=pa.Check.isin(["electron", "proton"])),
    'energy': pa.Column(pa.Float, checks=pa.Check.greater_than(0))
})



### Tabular data validation +++

schema_v2 = pa.DataFrameSchema({
    "timestamp": pa.Column(pa.String, checks=pa.Check.str_matches(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}")),
    "particle": pa.Column(pa.String, checks=pa.Check.isin(["electron", "proton", "neutron"])),
    "energy": pa.Column(pa.Float, checks=pa.Check.gt(0))
})



if __name__ == '__main__':
    
    
    # Validate object df --
    # Convert the object to a DataFrame
    measurement_obj_df = pd.DataFrame([{
        'timestamp': measurement_obj.timestamp,
        'particle': measurement_obj.particle,
        'energy': measurement_obj.energy
    }])
    # Convert the 'timestamp' column to datetime
    measurement_obj_df['timestamp'] = pd.to_datetime(measurement_obj_df['timestamp'])
    
    measurement_validated_df = schema_v1.validate(measurement_obj_df)
    print("Validate converted object:\n", measurement_validated_df)
    
    
    # Validate df ++
    validated_df = schema_v2.validate(measurement_df)
    print("Validate df:\n", validated_df)