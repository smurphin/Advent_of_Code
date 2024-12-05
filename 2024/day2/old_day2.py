import pandas as pd
import numpy as np
import time

t1 = time.time()
csv_file = "input.txt"

df = pd.read_csv(csv_file, header=None, sep='\s+')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

def check_safety(row):
    cleaned_row = row.dropna() #remove all NaN entries caused by different row lengths to avoid returning false when checking for monotonicity

    has_repeats = any(cleaned_row.value_counts()[cleaned_row.value_counts() > 1].index != 0)

    if has_repeats: #check for repeat numbers in row
        return 'repeat_unsafe' 
    
    """Checks if the difference between any value and its previous value in a row is greater than 3."""
    if cleaned_row.is_monotonic_increasing or cleaned_row.is_monotonic_decreasing:
        if (cleaned_row.diff().abs() > 3).any():
            return 'high_difference_unsafe'
        else:
            return 'safe'
    else:
        return 'up_and_down_unsafe'
    

#print(df.diff(axis=1))

#print(df.apply(check_safety, axis=1))

safety_results = df.apply(check_safety, axis=1)

num_safe = safety_results[safety_results == 'safe'].count()

print(f"Number of safe levels = {num_safe}")


#### part B ###

def safety_dampener(row):
    cleaned_row = row.dropna() #remove all NaN entries caused by different row lengths to avoid returning false when checking for monotonicity
    
    num_duplicates = cleaned_row.duplicated().sum()

    if num_duplicates > 1:  # More than one duplicate
        return 'duplicate_unsafe'
    
    if num_duplicates == 1:  # exactly one duplicate
        if (cleaned_row.diff().abs() > 3).any():
            return 'duplicate_unsafe'
        if cleaned_row.is_monotonic_increasing or cleaned_row.is_monotonic_decreasing:
            if (cleaned_row.diff().abs() > 3).any():
                return 'high_difference_unsafe'
        else:
            return 'safe'
    else:
        return 'up_and_down_unsafe'
    
    cleaned_row = cleaned_row.drop_duplicates(keep='first')
    
    #print(cleaned_row)

    """Checks if the difference between any value and its previous value in a row is greater than 3."""
    if (cleaned_row.diff().abs() > 3).any():
        # Drop first value if its difference is > 3
        if abs(cleaned_row.iloc[0] - cleaned_row.iloc[1]) > 3:  
            cleaned_row = cleaned_row.iloc[1:]
            # Recheck differences after dropping
            if (cleaned_row.diff().abs() > 3).any():  
                return 'high_difference_unsafe'
            else:
                return 'safe'

        # Drop last value if its difference is > 3
        elif abs(cleaned_row.iloc[-1] - cleaned_row.iloc[-2]) > 3:  
            cleaned_row = cleaned_row.iloc[:-1]
            # Recheck differences after dropping
            if (cleaned_row.diff().abs() > 3).any():  
                return 'high_difference_unsafe'
            else:
                return 'safe'
            
        else:
            return 'high_difference_unsafe'

    else:
        return 'safe'


#print(df.apply(safety_dampener, axis=1))

damp_safety_results = df.apply(safety_dampener, axis=1)

damp_num_safe = damp_safety_results[damp_safety_results == 'safe'].count()

print(f"Number of safe levels = {damp_num_safe}")

#print(df)

#print(df.diff(axis=1))

# Calc execution time
t2 = time.time()
print(f"Executed in {t2 - t1:0.4f} seconds")
