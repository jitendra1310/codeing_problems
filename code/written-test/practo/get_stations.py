#!/usr/bin/python3.8

"""
As discussed, below is Question 1 for the coding round

Minimum Number of Platforms Required for a Railway/Bus Station
Given arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station so that no train waits.
We are given two arrays which represent arrival and departure times of trains that stop.

Examples:

Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00}
dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}
Output: 3
Explanation: There are at-most three trains at a time (time between 11:00 to 11:20)


Input: arr[] = {9:00, 9:40}
dep[] = {9:10, 12:00}
Output: 1
Explanation: Only one platform is needed.
"""

def getStation(arrival, departure):
    
    station = 0
    dep2 = []
    for i in range(0,len(arrival)):
        assigened = 0
        if(i==0):
            station = 1
            assigened = 1
            dep2.append(departure[i]) 
        else:
            
             for j in range(0,len(dep2)):
                 if dep2[j] < arrival[i]:
                     dep2[j] = departure[i]                     
                     assigened = 1
                     break                     
             if assigened ==0:
                station +=1
                dep2.append(departure[i])
    print(station)            

arr = [9.00, 9.40, 9.50, 11.00, 15.00, 18.00]
dep = [9.10, 12.00, 11.20, 11.30 , 19.00, 20.00]
arr1 = [9.00, 9.40]
dep1 = [9.10, 12.00]
getStation(arr,dep)   


