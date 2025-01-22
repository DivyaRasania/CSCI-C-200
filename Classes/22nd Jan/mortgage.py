P = 400000
r = 0.0692
n = 12
t = 30

PMT = (P * (r / n)) / (1 - (1 + (r / n)) ** (-n * t))
print(PMT)
