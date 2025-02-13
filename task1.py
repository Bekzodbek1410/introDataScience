def kwargsAcceptFun(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

kwargsAcceptFun(name="Bekzod", age=19, country="Uzbekistan")
