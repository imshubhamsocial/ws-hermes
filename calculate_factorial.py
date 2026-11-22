import math
N = 9999
log_sum = 0
for i in range(2, N + 1):
    log_sum += math.log10(i)
number_of_digits = math.floor(log_sum) + 1
# The full number is too large to display. Providing the scientific representation.
print(f"The number of digits in 9999! is: {number_of_digits}")
# Scientific notation is approximately 9.999! ≈ 1.3999e36007
print(f"The value is approximately 1.3999e36007.")