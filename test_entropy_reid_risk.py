import pandas as pd
from entropy_reid_risk import calc_parameters

## Test Case 1
# q1 : Quasi Identifier
original_df1 = pd.DataFrame({'No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                    'q1': [88, 21, 90, 69, 25, 30, 60, 42, 14, 28, 35, 44, 15, 55, 72, 18]})

anonymized_df1 = pd.DataFrame({'No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                    'q1': [90, 22, 88, 71, 24, 28, 58, 39, 16, 30, 42, 46, 14, 61, 71, 20]})

## Test Case 2 : Without anonymization
# q1 : Quasi Identifier
original_df2 = pd.DataFrame({'No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                    'q1': [88, 21, 90, 69, 25, 30, 60, 42, 14, 28, 35, 44, 15, 55, 72, 18]})

anonymized_df2 = pd.DataFrame({'No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                    'q1': [88, 21, 90, 69, 25, 30, 60, 42, 14, 28, 35, 44, 15, 55, 72, 18]})


 calc_parameters(original_df1,anonymized_df1,'q1')
#calc_parameters(original_df2,anonymized_df2,'q1')
