# Baartyrbek Turatov 
# 5/21/2025

# Problem 4:  
# Search on the internet for a way to calculate an approximation for pi. 
# There are many that use simple arithmetic. 
# Write a program to compute the approximation and then print that value as well as the value of math.pi from the math module.


#We will use Leibniz formula: pi = 4 * (1 − 1/3 + 1/5 − 1/7 + 1/9 − 1/11 + …)


import math

# Number of terms to use for the approximation
nTerms = 100000
piApprox = 0

# Compute the approximation
for i in range(nTerms):
    denominator = 2 * i + 1
    if i % 2 == 0:
        piApprox += 4 / denominator
    else:
        piApprox -= 4 / denominator

# Print results
print(f"Approximated π using {nTerms} terms: {piApprox}")
print(f"Actual π from math module: {math.pi}")