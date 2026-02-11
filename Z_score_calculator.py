def calculate_z_scores(count):
    results = []
    for i in range(count):
        print(f"\n--- Entry {i+1} ---")
        measured = float(input("Input (x): "))
        mean = float(input("Mean (μ): "))
        dev = float(input("Std Dev (σ): "))
        z_score = (measured - mean) / dev
        results.append(z_score)
    
    return results


num = int(input("How many values to compare? "))
all_scores = calculate_z_scores(num)

print("\n--- Calculated Z-Scores ---")
for index, score in enumerate(all_scores):
    print(f"Item {index + 1}: {score:.4f}")