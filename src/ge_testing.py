import great_expectations as ge
import pandas as pd

from data_model.sample_data import measurement_df, measurement_obj



# data = {
#     "timestamp": ["2023-08-01 12:01", "2023-08-01 12:02", "2023-08-01 12:03"],
#     "particle": ["electron", "proton", "neutron"],
#     "energy": [0.511, 938.272088, 939.565413]  # energy in MeV
# }

# df = pd.DataFrame(data)


if __name__ == '__main__':
    
    # Validate object df ---
    # Convert the object to a DataFrame
    measurement_obj_df = pd.DataFrame([{
        'timestamp': measurement_obj.timestamp,
        'particle': measurement_obj.particle,
        'energy': measurement_obj.energy
    }])    
    
    # Convert the 'timestamp' column to datetime
    measurement_obj_df['timestamp'] =  pd.to_datetime(measurement_obj_df['timestamp']).dt.strftime('%Y-%m-%d %H:%M')
    print(measurement_obj_df)
    
    measurement_obj_df_ge = ge.from_pandas(measurement_obj_df)

    measurement_obj_df_ge.expect_column_values_to_match_regex("timestamp", r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}")
    measurement_obj_df_ge.expect_column_values_to_be_in_set("particle", ["electron", "proton", "neutron"])
    measurement_obj_df_ge.expect_column_values_to_be_between("energy", 0, None)
    
    
    # Validate df ++
    df_ge = ge.from_pandas(measurement_df)

    df_ge.expect_column_values_to_match_regex("timestamp", r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}")
    df_ge.expect_column_values_to_be_in_set("particle", ["electron", "proton", "neutron"])
    df_ge.expect_column_values_to_be_between("energy", 0, None)
