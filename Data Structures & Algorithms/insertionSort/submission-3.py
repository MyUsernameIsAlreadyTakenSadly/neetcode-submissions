# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        array=list(pairs)
        result=[]

        for i in range(len(array)):
            j=i

            while j>0 and array[j].key<array[j-1].key:
                array[j], array[j-1] = array[j-1], array[j]
                j-=1

            result.append(array.copy())
        return result
