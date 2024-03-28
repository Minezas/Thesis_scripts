import os

def process_file(file_path):
    # Open the file and read all lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Initialize lists to store different types of latencies
    total_latencies = []
    delayed_reward_latencies = []
    immediate_reward_latencies = []
    rewarded_latencies = []
    no_reward_latencies = []
    latencies = []

    # Iterate through each line in the file
    for line in lines:
        # Check if the line contains information about latency
        if "Latency" in line:
            # Extract the latency value from the line
            latency_str = line.split("Latency (sec):")[1].strip().replace(',', '.')

            # Convert the latency value to float and handle any errors
            try:
                latency = float(latency_str)
            except ValueError:
                print(f"Invalid latency value: {latency_str}. Skipping this line.")
                continue

            # Add the latency to the appropriate lists based on reward type
            total_latencies.append(latency)
            if "REWARD(3)" in line:
                delayed_reward_latencies.append(latency)
                rewarded_latencies.append(latency)
            elif "REWARD(1)" in line:
                immediate_reward_latencies.append(latency)
                rewarded_latencies.append(latency)
            elif "NO REWARD" in line:
                no_reward_latencies.append(latency)

            # Append the latency to the general latencies list
            latencies.append(latency)
        # Check for "Omission" trials and add a blank space in the latencies list
        elif "Omission|Start" in line:
            latencies.append("")

    # Calculate latency averages for different conditions
    latency_avg_all_trials = sum(total_latencies) / len(total_latencies) if total_latencies else 0
    latency_avg_delayed_reward = sum(delayed_reward_latencies) / len(delayed_reward_latencies) if delayed_reward_latencies else 0
    latency_avg_immediate_reward = sum(immediate_reward_latencies) / len(immediate_reward_latencies) if immediate_reward_latencies else 0
    latency_avg_rewarded = sum(rewarded_latencies) / len(rewarded_latencies) if rewarded_latencies else 0
    latency_avg_no_reward = sum(no_reward_latencies) / len(no_reward_latencies) if no_reward_latencies else 0

   
  return {
        "latency_avg_all_trials": latency_avg_all_trials,
        "latency_avg_delayed_reward": latency_avg_delayed_reward,
        "latency_avg_immediate_reward": latency_avg_immediate_reward,
        "latency_avg_rewarded": latency_avg_rewarded,
        "latency_avg_no_reward": latency_avg_no_reward,
        "latencies": latencies
    }

if __name__ == "__main__":
    # Input and output file paths
    input_file_path = "session.txt"  # Replace with the actual path to your input file
    output_file_path = "all_latencies.txt"  # Change the output file name if needed

    try:
      result = process_file(input_file_path)

        # Write all latencies to the output file
        with open(output_file_path, 'w') as output_file:
            for latency in result["latencies"]:
                if isinstance(latency, float):
                    output_file.write(f"{latency:.4f}\n")
                else:
                    output_file.write("\n")

        # Print latency averages for different conditions
        print("Latency Average of All Trials:", result["latency_avg_all_trials"])
        print("Latency Average of Delayed Reward Trials (REWARD 3):", result["latency_avg_delayed_reward"])
        print("Latency Average of Immediate Reward Trials (REWARD 1):", result["latency_avg_immediate_reward"])
        print("Latency Average of Rewarded Trials (REWARD 1 + REWARD 3):", result["latency_avg_rewarded"])
        print("Latency Average of No Rewarded Trials:", result["latency_avg_no_reward"])

    except FileNotFoundError:
        print(f"File not found at {input_file_path}. Please ensure the file exists and the path is correct.")
