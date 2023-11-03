class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        pointer = 0
        re = []
        for i in range(1,n+1):
            if i==target[pointer]:
                re.append("Push")
                pointer +=1
                if pointer == len(target):
                    return re
            else:
                re.append("Push")
                re.append("Pop")
        return re
