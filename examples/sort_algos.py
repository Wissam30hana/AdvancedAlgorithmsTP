def lcs_recursive(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    if X[m - 1] == Y[n - 1]:
        return 1 + lcs_recursive(X, Y, m - 1, n - 1)
    else:
        return max(lcs_recursive(X, Y, m - 1, n), lcs_recursive(X, Y, m, n - 1))
    
    def lcs_memoization(X, Y, m, n, memo):
    if m == 0 or n == 0:
        return 0
    if (m, n) in memo:
        return memo[(m, n)]
    if X[m - 1] == Y[n - 1]:
        memo[(m, n)] = 1 + lcs_memoization(X, Y, m - 1, n - 1, memo)
    else:
        memo[(m, n)] = max(lcs_memoization(X, Y, m - 1, n, memo), lcs_memoization(X, Y, m, n - 1, memo))
    return memo[(m, n)]
def lcs_dynamic_programming(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Retrieving the LCS from the DP table
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(reversed(lcs))
import random

class StringGenerator:
    def __init__(self, alphabet=['A', 'B', 'C']):
        self.alphabet = alphabet

    def generate(self, size: int = 1) -> str:
        return ''.join(random.choice(self.alphabet) for _ in range(size))
    
    def generate_pair(self, size1: int, size2: int):
        return self.generate(size1), self.generate(size2)
    
    def generate_similar_pair(self, size1: int, size2: int):
        str1 = self.generate(size1)
        str2 = str1[:size2]  # Make the second string a prefix of the first
        return str1, str2
    
    def generate_different_pair(self, size1: int, size2: int):
        str1 = self.generate(size1)
        str2 = self.generate(size2)
        return str1, str2
X = "ABCBDAB"
Y = "BDCAB"

print(lcs_recursive(X, Y, len(X), len(Y)))  # يجب أن يعرض 4
memo = {}

print(lcs_memoization(X, Y, len(X), len(Y), memo))  # يجب أن يعرض 4

print(lcs_dynamic_programming(X, Y))  # يجب أن يعرض "BCAB" أو "BDAB"

gen = StringGenerator(['A', 'C', 'G', 'T'])
print(gen.generate(10))  # مثال: "ACGTACGTAC"

str1, str2 = gen.generate_pair(5, 8)
print(str1, str2)

str1, str2 = gen.generate_similar_pair(6, 6)
print(str1, str2)

str1, str2 = gen.generate_different_pair(6, 8)
print(str1, str2)
