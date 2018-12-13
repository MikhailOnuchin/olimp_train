class Solve:
    def __init__(self, n, max_weight):
        self.n = n
        self.max_weight = max_weight
        self.covered = [False] * self.n
    
    def fill_sums(self, idx=0, curr_sum=0):
        if idx == self.answer:
            if 1 <= curr_sum <= self.n:
                self.covered[curr_sum - 1] = True
            return
        
        self.fill_sums(idx + 1, curr_sum)
        self.fill_sums(idx + 1, curr_sum - self.weights[idx])
        self.fill_sums(idx + 1, curr_sum + self.weights[idx])
    
    
    def check(self):
        self.covered = [False] * self.n
        self.fill_sums()
        
        for i in range(len(self.covered) - 1):
            if not self.covered[i] and not self.covered[i + 1]:
                return False
        return True
        
    
    def brute_force(self, idx=0, last=1):
        if (idx == self.answer):
            return self.check()
        
        for self.weights[idx] in range(last, self.max_weight + 1):
            if self.brute_force(idx + 1, self.weights[idx]):
                return True
        return False
        
    def solve(self, min_answer=0):
        self.answer = min_answer
        self.weights = [0] * min_answer
        
        while not self.brute_force():
            self.answer += 1
            self.weights.append(0)
        
        return self.weights

import sys
import math

n = int(input())
print(*Solve(n, n).solve(math.ceil(math.log(n, 3))))
