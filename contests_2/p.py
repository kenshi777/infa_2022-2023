import random as rnd

rnd.seed(42)

c = 0
ls = []
while True:
    is_rain = rnd.randint(0, 10000) <= 3000

    is_A_say_true = rnd.randint(0, 10000) <= 7000
    is_B_say_true = rnd.randint(0, 10000) <= 6000

    fact_A_about_rain = 'y' if is_rain == is_A_say_true else 'n'
    fact_B_about_rain = 'y' if is_rain == is_B_say_true else 'n'
    
    if fact_A_about_rain == 'y' and fact_B_about_rain == 'y':
        ls.append(1 if is_rain else 0)
    
    c += 1
    if c > 42000:
        break

print(sum(ls)/len(ls))