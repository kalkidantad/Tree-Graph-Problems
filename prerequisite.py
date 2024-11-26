from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 0:
            return True

        # Step 1: Build the graph and in-degree map
        graph = {i: [] for i in range(numCourses)}
        inDegree = {i: 0 for i in range(numCourses)}

        for prereq in prerequisites:
            next_course, prev_course = prereq
            graph[prev_course].append(next_course)
            inDegree[next_course] += 1

        # Step 2: Collect courses with no prerequisites
        noPrereqCourses = [i for i in range(numCourses) if inDegree[i] == 0]

        print("Initial graph:", graph)
        print("Initial in-degree map:", inDegree)
        print("Initial no prerequisite courses:", noPrereqCourses)

        # Step 3: Topological sorting
        i = 0
        while i < len(noPrereqCourses):
            course = noPrereqCourses[i]
            i += 1
            print(f"Processing course {course}")

            # Reduce in-degree for each dependent course
            for next_course in graph[course]:
                inDegree[next_course] -= 1
                print(f"Reduced in-degree of course {next_course} to {inDegree[next_course]}")
                if inDegree[next_course] == 0:
                    noPrereqCourses.append(next_course)
                    print(f"Added course {next_course} to no prerequisite list")

        print("Final no prerequisite courses:", noPrereqCourses)
        return len(noPrereqCourses) == numCourses


# Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Example 1: No cycles, all courses can be finished
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    print("Can finish:", solution.canFinish(numCourses1, prerequisites1))  # Output: True

    # Example 2: Contains a cycle, not all courses can be finished
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    print("Can finish:", solution.canFinish(numCourses2, prerequisites2))  # Output: False

    # Example 3: Multiple courses, no cycle
    numCourses3 = 4
    prerequisites3 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print("Can finish:", solution.canFinish(numCourses3, prerequisites3))  # Output: True

    # Example 4: Single course, no prerequisites
    numCourses4 = 1
    prerequisites4 = []
    print("Can finish:", solution.canFinish(numCourses4, prerequisites4))  # Output: True

    # Example 5: Empty input
    numCourses5 = 0
    prerequisites5 = []
    print("Can finish:", solution.canFinish(numCourses5, prerequisites5))  # Output: True
