class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        largest = arr[0]
        second_largest = -1
        
        for i in range(len(arr)):
            if arr[i] > largest:
                second_largest = largest
                largest = arr[i]
            elif arr[i] > second_largest and largest != arr[i]:
                second_largest = arr[i]
        return second_largest
