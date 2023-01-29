import random
import statistics
import matplotlib.pyplot as plt

def generate_number():
    digits = []
    for i in range(4):
        digit = random.randint(0, 9)
        digits.append(str(digit))
    return "".join(digits)

def one_sim_s1():
    key = 2022
    count = 0
    attempt = ""
    while(attempt != key):
        attempt = generate_number()
        count += 1
        if(attempt == key):
            print("success\n")
    return count

def sim(nsim):
    trials_record = []
    for i in range(nsim):
        trials = one_sim_s1()
        trials_record.append(trials)
        i +=1
    sd = statistics.stdev(trials_record)
    ave = statistics.mean(trials_record)
    return ave, sd

nsims = [i for i in range(100, 1001, 100)]
print(nsims)
ave_s1 = []
sd_s1 = []
for j in nsims:
    cave, csd = sim(j)
    ave_s1.append(cave)
    sd_s1.append(csd)

labels = [str(i) for i in nsims]












