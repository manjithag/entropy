import pandas as pd
import numpy as np

def normal_dist(x, mean, sd):

    prob_density = 1/(np.sqrt(2 * np.pi) * sd) * np.exp(-0.5*((x-mean)/sd)**2)

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
        annonymized_series = annonymized_df[quasi_identifier]

        #print(original_series)

        entropy_list =[]
        k_eff_list = []
        ecm = 0
        sd = 10


        for si in original_series:

            entropy_h_rs = 0
            for ri in annonymized_series:

                p_rs = normal_dist(ri,si,sd)
                log_p_rs = np.log2(p_rs)
                entropy_h_rs += p_rs * log_p_rs

            entropy_h_rs = -1 * entropy_h_rs
            k_eff_s = 2 ** entropy_h_rs

            entropy_list.append(entropy_h_rs)
            k_eff_list.append(k_eff_s)

            ecm += 1 / k_eff_s

        output_df = pd.DataFrame({'H(R|s)' : entropy_list, 'k eff' : k_eff_list})

    return output_df, ecm











