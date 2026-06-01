# neetcode 150 dsa tracker

a structured neetcode 150 tracking system organized by patterns for placement preparation.

## how to use

### 1. solve problems

go into the corresponding topic folder and solve the problem inside the `.py` file.

example:

```python id="6whwxt"
class Solution:
    def twoSum(self, nums, target):
        pass
```

### 2. mark a problem as done

add:

```python id="mjlwmn"
# status: done
```

inside the file after solving it.

example:

```python id="2ysnzs"
# status: done
# difficulty: Easy
# attempts: 1
# notes:
# link: https://leetcode.com/problems/two-sum/

class Solution:
    pass
```

### 3. update progress tracker

run:

```bash id="aydmqx"
python3 tracker.py
```

this automatically:

* updates progress
* checks completed problems
* updates `PROGRESS_TRACKER.md`
* calculates completion percentage

## my progress

* completed: 1/150
* percentage: 0.67%

## full progress tracker

[view progress tracker](PROGRESS_TRACKER.md)
