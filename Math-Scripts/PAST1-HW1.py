from random import random

def bernoulli(pr: float = 0.5) -> bool:
    return random() < pr

# ======= Coin toss simulation ========

class Coin:
    def __init__(self, prob_heads):
        self.prob_heads = prob_heads
    
    def Toss(self):
        return bernoulli(self.prob_heads)

def Round(coin):
    toss_count = 0

    # toss until heads fall
    while not coin.Toss():
        toss_count += 1
    toss_count += 1
    
    # toss to see if coins can be kept
    for _ in range(toss_count):
        if not coin.Toss():
            return False, 0

    return True, toss_count

def coin_game(rounds: int = 50000, prob_heads: float = 0.5):
    win_count = 0
    two_coin_wins = 0

    c = Coin(prob_heads)

    for _ in range(rounds):
        win, winnings = Round(c)
        if win:
            win_count += 1
            if winnings == 2:
                two_coin_wins += 1
    
    prob_two_coin_win = two_coin_wins / rounds
    prob_win = win_count / rounds

    print(f"P[win] = {prob_win}")
    print(f"P[two coin win] = {prob_two_coin_win}")


# ======== Disease simulation =========

class Human:
    # disease prevance should be the ratio of infected people and all people
    # aka the probability of a uniformly chosen person being infected
    def __init__(self, disease_prevalence):
        self.infected = bernoulli(disease_prevalence)

class Test:
    # specificity - the probability that the test is positive given the tested person is infected
    # sensitivity - the probability that the test is negative given the tested person is not infected
    def __init__(self, sensitivity: float, specificity: float):
        self.sensitivity = sensitivity
        self.specificity = specificity

    def TestPerson(self, human: Human) -> bool:
        if human.infected:
            return bernoulli(self.sensitivity)
        else:
            return not bernoulli(self.specificity)

# Drives the simulation, prints the probability of true positive, false poitive, positive test probability and disease probablility
def disease_test(subject_count: int = 50000, test_sensitivity: float = 0.99, test_specificity: float = 0.98, disease_prevalence: float = 0.001):
    false_positive = 0
    true_positive = 0
    infected = 0

    t = Test(test_sensitivity, test_specificity)

    for _ in range(subject_count):
        h = Human(disease_prevalence)
        if h.infected:
            infected += 1
            if t.TestPerson(h):
                true_positive += 1
        elif t.TestPerson(h):
            false_positive += 1
    
    prob_positive_test = (false_positive + true_positive) / subject_count
    prob_false_positive = false_positive / (subject_count - infected)
    prob_true_positive = true_positive / infected
    prevalence_estimate = (prob_positive_test - prob_false_positive) / (prob_true_positive - prob_false_positive)

    # print(f"P[positive test] = {prob_positive_test}")
    # print(f"P[false positive] = {prob_false_positive} (Actual value: {1 - test_specificity})")
    # print(f"P[true positive] = {prob_true_positive} (Actual value: {test_sensitivity})")
    # print(f"P[disease] = {prevalence_estimate} (Actual value: {disease_prevalence})")

    prob_infected_given_positive = (prob_true_positive * prevalence_estimate) / (prob_true_positive * prevalence_estimate + prob_false_positive * (1 - prevalence_estimate))
    print(f"P[infected given pos. test] = {prob_infected_given_positive}")

    prob_infected_given_two_tests = ((prob_true_positive**2) * prevalence_estimate) / (((prob_true_positive**2) * prevalence_estimate) + ((prob_false_positive**2) * (1 - prevalence_estimate)))
    print(f"P[infected given two pos. tests] = {prob_infected_given_two_tests}")

# ============ Driver code ============

def main():
    print("===== Coin game simulation =====")
    coin_game()
    print("====== Disease simulation ======")
    disease_test()

if __name__ == "__main__":
    main()