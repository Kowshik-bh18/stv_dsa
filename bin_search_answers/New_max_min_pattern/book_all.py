'''
Problem Statement: Given an array ‘arr of integer numbers, ‘ar[i]’ represents the number of pages in the ‘i-th’ book. There are a ‘m’ number of students, and the task is to allocate all the books to the students.
Allocate books in such a way that:

Each student gets at least one book.
Each book should be allocated to only one student.
Book allocation should be in a contiguous manner.
You have to allocate the book to ‘m’ students such that the maximum number of pages assigned to a student is minimum. If the allocation of books is not possible. return -1
'''

'''
This problem is solved using Binary Search to efficiently find the best way to distribute books among students.
The main idea is to cut the search range in half each time by checking whether a certain number of pages per student is possible or not.
The possible range of answers lies between the largest book (since no student can receive less than the largest book) and the total number of pages (which means giving all books to one student).
First, if there are more students than books, it's impossible to assign at least one book to each student, so we return -1.
Next, we search between the minimum and maximum possible values:
The minimum possible is the largest single book (because every student must get at least one complete book).
The maximum possible is the sum of all pages (if one student reads all books).
We perform Binary Search:
We try a middle value of pages per student.
We check how many students would be required if no student gets more than that value.
If it takes more students than allowed, that value is too low, so we try a higher one.
If it fits within the allowed number of students, we store it and try a smaller one to find an even better option.
Eventually, we land on the smallest value that works this is our answer.
Note: After the binary search loop ends, the pointer will be on the smallest possible maximum number of pages per student. That's why it gives the correct result directly.

'''

'''
Brute Force Approach
Algorithm
If m > n: In this case, book allocation is not possible and so, we will return -1.
Next, we will find the maximum element and the summation of the given array.
We will use a loop(say pages) to check all possible pages from max(arr[]) to sum(arr[]).
Next, inside the loop, we will send each ‘pages’, to the function countStudents() function to get the number of students to whom we can allocate the books.
The first number of pages, ‘pages’, for which the number of students will be equal to ‘m’, will be our answer. So, we will return that particular ‘pages’.
Finally, if we are out of the loop, we will return max(arr[]) as there cannot exist any answer smaller than that.

'''

class Solution:
    def findPages(self, nums, m):
        def can_allocate(limit):
            students = 1
            pages = 0
            for book in nums:
                if pages + book > limit:
                    students += 1
                    pages = book
                else:
                    pages += book
            # Each student must get at least one book
            return students <= m

        left = max(nums)      # largest single book
        right = sum(nums)     # all books to one student
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if can_allocate(mid):
                ans = mid       # feasible, try smaller maximum
                right = mid - 1
            else:
                left = mid + 1  # not feasible, need bigger maximum

        return ans