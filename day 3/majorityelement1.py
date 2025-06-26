class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0
        for x in nums:
            if count == 0:
                candidate = x
            count += (1 if candidate == x else -1)
        return candidate
    
'''
**Revision Notes: Majority Element (LeetCode 169)**


---


**Problem:**

Find the element that appears more than ⌊n/2⌋ times in an array.


---


**Algorithm:**

**Boyer-Moore Voting Algorithm**


---


**Steps:**


1. Initialize `count = 0`, `candidate = None`.

2. For each `num` in `nums`:


  * If `count == 0`: set `candidate = num`

  * If `num == candidate`: `count += 1`

  * Else: `count -= 1`

3. Return `candidate`


---


**Key Idea:**

Each non-candidate cancels out one occurrence of the current candidate. Majority element survives because it exceeds all others combined.


---


**Time & Space:**


* Time: O(n)

* Space: O(1)


---


**Python Code:**


```python

def majorityElement(nums):

  count, candidate = 0, None

  for num in nums:

    if count == 0:

      candidate = num

    count += 1 if num == candidate else -1

  return candidate

```


**Java Code:**


```java

public int majorityElement(int[] nums) {

  int count = 0, candidate = 0;

  for (int num : nums) {

    if (count == 0)

      candidate = num;

    count += (num == candidate) ? 1 : -1;

  }

  return candidate;

}

```


---


**Caveat:**

Final `count` is not the actual frequency. It only reflects net balance during voting. To confirm frequency (if needed), do a second pass.

'''