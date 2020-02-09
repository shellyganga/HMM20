#home use, pocket highway, hand highwat
states = ('hu', 'hp', 'hh')


#no range, just numero -----for every oi
raw_observation = {'meanSignalLength': 1.0, 'amplCor': .97, 'syncVar' : 3, 'metr6.velSum': 1}

#only looking at a sequence of two observations at a given period of time
def updateObservation( meanSignalLength, amplCor, syncVar, velSum, raw_observation):
    ob_s2 = []
    ob_s2.append(raw_observation)
    ob_s={}
    ob_s['meanSignalLength'] = meanSignalLength
    ob_s['amplCor'] = amplCor
    ob_s['syncVar'] = syncVar
    ob_s['metr6.velSum'] = velSum
    ob_s2.append(ob_s)
    ob_s_f = ob_s2
    raw_observation = ob_s_f[1]
    return ob_s_f

def getRange(observations):
    range = ''
    for observation in observations:
            if observation == 'meanSignalLength':
                if raw_observation[observation] in range(.078,.48):
                    range = 'A'
                if raw_observation[observation] in range(.478, .880):
                    range = 'B'
                if raw_observation[observation] in range(.878, 1.480):
                    range = 'C'
            if observation == 'amplCor':
                if raw_observation[observation] in range(.104, .466):
                    range = 'A'
                if raw_observation[observation] in range(.464, .735):
                    range = 'B'
                if raw_observation[observation] in range(.735, .975):
                    range = 'C'
    return range


inti_prob = {
    'hu' : 0.5,
    'hp' : 0.3,
    'hh' : 0.2
}

transi_prob = {
    'hu': { 'hu' : 0.8, 'hh' : 0.1, 'hp' : 0.1 },
    'hp': { 'hu' : 0.15, 'hh' : 0.8, 'hp' : 0.05 },
    'hh': { 'hu' : 0.25, 'hh' : 0.25, 'hp' : 0.05}
}

# given the state, what is the probility of a certain observation?
#A=low, b= med, c= high
emit_prob_indv = {
    'hu' : {'meanSignalLength' : { 'A' : 0.6195, 'B' : 0.3066, 'C' : 0.076},
            'amplCor' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2},
            'syncVar' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2},
            'metr6.velSum' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2}
    },
    'hp' : {'meanSignalLength' : {'A' : 0.5682, 'B' : 0.5, 'C' : 0.2 },
            'amplCor' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2},
            'syncVar' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2},
            'metr6.velSum' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2}
    },
    'hh' : {'meanSignalLength' : { 'A' : 0.8247, 'B' : 0.1635, 'C' : 0.0382},
            'amplCor' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2},
            'syncVar' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2},
            'metr6.velSum' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2}
    }
}



def int_prob(state):
    return inti_prob[state]

def trans_prob(prevstate, state):
    return transi_prob[prevstate][state]


def emit_prob(state, raw_observations, rangE):
    value = 1
    for observation in raw_observations:
        value *= emit_prob_indv[state][observation][rangE]
    return value


def forward(sequence):
    sequence_length = len(sequence)
    alpha = [{}]
    for state in states:
        alpha[0][state] = int_prob(state) * emit_prob(state, sequence[0], getRange(sequence[0]))
    for index in range(1, sequence_length):
        alpha.append({})
        for state_to in states:
            prob = 0
            for state_from in states:
                prob += alpha[index - 1][state_from] * trans_prob(state_from, state_to)
            alpha[index][state_to] = prob * emit_prob(state_to, sequence[index], getRange(sequence[0]))
    return alpha[1]


sequenceOfOb = updateObservation(1,1,1,1,raw_observation)
print(sequenceOfOb)
print(forward(sequenceOfOb))
