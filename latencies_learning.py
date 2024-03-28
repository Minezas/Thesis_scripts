import os

def calculate_average(filename):
    try:
        # Specify the full path to the file on your desktop
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        filename = os.path.join(desktop_path, f'{filename}.txt')  # Assume it's a text file, modify if necessary

        with open(filename, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()

            # Ensure that each line contains a valid latency value
            values = []
            for line in lines:
                try:
                    latency_value = float(line.strip())
                    values.append(latency_value)
                except ValueError:
                    print(f"Skipping line: {line.strip()} - Latency information not found or not valid.")

            # Check if there are valid values before calculating averages
            if not values:
                print("Error: No valid latency values found.")
                return

            # Calculate the average for all values
            total_values = len(values)
            average_all = sum(values) / total_values

            # Calculate average for values greater than 5 seconds
            values_gt_5 = [value for value in values if value > 5]
            total_values_gt_5 = len(values_gt_5)
            average_gt_5 = sum(values_gt_5) / total_values_gt_5 if total_values_gt_5 > 0 else 0

            # Calculate average for values less than 5 seconds
            values_lt_5 = [value for value in values if value < 5]
            total_values_lt_5 = len(values_lt_5)
            average_lt_5 = sum(values_lt_5) / total_values_lt_5 if total_values_lt_5 > 0 else 0

            # Print the averages
            print(f"The average of all latencies is: {average_all}")
            if total_values_gt_5 > 0:
                print(f"The average of latencies greater than 5 seconds is: {average_gt_5} (based on {total_values_gt_5} values)")
            else:
                print("No latencies greater than 5 seconds found.")
            if total_values_lt_5 > 0:
                print(f"The average of latencies less than 5 seconds is: {average_lt_5} (based on {total_values_lt_5} values)")
            else:
                print("No latencies less than 5 seconds found.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except ValueError:
        print("Error: The file contains non-numeric values.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with the correct filename
calculate_average('latency')
