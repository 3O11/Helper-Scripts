import random
import math

# Expected value of the longer part of a 1m long stick that was cut into two pieces.
def CuttingStick(iterations: int = 1000000):
    totalLength = 0
    for _ in range(iterations):
        cutAt = random.uniform(0, 1)
        totalLength += max(cutAt, 1 - cutAt)
    
    expectedValue = totalLength / iterations
    print("Expected value of longer piece: " + str(expectedValue))

# This was taken directly from the assignment
def rand_point():
    # vraci nahodny bod [-1, 1) X [-1, 1)
    return (2 * random.random() - 1, 2 * random.random() - 1)

def p():
    # vraci nahodny bod v terci
    x, y = rand_point()
    while x**2 + y**2 > 1:
        x, y = rand_point()
    return (x, y)

# Dart throwing simulation
def DartThrowing(iterations: int = 1000000):
    totalDistanceFromCenter = 0
    for _ in range(iterations):
        x, y = p()
        totalDistanceFromCenter += math.sqrt(x**2 + y**2)
    
    expectedValue = totalDistanceFromCenter / iterations
    print("Expected distance from target center: " + str(expectedValue))

def DartCDF(values: list = [0, 0.25, 0.5, 0.75, 0.99, 1], iterations: int = 1000000):
    for value in values:
        smallerThanValCount = 0
        for _ in range(iterations):
            x, y = p()
            currentDistFromCenter = math.sqrt(x**2 + y**2)
            if currentDistFromCenter <= value:
                smallerThanValCount += 1
        
        cdfApprox =smallerThanValCount / iterations
        print(f"The approximation of CDF value for {value} is {cdfApprox}.")

def main():
    # Calculation of expected values
    CuttingStick()
    DartThrowing()

    # CDF Approximation for a few discrete values
    DartCDF()

if(__name__ == "__main__"):
    main()