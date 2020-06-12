

def calc_bayes(prior_A, prob_B_given_A, prob_B):
    return (prior_A * prob_B_given_A) / prob_B


if __name__ == "__main__":
    prob_cancer = 1 / 100000
    
    # prob_cancer = 0.09  # para dado un segundo test
    prob_sintom_given_cancer = 1
    prob_sintom_given_no_cancer = 10 / 99999
    prob_no_cancer = 1 - prob_cancer



    prob_sintom = (prob_sintom_given_cancer * prob_cancer) + (prob_sintom_given_no_cancer * prob_no_cancer)

    print(prob_cancer)
    print(prob_sintom_given_cancer)
    print(prob_sintom_given_no_cancer)
    print(prob_no_cancer)
    print(prob_sintom)

    prob_cancer_given_sintom = calc_bayes(
        prob_cancer,
        prob_sintom_given_cancer,
        prob_sintom
    )
    print('probabilidad del cancer dado sintomas')
    print(prob_cancer_given_sintom)

