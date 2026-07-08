# Statistics-Functions
Command-line interface application for calculating statistical metrics across multiple datasets. Built with Python and `numpy`, this tool allows users to input multiple data lists and select from a variety of standard statistical operations, returning formatted results in real-time.

---
## Dependencies

This script relies on standard Python libraries and NumPy. Ensure you have the following installed in your environment:

* Python 3.x
* `numpy`

To install NumPy, you can use pip:
```bash
pip install numpy

```

---

## Usage

Run the script directly from your terminal:

```bash
python your_script_name.py

```

### 1. Select Your Calculators

Upon execution, the prompt will ask you which calculators you want to use. You can input multiple calculators one by one. Once you are satisfied with your selections, type **`stop`**, **`terminate`**, **`exit`**, or **`quit`** to proceed to data entry.

### 2. Input Your Data

* Specify how many lists of data you want to compare.
* Input the data for each list as comma-separated values (e.g., `12, 15, 18.5, 22`).
* **Note:** All lists entered must be of the exact same length. If they are not, the script will trigger an error and prompt you to re-enter your data.

### 3. Review Results

The program will output the requested statistics sequentially for each list provided. If you selected the Z-Score calculator, it will launch a dedicated subsystem to gather the specific variables (Input, Mean, Standard Deviation) needed for that calculation.

---

## Available Calculators

Use the exact "Input Command" below when prompted by the application to queue up a specific statistical calculation.

| Input Command | Description | Outputs Generated |
| --- | --- | --- |
| `five` | 5 Summary Statistics | Minimum, Maximum, Mean, Median, Mode |
| `svar` | Sample Variance | Variance (Degrees of Freedom = 1) |
| `pvar` | Population Variance | Variance (Degrees of Freedom = 0) |
| `sdev` | Standard Deviation | Standard Deviation (derived from Sample Variance) |
| `r` | Range | Difference between the Maximum and Minimum values |
| `serr` | Standard Error | Standard Error of the Mean |
| `q` | Quartiles & IQR | Interquartile Range, Q1 (25th percentile), Q3 (75th percentile) |
| `z` | Z-Score Calculator | Dedicated prompt for x, μ, and σ to return a Z-score |

---

## Notes

* **List Length Constraints:** The `evenlengthchecker` function strictly enforces that all compared lists contain the same number of elements.
* **Empty Lists:** While the code flags empty datasets during the execution loop, inputting empty strings may cause unforeseen `ValueError` exceptions during the float-conversion phase. Please ensure your comma-separated inputs are populated.
* **Mode Calculation:** If all values in a dataset appear exactly once (maximum frequency = 1), the mode will explicitly return `"None"` rather than the entire dataset.

```

```
