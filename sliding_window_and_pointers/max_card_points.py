'''
1423. Maximum Points You Can Obtain from Cards

There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.

'''

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = sum(cardPoints[:k])
        maxi = left_sum
        n = len(cardPoints)-1
        for i in range(k-1,-1,-1):
            left_sum-=cardPoints[i]
            left_sum+=cardPoints[n]
            n-=1
            if left_sum>maxi:
                maxi = left_sum
        return maxi
        


# or (another solution with easy understanding using another seperate right_sum varaiable)


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        leftsum = sum(cardPoints[:k])
        maxi = leftsum
        rightsum = 0
        rp = n-1
        for i in range(k-1,-1,-1):
            leftsum -=cardPoints[i]
            rightsum +=cardPoints[rp]
            rp-=1
            new_sum = leftsum+rightsum
            maxi = max(maxi,new_sum)
        return maxi


#logical intuition
'''
Instead of trying all combinations by recalculating front and back sums each time, we use a modified sliding window technique. We start by taking all k cards from the front, then gradually shift the window by removing one card from the front and adding one from the back. This keeps the number of selected cards fixed, but changes the selection balance between front and back. At each step, we update the score in constant time, which makes the solution much faster than brute force.
Calculate the sum of the first few elements from the start of the array, equal to the total number of cards to be selected.
Store this sum as the initial maximum possible score.
Iterate from the end of this initial window, gradually removing one element from the end of the current front window and adding one new element from the back of the array.
This maintains the total number of selected cards but shifts the balance between front and back.
After each shift, compare the new total score with the previously stored maximum and update the maximum if the new score is higher.
Repeat this process for as many shifts as there are cards to be picked.
Return the highest score obtained after evaluating all possible combinations of selections from the front and back.


'''