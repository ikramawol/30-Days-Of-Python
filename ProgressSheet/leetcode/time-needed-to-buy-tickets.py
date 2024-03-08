class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue = deque()

        for i in range(len(tickets)):
            queue.append(i)
        
        count = 0
        while tickets[k] != 0:
            popped = queue.popleft()
            count += 1
            tickets[popped] -= 1

            if tickets[popped] > 0:
                queue.append(popped)

        return count
            

        # for i in range(len(tickets)):
        #     if queue[i] != 0:
        #         popped = queue.popleft()
        #         queue.append(popped - 1)
        #         count+=1
        #     else:
        #         queue.append(queue[i])
        #         if i==k:
        #             return count
        # return count



            