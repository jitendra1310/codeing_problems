#!/usr/bin/python3.8

"""
In our packaging department, N workers pack M items that need to be delivered to our customers. Each worker
works at a different pace and takes different amount of time to pack an item. Given all workers work
simultaneously, you need to find minimum time required to pack all M items.
Input
First row has 2 integers N and M where N is the number of workers and M is the total number of items that need
to be packed.
Next row has N integers where each integer is the amount of time in seconds each worker takes to pack an item.
We can have upto 1000 workers working together (N <= 1000) to pack upto 10000 items (M <= 10000).
Some of the workers are new at the job and might take upto 300 seconds to pack an item.
Example
Input
4 17
7 11 13 9
Output
44
Explanation:
In 44 seconds:
Worker 1 packs 6 items
Worker 2 packs 4 items
Worker 3 packs 3 items
Worker 4 packs 4 items

"""

class solution:
    def __init__(self):
        self.total_workers = int(input("Please enter the workers:"))
        self.items = int(input("Please enter the items:"))
        self.workers= dict()
        self.consumeTime = 0
        self.totalConsumeTime = 0
        
        for i in range(0,self.total_workers):
            pace = int(input("Please enter worker pace:"))
            self.workers[i] = {"pace":pace}
        
        self.get_working_time()
        
        print(f"Total Time Consume:{self.consumeTime}")
        print(self.workers)    
        
    def get_working_time(self):
        assigned_item = 0        
        while(self.items>assigned_item):
            self.totalConsumeTime += 1
            for x in range(0,len(self.workers)):
                if(self.items-assigned_item):
                    if(self.totalConsumeTime==1):
                        self.workers[x]['iteams'] = 1
                        self.workers[x]['max_time'] = self.workers[x]['pace']                    
                        assigned_item += 1
                    elif((self.totalConsumeTime-1)%self.workers[x]['pace']==0):
                            self.workers[x]['iteams'] = self.workers[x]['iteams']+1
                            self.workers[x]['max_time'] += self.workers[x]['pace']
                            assigned_item += 1
                    
                    if(self.workers[x]['max_time']>=self.consumeTime):
                        self.consumeTime = self.workers[x]['max_time']        
                        
        
obj = solution()        
           