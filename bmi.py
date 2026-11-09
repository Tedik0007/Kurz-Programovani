vaha = 0
vyska = 0

vyska = float(input("Zadejte svou výšku v metrech: "))
vaha = float(input("Zadejte svou váhu v kilogramech: "))

bmi = vaha / (vyska ** 2)

if bmi < 18.5:
    print(f"Vaše BMI je {bmi:.2f}. Máte podváhu.")
elif 18.5 <= bmi < 25:
    print(f"Vaše BMI je {bmi:.2f}. Máte normální váhu.")
elif 25 <= bmi < 30:
    print(f"Vaše BMI je {bmi:.2f}. Máte nadváhu.")
else:
    print(f"Vaše BMI je {bmi:.2f}. Máte obezitu.")