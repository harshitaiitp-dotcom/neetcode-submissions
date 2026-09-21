class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        idle_time = 0
        total_waiting_time = 0
        for arrival, time in customers:
            start_time = max(idle_time, arrival)
            completion_time = start_time + time
            total_waiting_time += (completion_time - arrival)
            idle_time = completion_time            
        return total_waiting_time / len(customers)