import math
import numpy as np


Test_dictionary = {"five":"Summary Statistics",
                   "svar": "Sample Varriance",
                   "pvar":"Population Varriance",
                   "sdev":"Standard Deviation",
                   "r":"Range",
                   "serr":"Standard Error",
                   "q":"Q1, Q3, and Interqurtile range",
                   "z":"Z-Score"}

Stoping_triggers = ["stop", "terminate", "exit", "quit"]
Continue_triggers = ["y", "yes", "continue", "oui"]


no_z = Test_dictionary.copy()
no_z.pop("z")

all_lists = []

def mode(List):
    frequency = {}
    for item in List:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    max_count = max(frequency.values())
    if max_count == 1:
        return "None"
    modes = [key for key, value in frequency.items() if value == max_count]
    return sorted(modes)

def deviation(svar):
    return math.sqrt(svar)

def iqr(List):
    n = len(List)
    half = n // 2
    if n % 2 == 0:
        half1, half2 = List[:half], List[half:]
    else:
        half1, half2= List[:half], List[half+1:]
    Q1 = np.median(half1)
    Q3 = np.median(half2)
    return Q3 - Q1

def z_subsystem(results_list):
    measured = float(input("Input (x): "))
    mean = float(input("Mean (μ): "))
    dev = float(input("Std Dev (σ): "))
    z_score = (measured - mean) / dev
    results_list.append(z_score)

def calculate_z_scores(count):
    results = []
    for i in range(count):
        print(f"\n--- Entry {i+1} ---")
        try:
            z_subsystem(results)
        except ValueError:
            print("ERROR: Please enter numeric values only. Try Again:")
            z_subsystem(results)
        print("\n--- Calculated Z-Scores ---")
        for index, score in enumerate(results):
            print(f"Item {index + 1}: {score:.4f}")

def list_subsystem():
    num_lists = int(input("How many lists to compare? "))
    local_lists = []
    for i in range(num_lists):
        csv_data = input(f"Please input List {i+1} (comma separated): ")
        try:
            clean_data = [float(x.strip()) for x in csv_data.split(',')]
            clean_data.sort()
            local_lists.append(clean_data)
        except ValueError:
            print(f"Error reading List {i+1}. Ensure you only use numbers and commas.")
    return local_lists

def ck_subsystem(key, place_holder, i):
    current_input = place_holder
    while current_input not in Test_dictionary and current_input not in Stoping_triggers:
            current_input = input(f"!!!ERROR!!!\nNot a Valid Calculator. Calculator {i}: ").strip().lower()
    key.append(current_input)

def create_key():
    key =[]
    i = 1
    place_holder = input(f"What calculator would you like to use? Options:\n1) \"Five\" (5 summary statistics)\n2) \"SVar\" (Sample Varriance)\n3) \"SDev\" (Sandard Deviation)\n4) \"R\" (Range)\n5) \"SErr\" (Standard Error)\n6) \"Q\" (IQR, Q1, Q3)\n7) \"Z\" (Z-Score Calculator)\nCalculator 1: ").strip().lower()
    ck_subsystem(key, place_holder, i)
    i += 1
    while not any(trigger in key for trigger in Stoping_triggers):
        place_holder = input(f"Either type \"stop\" or name another calcluator:\nCalculator {i}: ").strip().lower()
        ck_subsystem(key, place_holder,i)
        i += 1
    return key

def evenlengthchecker(nestedlist):
    length = len(nestedlist[0])
    for element in nestedlist:
         if len(element) != length:
             return False
    return True

def main():
    while True:
        
        key = create_key()
        all_lists = list_subsystem()
        
        input_check = list(set(key).intersection(no_z))
        
        print(f"\nTests to run:")
        for test in key:
            if test in Test_dictionary:
                print(f"- {Test_dictionary[test]}")
                
        if all_lists:
            if evenlengthchecker(all_lists):    
                for i in range(len(all_lists)):
                    current_list = all_lists[i]
                    if not current_list:
                        print(f"\n___________-_-_- LIST {i+1} (Empty) -_-_-___________")
                    
                    list_mean = np.mean(current_list)
                    list_median = np.median(current_list)
                    list_mode = mode(current_list)
                    list_svarriance = np.var(current_list, ddof=1)
                    list_pvarriance = np.var(current_list, ddof=0)
                    list_deviation = deviation(list_svarriance)
                    list_range = current_list[-1] - current_list[0]
                    list_error = list_deviation / math.sqrt(len(current_list))
                    list_iqr = iqr(current_list)
                    list_q1 = np.percentile(current_list, 25)
                    list_q3 = np.percentile(current_list, 75)

                    print(f"\n___________-_-_- LIST {i+1} -_-_-___________")
                    if "five" in key:
                        print(f"Min: {min(current_list)}")
                        print(f"Max: {max(current_list)}")
                        print(f"Mean: {list_mean}")
                        print(f"Median: {list_median}")
                        print(f"Mode: {list_mode}")
                    if "svar" in key:
                        print(f"Sample Variance: {list_svarriance}")
                    if "pvar" in key:
                        print(f"Population Variance: {list_pvarriance}")
                    if "sdev" in key:
                        print(f"Standard Deviation: {list_deviation}")
                    if "r" in key:
                        print(f"Range: {list_range}")
                    if "serr" in key:
                        print(f"Standard Error: {list_error}")
                    if "q" in key:
                        print(f"IQR: {list_iqr}")
                        print(f"Q1: {list_q1}")
                        print(f"Q3: {list_q3}")
                        
                if "z" in key:
                    try:
                        num = int(input("\n-_-_- Z-Score Calculator -_-_-\nHow many values to compare: "))
                        calculate_z_scores(num)
                    except ValueError:
                        print("Invalid input for Z-Score count. Try again:")
                        calculate_z_scores(int(input("\n-_-_- Z-Score Calculator -_-_-\nHow many values to compare: ")))
            else:
                print("Error: Lists must be equal length. Restarting input...")
                all_lists = []
                list_subsystem()
    
        restart = input("\nWould you like to perform another calculation? (y/n): ").strip().lower()
        if restart not in Continue_triggers:
            print("Terrminating Program")
            return False
                
                
if __name__ == "__main__":
    main()
