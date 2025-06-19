D = 154.0
u0 = 9.0
ct = 0.763
k = 0.02

beta = (1 + (1 - ct)**0.5) / (2 * (1 - ct)**0.5)

def sigma(x):
    return k * x + 0.25 * (beta**0.5) * D

def u(x):
    term = 1 - ct / 8 * (D / sigma(x))**2
    return u0 * term**0.5 if term > 0 else 0

x = 1
while True:
    wind_speed = u(x)
    if wind_speed >= 8.95:
        break
    x += 1

recovery_distance = x