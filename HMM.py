#home use, pocket highway, hand highwat
states = ('hu', 'hp', 'hh')

#operational indicators
o_i = ('meanSignalLenght', 'amplCor', 'syncVar', 'metr6.velSum')

'''
an observation is defined by the range that a value of an operational indicator falls in
we are going to look at a window of 4 observations at a time, where each observation is a value of one of the 4 operational indicators
struggle: getting the emission probilities 

'''




#how the heck do u pass a varible(integer) into a JSON object?? do we even need to do this?

#no range, just numero -----for every oi
raw_observation = {'meanSignalLength': val, ect}

#range-------for every oi
new_observation = {'meanSignalLength': {'A', 'B', 'C'}, ect}

'''
i want to pass in a value for an observation into getObs 
getObs is going to assign a range (A, B, C) to the operational indicator 
where a = low range, b = middle range and c = high range
the getObs methode will return the operational indicator with the correclty assigned range
'''
def getObs(o_i, val)
    for i, oi in enumerate(o_i):
        if(oi=='meanSignalLength')
            if(val is in lower range)
                range = 'A'
                return new_observation[o_i][range]


int_prob = {
    'hu' : 0.5,
    'hp' : 0.3,
    'hh' : 0.2
}

trans_prob = {
    'hu': { 'hu' : 0.8, 'hh' : 0.1, 'hp' : 0.1 },
    'hh': { 'hu' : 0.15, 'hh' : 0.8, 'hp' : 0.05 },
    'hp': { 'hu' : 0.25, 'hh' : 0.25, 'hp' : 0.05}
}

# given the state, what is the probility of a certain observation?
emit_prob_indv = {
    'hu' : {'meanSignalLength' : { 'A' : 0.3, 'B' : 0.5, 'C' : 0.2},
            'amplCor' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2},
            'syncVar' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2},
            'metr6.velSum' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2}
    },
    'hh' : {'meanSignalLength' : { 'A' : 0.3, 'B' : 0.5, 'C' : 0.2},
            'amplCor' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2},
            'syncVar' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2},
            'metr6.velSum' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2}
    },
    'hh' : {'meanSignalLength' : { 'A' : 0.3, 'B' : 0.5, 'C' : 0.2},
            'amplCor' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2},
            'syncVar' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2},
            'metr6.velSum' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2}
    }
}


def int_prob(state):
    return int_prob[state]

def trans_prob(prevstate, state):
    return trans_prob[prevstate,state]


def emit_prob(state, getObs(o_i, val))
   '''
   use getObs to find the "new observation"
   for each state find the emiision probility of the new observation and then multiply the new observations
   asojsadfhdf i am probly over complicating this its 5 am good night
   '''


def forward(states, observations):
    alpha=[{}]
    for state in states:
        alpha[0][state]=int_prob(state)*emit_prob()
    for observation in observations:
        for state in states:
            #observation - 1 --> previous observation, same thing for state
           alpha[observation][state] += alpha[observation-1][state-1] * trans_prob(state-1, state) * emit_prob()
    alpha_prob = alpha[observation][state]
return alpha_prob