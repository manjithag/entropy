import pandas as pd
import numpy as np

def normal_dist(x, mean, sd):

    prob_density = (np.pi*sd) * np.exp(-0.5*((x-mean)/sd)**2)

    return prob_density


def calc_k_eff_s(original_df : pd.DataFrame, annonymized_df : pd.DataFrame):

    no_records_original = original_df.shape[0]
    no_records_annonymized = annonymized_df.shape[0]

    #print(original_df)

    if no_records_original != no_records_annonymized:
        print('Error : No of records are different in original and annonymized datasets')

    else:

        quasi_identifier = 'q1'

        original_series = original_df[quasi_identifier]
        #annonymized_series = annonymized_df[quasi_identifier]

        #print(original_series)

        sd = 10


        for si in original_series:

            entropy_h_rs = 0
            for ri in annonymized_df:

                p_rs = normal_dist(ri,si,sd)
                log_p_rs = np.log2(p_rs)
                entropy_h_rs += p_rs * log_p_rs

            print(entropy_h_rs)














