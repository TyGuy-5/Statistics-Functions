import math
import numpy as np
    
def mean(List):
    summ = 0
    for element in List:
        summ += element
    return summ / len(List)

def median(List):
    parity = len(List) % 2
    if parity == 0:
        half = len(List) // 2
        cente1 = List[half - 1]
        cente2 = List[half]
        return mean([cente1, cente2])
    else:
        half = len(List) // 2
        return List[half]

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

def variance(List, mean_val):
    summ = 0
    for num in List:
        product = num - mean_val
        sqr = product ** 2
        summ += sqr
    devisor = len(List) - 1
    return summ / devisor

def deviation(var):
    return math.sqrt(var)

def iqr(List, cente):
    Q2 = cente
    parity = len(List) % 2
    half = len(List) // 2
    if parity == 0:
        half1 = List[:half]
        half2 = List[half:]
    else:
        half1 = List[:half-1]
        half2 = List[half:]
    Q1 = median(half1)
    Q3 = median(half2)
    return Q3 - Q1
def main():
    try:
        num_lists = int(input("How many lists to compare? "))
    except ValueError:
        print("Please enter a valid number.")
        exit()
    all_lists = []
    for i in range(num_lists):
        csv_data = input(f"Please input List {i+1}: ")
        try:
            # Changed int to float here
            clean_data = [float(x.strip()) for x in csv_data.split(',')]
            clean_data.sort()
            all_lists.append(clean_data)
        except ValueError:
            print(f"Error reading List {i+1}. Ensure you only use numbers and commas.")
            all_lists.append([])
            
    for i in range(len(all_lists)):
        current_list = all_lists[i]
        
        if not current_list:
            print(f"\n___________-_-_- LIST {i+1} (Empty) -_-_-___________")
            continue

        A = mean(current_list)
        B = median(current_list)
        C = mode(current_list)
        D = variance(current_list, A)
        E = deviation(D)
        F = current_list[-1] - current_list[0]
        G = E / math.sqrt(len(current_list))
        H = iqr(current_list, B)
        I = np.percentile(current_list, 25)
        J = np.percentile(current_list, 75)

        print(f"\n___________-_-_- LIST {i+1} -_-_-___________")
        print(f"Min: {min(current_list)}")
        print(f"Max: {max(current_list)}")
        print(f"Mean: {A}")
        print(f"Median: {B}")
        print(f"Mode: {C}")
        print(f"Sample Variance: {D}")
        print(f"Standard Deviation: {E}")
        print(f"Range: {F}")
        print(f"Standard Error: {G}")
        print(f"IQR: {H}")
        print(f"Q1: {I}")
        print(f"Q3: {J}")
        


main()


















# # --- 2.DEFINE HOW MANY LISTS TO COMPUTE ---
# num = int(input(f"How many list to compare"))
# 
# # --- 3. GET INPUT(S) ---
# def get_list(num):
#     for a in range(1, num + 1):
#         csv_data = input(f"Please input list: ")
#         data = [int(x.strip()) for x in csv_data.split(',')]
#         l{a}st = sorted(data)
#         return l{a}st
# 
# # --- 4. CALCULATE ---
# def calculate():
#     for a in range(1, num + 1):       
#         A{a} = mean(l{a}st)
#         B{a} = median(l{a}st)
#         C{a} = mode(l{a}st)
#         D{a} = variance(l{a}st, A)  
#         E{a} = deviation(D)       
#         F{a} = l{a}st[-1] - l{a}st[0]          
#         G{a} = E / math.sqrt(len(l{a}st))    
# 
# # --- 5. OUTPUT ---
# def OUTPUT():
#     for a in range(1, num + 1):
#         print(f"___________-_-_- LIST {a} -_-_-___________")
#         print(f"Mean: {A{a}}")
#         print(f"Median: {B{a}}")
#         print(f"Mode: {C{a}}")
#         print(f"Sample Variance: {D{a}}")
#         print(f"Standard Deviation: {E{a}}")
#         print(f"Range: {F{a}}")
#         print(f"Standard Error: {G{a}}")
#         
