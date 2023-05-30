import pandas as pd
from entropy_reid_risk import calc_k_eff_s

## Test Case 1
original_df = pd.DataFrame({'No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                    'q1': [88, 21, 90, 69, 25, 30, 60, 42, 14, 28, 35, 44, 15, 55, 72, 18]})

annonymized_df = pd.DataFrame({'No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                    'q1': [90, 22, 88, 71, 24, 28, 58, 39, 16, 30, 42, 46, 14, 61, 71, 20]})


print(calc_k_eff_s(original_df,annonymized_df))

#print(original_df)
#original_series = original_df['s1']
#print(original_series)