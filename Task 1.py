# TODO решите задачу
import json
input_file = "input.json"
def task() -> float:
    total = 0.0
    with open(input_file, "r") as file:
        data = json.load(file)
        for item in data:
            total += item["score"] * item["weight"]
    return round(total, 3)
print(task())
