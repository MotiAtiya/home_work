import temperature as t

cities = ["Eilat", "Haifa", "Jerusalem"]
temperatures = [35, 22, 9]

if __name__ == "__main__":
    for i in range(len(cities)):
        city = cities[i]
        celsius = temperatures[i]
        fahrenheit = t.c_to_f(temperatures[i])
        description = t.describe(temperatures[i])

        print(f"{city}: {celsius} C / {fahrenheit} F - {description}")
