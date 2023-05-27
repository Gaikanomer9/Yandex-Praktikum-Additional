import copy

class Solution:
    @staticmethod
    def print(arr):
        for a in arr:
            print(a, end=' ')
        print()

    def find_min(self, copy_people, min_height=float('inf'), min_index=-1, i=0):
        if i == len(copy_people):
            return min_index, min_height
        if copy_people[i][1] == 0 and min_height > copy_people[i][0]:
            min_index = i
            min_height = copy_people[i][0]
        return self.find_min(copy_people, min_height, min_index, i+1)

    def update_values(self, copy_people, min_height, i=0):
        if i == len(copy_people):
            return
        if copy_people[i][0] <= min_height:
            copy_people[i][1] -= 1
        self.update_values(copy_people, min_height, i+1)

    def reconstructQueue(self, people, res=None, copy_people=None, j=0):
        if res is None:
            res = [[0, 0] for _ in people]
            copy_people = copy.deepcopy(people)
            self.print(res)
            self.print(copy_people)
        
        if j == len(res):
            return res

        min_index, min_height = self.find_min(copy_people)
        res[j] = people[min_index]
        self.update_values(copy_people, min_height)
        return self.reconstructQueue(people, res, copy_people, j+1)

people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
sol = Solution()
print(sol.reconstructQueue(people))