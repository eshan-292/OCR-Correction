from sre_parse import State


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
        cost_new= 0
        min_state = start_state
        new_state = start_state

        # You should keep updating self.best_state with best string so far.
        self.best_state = start_state





        ## Hill Climbing

        # index_list = list(range(0,len(self.best_state)))        # List of indices of characters which have not been changed till now

        
        # while(len(index_list)!=0):
        #     for i in index_list:
        #     #for i in range(len(self.best_state)):
        #         ch_conf = self.best_state[i]
        #         if(ch_conf == ' '): 
        #             continue
                
        #         for ch_actual in self.state_map[ch_conf]:
                    
        #             # Modify the string to replace the confused character with the possible actual character
        #             temp = list(self.best_state)
        #             temp[i] = ch_actual
        #             new_state = "".join(temp)

        #             # Calculate the cost of the new string
        #             cost_new = self.cost_fn(new_state)

        #             #Updating the min state and cost
        #             if(cost_new <= cost_min):
        #                 cost_min = cost_new
        #                 min_state = new_state
            
        #     # To prevent self loops in case they occur. They can occur if the cost function is not monotonic , or in other words if it not one one function
        #      # If there is no child state with a better cost, then we have reached a local minima so break out of the loop and return the best state            
        #     if(self.best_state == min_state) : 
        #         break 
        #     else : 
        #         # Updating the best state
        #         index_list.remove(i)
        #         self.best_state = min_state   
          




        # # Modified Hill Climbing
        # # In case we have a state which has the same cost as the min cost, we move to a random state 

        # index_list = list(range(0,len(self.best_state)))        # List of indices of characters which have not been changed till now



        # def hill_climbing_helper(curr_state,index_list):
        #     if len(index_list)==0:
        #         return curr_state

        #     for i in index_list:
        #     #for i in range(len(self.best_state)):
        #         ch_conf = curr_state[i]
        #         if(ch_conf == ' '): 
        #             continue
                
        #         for ch_actual in self.state_map[ch_conf]:
                    
        #             # Modify the string to replace the confused character with the possible actual character
        #             temp = list(curr_state)
        #             temp[i] = ch_actual
        #             nonlocal new_state
        #             nonlocal min_state
        #             nonlocal cost_new
        #             nonlocal cost_min

        #             new_state = "".join(temp)

        #             # Calculate the cost of the new string
        #             cost_new = self.cost_fn(new_state)

        #             #Updating the min state and cost
        #             if(cost_new <= cost_min):
        #                 cost_min = cost_new
        #                 min_state = new_state
            
        #     # If there is no child state with a better cost, then we have reached a local minima so break out of the loop and return the best state            
        #     if(curr_state == min_state) : 
        #         index_list.remove(i)
        #         temp_state = hill_climbing_helper(new_state,index_list)
        #         if(self.cost_fn(curr_state)< self.cost_fn(temp_state)):
        #             return curr_state
        #         else:
        #             return temp_state
        #     else : 
        #         # Updating the best state
        #         index_list.remove(i)
        #         return hill_climbing_helper(min_state,index_list)
          
        # self.best_state = hill_climbing_helper(start_state,index_list)




        # # Stochastic Hill Climbing
        # Instead of choosing the best state, choose the first state with cost less than current cost



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



        # Local Beam Search
        # Instead of selecting one min state as in hill climbing, select k min states and then choose the best state from them

        index_list = list(range(0,len(self.best_state)))        # List of indices of characters which have not been changed till now



        def local_beam_helper(curr_state,index_list):
            if len(index_list)==0:
                return curr_state

            for i in index_list:
            #for i in range(len(self.best_state)):
                ch_conf = curr_state[i]
                if(ch_conf == ' '): 
                    continue
                
                for ch_actual in self.state_map[ch_conf]:
                    
                    # Modify the string to replace the confused character with the possible actual character
                    temp = list(curr_state)
                    temp[i] = ch_actual
                    nonlocal new_state
                    nonlocal min_state
                    nonlocal cost_new
                    nonlocal cost_min

                    new_state = "".join(temp)

                    # Calculate the cost of the new string
                    cost_new = self.cost_fn(new_state)

                    #Updating the min state and cost
                    if(cost_new <= cost_min):
                        cost_min = cost_new
                        min_state = new_state
            
            # If there is no child state with a better cost, then we have reached a local minima so break out of the loop and return the best state            
            if(curr_state == min_state) : 
                index_list.remove(i)
                temp_state = local_beam_helper(new_state,index_list)
                if(self.cost_fn(curr_state)< self.cost_fn(temp_state)):
                    return curr_state
                else:
                    return temp_state
            else : 
                # Updating the best state
                index_list.remove(i)
                return local_beam_helper(min_state,index_list)
          
        self.best_state = local_beam_helper(start_state,index_list)


















        print('start state = \t', start_state)
        print('final state = \t', self.best_state)

        # raise Exception("Not Implemented.")


