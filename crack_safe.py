class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        visited = set()  # To keep track of the visited combinations
        s = '0' * (n - 1)  # Starting with the initial string of n-1 '0's
        res = s  # This will store the final result string
        
        # Start the backtracking process
        while True:
            for i in range(k - 1, -1, -1):  # Try digits from k-1 down to 0
                # Check if the combination (current string + digit) has been visited
                if (s, i) not in visited:
                    res += str(i)  # Append the new digit to the result
                    visited.add((s, i))  # Mark the current combination as visited
                    s = (s + str(i))[1:]  # Shift the string to get the next possible sequence
                    break
            else:
                # If no valid digit is found to extend the string, it means we have finished
                return res

# Test Example
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1: Simple Case with n=2 and k=2
    print(solution.crackSafe(2, 2))  # Expected Output: "00110" or any valid sequence
    
    # Test Case 2: Case with n=3 and k=2
    print(solution.crackSafe(3, 2))  # Expected Output: "00010111" or any valid sequence
    
    # Test Case 3: Larger Case with n=2 and k=3
    print(solution.crackSafe(2, 3))  # Expected Output: "00012" or any valid sequence
    
    # Test Case 4: Larger Case with n=4 and k=3
    print(solution.crackSafe(4, 3))  # Expected Output: A valid sequence that covers all 3-digit combinations
