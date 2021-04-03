import random

def dieToss(sideCount: int = 6):
    return random.randint(1, sideCount)

def expectedValueOfOneDie(rollCount: int) -> int:
    rollSum = 0
    for _ in range(rollCount):
        rollSum += dieToss()
    return rollSum/rollCount

def expectedValueOfSum(rollCount: int) -> int:
    rollSum = 0
    for _ in range(rollCount):
        rollSum += dieToss() + dieToss()
    return rollSum/rollCount

def expectedValueOfMin(rollCount: int) -> int:
    rollSum = 0
    for _ in range(rollCount):
        rollSum += min(dieToss(), dieToss())
    return rollSum/rollCount

def diceSimulation(rollCount: int = 50000):
    print("Expected value of one die: ", expectedValueOfOneDie(rollCount))
    print("Expected value of the sum of two tosses: ", expectedValueOfSum(rollCount))
    print("Expected value of the minimum of two tosses: ", expectedValueOfMin(rollCount))

# ======= ENTRY =======
def main():
    diceSimulation()

if __name__ == "__main__":
    main()