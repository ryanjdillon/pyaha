
SEAL_CFG = {'w_adult_m': 75, # kg
            'w_adult_f': 50, # kg
            'w_birth_m': 10, # kg
            'w_birth_f': 10, # kg
            'w_adult_f': 50, # kg
           }

def sample_maturity(age, sex, biomass):
    '''Sample maturity state using logistic function of age, sex, biomass'''
    import random
    from scipy.special import expit

    #TODO generate curve of sex maturity for species
    ## Male maturity stage
    #if sex == 1:
    #    mature = expit()
    ## Femail maturity stage
    #elif sex == 0:
    #    mature = expit()
    #else:
    #    raise ValueError, 'Sex value {} incorrect'.format(sex)

    return False


def sample_biomass(age, sex):
    '''Sample biomass at age'''
    #TODO generage curve of biomass for species at age

    return 10
