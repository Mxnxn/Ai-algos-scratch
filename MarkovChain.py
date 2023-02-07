import numpy as np

defaultStates =  {
            0:'Snowy',
            1:'Rainy',
            2:'Sunny'
            }

class MarkovChain():
    def __init__(self, states, transition_matrix):
        '''
        Initiate Class Objects

        Parameters
        ---------------------
        states : dict
            takes total numbers of state such as Rainy, Snowy, ...
        
        transition_matrix : 2d array
            probability distribution for each state present in states.

        Return
        ____________________
        None        
        '''
        self.states = states
        self.transition_matrix = transition_matrix
        self.pi = np.array([0, 0, 0])

    def randomChain(self,n_sequence):
        '''
        Provide chain or list that has randomly selected states from defined states.

        Parameters
        ---------------------
        n_sequence : int
            takes a integer defining length of sequence
        

        Return
        ____________________
        sequence : list
            a list that holds random states     
        '''
        n = n_sequence
        start_state = 0
        curr_weather = start_state
        sequence = []
        while n-1:
            # it provides state from [0, 1, 2] while considering transion_matrix
            curr_weather = np.random.choice([0, 1, 2], p=self.transition_matrix[curr_weather])

            # appending each state.
            sequence.append(curr_weather)
            n-=1

        return sequence

    def genMCS(self,steps = 10000, initialState = 0):
        '''
        Calculates PI (Probability Distribution) for each instances

        Parameters
        ---------------------
        steps : int
            a integer for defining montecarlo simulations
        
        initialState : int, Optional
            a integer to define from where to start.
        
        Return
        ____________________
        None     
        '''
        steps = steps
        start_state = initialState
        curr_weather = start_state
        
        # initiating probability count of inital step with 1
        self.pi[start_state] = 1

        i = 0
        # iterate through the count.
        while i < steps:
            curr_weather = np.random.choice([0,1,2], p=self.transition_matrix[curr_weather])
            
            # increment by 1 for each iteration of state snowy = [1 0 0], again snowy [2 0 0]
            self.pi[curr_weather]+=1
            i +=1

        # dividing by total numbers of steps to get probability.
        self.pi = self.pi/steps
        print("π = ", self.pi )
        return None
    
    def randomProbability(self,sequence):
        '''
        Provide probability for given sequence.

        Parameters
        ---------------------
        sequence : list
            a list having states (integer) to calculate their probability
            it should be greater than or equals to 2
        
        Return
        ____________________
        prob: float
            probability for given sequence     
        '''
        start_state = sequence[0]
        prob = self.pi[start_state]
        
        #initial prev and curr_state both will set to sequence's first state.
        prev_state, curr_state = start_state, start_state
        
        for i in range(1, len(sequence)):
            curr_state = sequence[i]
            
            # pi dot multiplication with transitional matrix
            # pi[snowy]A[previousWeather, snowy] = prob
            prob *= self.transition_matrix[prev_state][curr_state]
            
            #chaging current state to prev for next iteration
            prev_state = curr_state
        return prob

if __name__ == '__main__':
    # Providing matrix, a graph of probability
    chain = MarkovChain(defaultStates, np.array([[0.6, 0.2, 0.2], [0., 0.6, 0.4], [0.2, 0.4, 0.4]]))
    
    # generating random sequence
    sequence = chain.randomChain(3)
    print('Random Sequence -> ', sequence)

    # monte carlo simulation for calculating pi matrix
    chain.genMCS(82312)

    # Printing sequence's probability.
    if len(sequence) == 1:
        print('{:.2f}%'.format(chain.randomProbability(sequence) * 100),'probability for this state ->',defaultStates[sequence[0]])
    else:
        print('{:.2f}%'.format(chain.randomProbability(sequence) * 100),'probability for this state ##', defaultStates[sequence[0]],end=" ")
        for i in sequence[1:]:
            print("then ",defaultStates[i],end = " ")
        



