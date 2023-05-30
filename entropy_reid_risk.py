###  This method of calculating risk of re-identification refers to the research paper of
###  'M. Bezzi, “An Entropy based method for Measuring Anonymity'.

import pandas as pd
import numpy as np
def normal_dist(x, mean, sd):
    ## Calculating the probablity value according to normal distribution
            ##  Arguments   : Variable (x), Mean, Standard Diviation (sd)
            ##  Returns     : probability

    prob_density = 1/(np.sqrt(2 * np.pi) * sd) * np.exp(-0.5*((x-mean)/sd)**2)

    return prob_density

def calc_parameters(original_df : pd.DataFrame, anonymized_df : pd.DataFrame, quasi_identifier : str ):

    ## Calculate following parameters
            # Entropy = H(R|s)
            # k_eff (s)
            # ECM
            # NTM
    ## Arguments : Original and Anonymized datasets, column name of quasi identifier

    no_records_original = original_df.shape[0]
    no_records_anonymized = anonymized_df.shape[0]

    if no_records_original != no_records_anonymized:
        print('Error : No of records are different in original and annonymized datasets')

    else:
       # quasi_identifier = 'q1'

        original_series = original_df[quasi_identifier]
        anonymized_series = anonymized_df[quasi_identifier]

        entropy_list =[]        # A list to store entropy values of each record
        k_eff_list = []         # A list to store k_eff values of each record
        ecm = 0
        ntm = 0
        sd = 10


        for i in range(no_records_original):    # Looping through records in original data set
            si = original_series[i]

            entropy_h_rs = 0                    # Entropy = H(R|s)
            p_rs_list = []                      # A list to store P(R|s)
            for ri in anonymized_series:        # Looping through records in anonymized data set

                p_rs = normal_dist(ri,si,sd)    # Probability for individual records
                log_p_rs = np.log2(p_rs)
                entropy_h_rs += p_rs * log_p_rs

                p_rs_list.append(p_rs)          #  Storing P(r|s) for a 's' value of each records (For NTM)

            entropy_h_rs = -1 * entropy_h_rs    # Calculating H(R|s) = SIGMA {P(R|s) x log2[P(R|s)]} for a 's' value
            k_eff_s = 2 ** entropy_h_rs         # Calculating k_eff for a 's' value

            entropy_list.append(entropy_h_rs)   # Entropy list for all the 's' values
            k_eff_list.append(k_eff_s)          # k_eff list for all the 's' values

            ecm += 1 / k_eff_s                  # Calculating ECM for a 's' value

            ## Calculation of NTM
            max_prob_index = p_rs_list.index(max(p_rs_list))        # Getting index of the maximum P(r|s) for a 's'

            if max_prob_index == i:             # Verification if the maximum P(r|s) corresponds to an actual match
                ntm += 1
                print(i)

        output_df = pd.DataFrame({'H(R|s)' : entropy_list, 'k eff' : k_eff_list})

        print(output_df)
        print('ECM = ' + str(ecm))
        print('NTM = ' + str(ntm))

    #return output_df, ecm, ntm











