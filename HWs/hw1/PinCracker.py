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
    key = '2022'
    count = 0
    attempt = ''
    while(attempt != key):
        attempt = generate_number()
        count += 1
    return count

def one_sim_s2():
    key = '2022'
    count = 0
    attempt = ''
    record = []
    while(attempt != key):
        attempt = generate_number()
        if(attempt in record):
            continue
        else:
            count +=1
            record.append(attempt)
    return count


def sim1(nsim):
    trials_record = []
    for i in range(nsim):
        trials = one_sim_s1()
        trials_record.append(trials)
        i +=1
    sd = statistics.stdev(trials_record)
    ave = statistics.mean(trials_record)
    print(sd, ave, '\n')
    return ave, sd

def sim2(nsim):
    trials_record = []
    for i in range(nsim):
        trials = one_sim_s2()
        trials_record.append(trials)
        i +=1
    sd = statistics.stdev(trials_record)
    ave = statistics.mean(trials_record)
    print(sd, ave, '\n')
    return ave, sd

nsims = [i for i in range(100, 1001, 100)]
print(nsims)
ave_s1 = []
sd_s1 = []
ave_s2 = []
sd_s2 = []

for j in nsims:
    cave1, csd1 = sim1(j)
    cave2, csd2 = sim2(j)
    ave_s1.append(cave1)
    sd_s1.append(csd1)
    ave_s2.append(cave2)
    sd_s2.append(csd2)


plt.errorbar(nsims, ave_s1, yerr=sd_s1, fmt='o', color='red', ecolor='black', capsize=5)
plt.xlabel('Number of Simulations')
plt.ylabel('Average Number of Trials')
plt.title('Plot s1 with Error Bars')
plt.savefig('s1plot.jpeg')
plt.show()












