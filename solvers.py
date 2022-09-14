class SentenceCorrector(object):
    def __init__(self, cost_fn, conf_matrix):
        self.conf_matrix = conf_matrix
        self.cost_fn = cost_fn

        # Inverting confusion matrix to create a state map
        state_map = {}     

        for i in range(26):
            state_map[chr(ord('a')+i)] = []

        for ch_actual in self.conf_matrix.keys():
            for ch_conf in self.conf_matrix[ch_actual]:
                state_map[ch_conf].append(ch_actual)

        self.state_map = state_map

        # You should keep updating following variable with best string so far.
        self.best_state = None  

    def search(self, start_state):
        """
        :param start_state: str Input string with spelling errors
        """

        # print(self.state_map)

        cost_min = self.cost_fn(start_state)
        min_state = start_state

        # You should keep updating self.best_state with best string so far.
        self.best_state = start_state

        # Hill Climbing
        while(True):
            for i in range(len(self.best_state)):
                ch_conf = self.best_state[i]
                if(ch_conf == ' '): 
                    continue
                
                for ch_actual in self.state_map[ch_conf]:
                    temp = list(self.best_state)
                    temp[i] = ch_actual
                    new_state = "".join(temp)
                    cost_new = self.cost_fn(new_state)

                    if(cost_new <= cost_min):
                        cost_min = cost_new
                        min_state = new_state

            if(self.best_state == min_state) : 
                break 
            else : 
                self.best_state = min_state   
          

        # # Stochastic Hill Climbing
        
        # next_state = start_state
        # cost_curr = self.cost_fn(start_state)
        # while(True):
        #     for i in range(len(self.best_state)):
        #         ch_conf = self.best_state[i]
        #         if(ch_conf == ' '): 
        #             continue
                
        #         for ch_actual in self.state_map[ch_conf]:
        #             temp = list(self.best_state)
        #             temp[i] = ch_actual
        #             new_state = "".join(temp)
        #             cost_new = self.cost_fn(new_state)

        #             if(cost_new <= cost_curr):
        #                 next_state = new_state

        #     if(self.best_state == next_state) : 
        #         break 
        #     else : 
        #         self.best_state = next_state   
        #         cost_curr = self.cost_fn(self.best_state)                
                             
        print('start state = \t', start_state)
        print('final state = \t', self.best_state)

        # raise Exception("Not Implemented.")
