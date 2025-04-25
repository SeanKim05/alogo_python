def permutation(nums):
    result = []
    curr = []
    visited = [False] * len(nums)

    def backtrack():
        if len(curr) == len(nums):
            result.append(curr[:])
            return

        for i in range(len(nums)):
            if visited[i]:
                continue

            visited[i] = True
            curr.append(nums[i])
            backtrack()
            curr.pop()
            visited[i] = False

    backtrack()
    return result

# [1] → [1,2] → [1,2,3] ✅
#            ↘︎ [1,3] → [1,3,2] ✅
# [2] → [2,1] → [2,1,3] ✅
#            ↘︎ [2,3] → [2,3,1] ✅
# [3] → [3,1] → [3,1,2] ✅
#            ↘︎ [3,2] → [3,2,1] ✅
