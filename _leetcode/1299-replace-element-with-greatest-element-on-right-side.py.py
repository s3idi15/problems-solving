class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        # initial max = -1
        # reverse iteration
        # new max = max(old max, arr[i])
        rightMax = -1

        for i in range(len(arr) - 1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr

if __name__ == "__main__":
    arr = [17, 18, 5, 4, 6, 1]
    rightMax = -1 #rightMax = 18
    for i in range(len(arr) - 1, -1, -1): # i = 1 arr[0] = 17
        newMax = max(rightMax, arr[i]) # newMax = (18, 17) ==> newMax = 18
        arr[i] = rightMax # arr[0] = 18
        rightMax = newMax # rightMax = 18
        print(f"{arr}")
        