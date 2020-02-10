#home use, pocket highway, hand highwat


states = ('hu', 'hp', 'hh')


#no range, just numero -----for every oi
raw_observation = {'meanSignalLength': 1.0, 'amplCor': .97, 'syncVar' : 3, 'metr6.velSum': 1}
new_raw_observation = {'meanSignalLength': 0, 'amplCor': 0, 'syncVar' : 0, 'metr6.velSum': 0}

#only looking at a sequence of two observations at a given period of time

#input an additional observation
def updateObservation( meanSignalLength, amplCor, syncVar, velSum):

    ob_s={}
    ob_s['meanSignalLength'] = meanSignalLength
    ob_s['amplCor'] = amplCor
    ob_s['syncVar'] = syncVar
    ob_s['metr6.velSum'] = velSum
    return ob_s

"""
[{first observation}, {secound observation}]
[{secound observation}, {third observation}]

i am trying to write a method to return a sequence of two observations (that can be updated based on parameter input)

"""
def getSeq(meanSignalLength, amplCor, syncVar, velSum, raw_observation):
    seq = [raw_observation, updateObservation(meanSignalLength, amplCor, syncVar, velSum)]
    new_raw_observation = updateObservation(meanSignalLength, amplCor, syncVar, velSum)
    raw_observation = new_raw_observation
    print(raw_observation)
    print(seq)
    return seq



getSeq(1,1,1,1, raw_observation)
getSeq(2,2,2,2, raw_observation)


"""ob_s_f = updateObservatiYon( 2,2,2,2)
raw_observation = ob_s_f[1]
print(ob_s_f)

print(raw_observation)
ob_s_f = updateObservation( 1,1,1,1)
print(ob_s_f)"""






def getRange(observations):
    range = ''
    for observation in observations:
            if observation == 'amplCor':
                if 0 <= raw_observation[observation] <= .465:
                    range = 'A'
                if .465 <= raw_observation[observation] <= .735:
                    range = 'B'
                if .735 <= raw_observation[observation] <= 1:
                    range = 'C'
            if observation == 'meanSignalLength':
                if .079 <= raw_observation[observation] <= .479:
                    range = 'A'
                if .479 <= raw_observation[observation] <= .879:
                    range = 'B'
                if .879 <= raw_observation[observation]:
                    range = 'C'
            if observation == 'syncVar':
                if 0 <= raw_observation[observation] <= 1.5:
                    range = 'A'
                if 1.5 <= raw_observation[observation] <= 3.5:
                    range = 'B'
                if 3.5 <= raw_observation[observation]:
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
            'amplCor' : {'A' : 0.008, 'B' : 0.2606, 'C' : 0.7580},
            'syncVar' : {'A' : 0.9406, 'B' : 0.0618, 'C' : 0.0352},
            'metr6.velSum' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2}
    },
    'hp' : {'meanSignalLength' : {'A' : 0.5682, 'B' : 0.7672, 'C' : 0.0437},
            'amplCor' : {'A' : 0.1825, 'B' : 0.5307, 'C' : 0.3706},
            'syncVar' : {'A' : 0.9738, 'B' : 0.0263, 'C' : 0.0038},
            'metr6.velSum' : {'A' : 0.3, 'B' : 0.5, 'C' : 0.2}
    },
    'hh' : {'meanSignalLength' : { 'A' : 0.8247, 'B' : 0.1635, 'C' : 0.0382},
            'amplCor' : {'A' : 0.0193, 'B' : 0.0324, 'C' : 0.9563},
            'syncVar' : {'A' : 0.987, 'B' : 0.0112, 'C' : 0.0087},
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
