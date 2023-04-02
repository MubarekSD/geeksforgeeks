class Solution:
    def select(self, arr, i):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        return min

    def selectionSort(self, arr, n):
        print(n)
        for i in range(n):
            min = self.select(arr, i)
            arr[i], arr[min] = arr[min], arr[i]
        return arr
