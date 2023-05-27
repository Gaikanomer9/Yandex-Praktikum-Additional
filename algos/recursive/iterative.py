import copy

class Solution:
    @staticmethod
    def print(arr):
        for a in arr:
            print(a, end=' ')
        print()

    def reconstructQueue(self, people):
        res = [[0, 0] for _ in people]
        copy_people = copy.deepcopy(people)
        self.print(res)
        self.print(copy_people)

        for j in range(len(res)):
            # find min
            minz = float('inf')
            mind = -1
            for i in range(len(people)):
                if copy_people[i][1] == 0:
                    if minz > copy_people[i][0]:
                        minz = copy_people[i][0]
                        mind = i

            res[j] = people[mind]

            # update values
            for i in range(len(copy_people)):
                if copy_people[i][0] <= minz:
                    copy_people[i][1] -= 1

        return res
    
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
sol = Solution()
print(sol.reconstructQueue(people))