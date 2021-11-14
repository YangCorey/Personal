
from typing import List
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #Create a hash with each task and number of occurrences
        #Also create a set with possible tasks
        
        #Create history list of size n and add the n previous tasks
        
        #If hist[ind%n] contained task that > 0 in hash, readd to set
        #If possible tasks is not empty
        #pop one task from set
            #Add this task to history list of ind % n
            
        #If possible task is empty:
            #Add "idle" to hist
            
        #["A","A","B"]
        #n = 2
        
        if n == 0:
            return len(tasks)
        
        #space O(n)
        tasks_left = {} 
        possible_tasks = []
        history = [None]*n 

        for task in tasks:
            if task in tasks_left:
                tasks_left[task] += 1
            else:
                tasks_left[task] = 1
                

        for task in tasks_left:
            
            heapq.heappush(possible_tasks, (-1*tasks_left[task], task) )

                

        ind = 0
        tot_task = len(tasks)
        while tot_task > 0: # 3
            replaced_task = history[ind%n]  #None None "A":-1
            if len(possible_tasks) > 0: #{"A": 0}
                ct, task = heapq.heappop(possible_tasks)
                history[ind%n] = (ct + 1, task) #[None, None]
                tot_task -= 1 # 2
            else:
                history[ind%n] = None
                
            if replaced_task is not None  and replaced_task[0] < 0:
                heapq.heappush(possible_tasks,replaced_task)
            ind += 1 # 1 2 3
        return ind

