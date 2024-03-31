import os

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    latencies = []

    for line in lines:
        if "Latency (sec):" in line:
            # Replace commas with dots for proper conversion to float
            latency_str = line.split("Latency (sec):")[1].strip().replace(',', '.')

            # Remove non-numeric characters, including the hyphen
            latency_str = ''.join(char for char in latency_str if char.isdigit() or char == '.')

            # Convert to float and round
            if latency_str:
                latency = round(float(latency_str), 4)
                latencies.append(latency)
            else:
                latencies.append("")
        elif "Omission|Start" in line:
            # If the line indicates an "Omission" trial, insert a blank space
            latencies.append("")

    return latencies


def calculate_average(filename):
    latencies = process_file(filename)

    # Lists to store latencies greater than and less than 5 seconds
    total_values = []
    values_gt_5 = []
    values_lt_5 = []

    # Iterate through extracted latencies
    for latency in latencies:
        if isinstance(latency, float):
            # Append to the total values list
            total_values.append(latency)

            # Categorize into values greater than and less than 5 seconds
            if latency > 5:
                values_gt_5.append(latency)
            elif latency < 5:
                values_lt_5.append(latency)

    # If no valid latency values found, return zero averages
    if not total_values:
        print("Error: No valid latency values found.")
        return {
            "latency_avg_all": 0,
            "latency_avg_gt_5": 0,
            "latency_avg_lt_5": 0
        }

    # Calculate average latency values for all, greater than 5, and less than 5 seconds
    average_all = sum(total_values) / len(total_values)
    average_gt_5 = sum(values_gt_5) / len(values_gt_5) if values_gt_5 else 0
    average_lt_5 = sum(values_lt_5) / len(values_lt_5) if values_lt_5 else 0

    # Return a dictionary containing the average latency values
    return {
        "latency_avg_all": average_all,
        "latency_avg_gt_5": average_gt_5,
        "latency_avg_lt_5": average_lt_5
    }


if __name__ == "__main__":
    # Input File
    file_path = "session.txt"

    try:
        # Calculate average latency values
        result = calculate_average(file_path)

        # Print the results
        print("Latency Average of All Trials:", result["latency_avg_all"])
        print("Latency Average of Trials with Latencies Greater than 5 Seconds:", result["latency_avg_gt_5"])
        print("Latency Average of Trials with Latencies Less than 5 Seconds:", result["latency_avg_lt_5"])

    except FileNotFoundError:
        # Handle file not found error
        print(f"File not found at {file_path}. Please ensure the file exists and the path is correct.")

