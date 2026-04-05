from lab1 import monotony_check

def classify_temperature(temps):

    if monotony_check(temps) == False:
        return "non-monotonic"
        
    if temps[0] == temps[-1]:
        return "constant"
    elif temps[0] < temps[-1]:
        return "increasing"
    else:
        return "decreasing"

if __name__ == "__main__":
    print("Зростання:", classify_temperature([20.0, 21.5, 22.0, 24.1]))
    print("Спадання:", classify_temperature([100.5, 98.0, 95.2, 90.0]))
    print("Стабільна:", classify_temperature([50.0, 50.0, 50.0, 50.0]))
    print("Стрибки:", classify_temperature([45.0, 48.0, 46.5, 50.0]))