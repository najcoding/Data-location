import numpy as np
import matplotlib.pyplot as plt

def calculate_statistics(data):
    """
    Calculate Q1, Q3, IQR, and detect outliers using the IQR method.
    """
    # Ensure data is a NumPy array for easier calculations
    data = np.array(data, dtype=float)

    # Calculate quartiles
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    iqr = q3 - q1

    
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    
    outliers = data[(data < lower_bound) | (data > upper_bound)]

    return q1, q3, iqr, lower_bound, upper_bound, outliers

def visualize_boxplot(data):
    """
    Create a boxplot for the given dataset.
    """
    plt.figure(figsize=(6, 4))
    plt.boxplot(data, vert=True, patch_artist=True)
    plt.title("Boxplot of Data")
    plt.ylabel("Values")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

if __name__ == "__main__":
    try:
       
        raw_input = input("Enter numbers separated by spaces: ").strip()
        if not raw_input:
            raise ValueError("No data entered.")

        
        data = [float(x) for x in raw_input.split()]

       
        q1, q3, iqr, lower_bound, upper_bound, outliers = calculate_statistics(data)

        # Display results
        print(f"Q1 (25th percentile): {q1}")
        print(f"Q3 (75th percentile): {q3}")
        print(f"IQR: {iqr}")
        print(f"Lower bound for outliers: {lower_bound}")
        print(f"Upper bound for outliers: {upper_bound}")
        print(f"Outliers detected: {list(outliers) if outliers.size > 0 else 'None'}")

       
        visualize_boxplot(data)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
