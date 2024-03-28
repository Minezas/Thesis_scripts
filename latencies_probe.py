import os

def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    total_latencies = []
    delayed_reward_latencies = []
    immediate_reward_latencies = []
    rewarded_latencies = []
    no_reward_latencies = []

    for line in lines:
        if "Latency" in line:
            # Replace commas with dots in the latency string
            latency_str = line.split("Latency (sec):")[1].strip().replace(',', '.')

            # Check if the latency_str is a valid float
            try:
                latency = float(latency_str)
            except ValueError:
                print(f"Invalid latency value: {latency_str}. Skipping this line.")
                continue

            total_latencies.append(latency)

            if "REWARD(3)" in line:
                delayed_reward_latencies.append(latency)
                rewarded_latencies.append(latency)
            elif "REWARD(1)" in line:
                immediate_reward_latencies.append(latency)
                rewarded_latencies.append(latency)
            elif "NO REWARD" in line:
                no_reward_latencies.append(latency)

    latency_avg_all_trials = sum(total_latencies) / len(total_latencies)
    latency_avg_delayed_reward = sum(delayed_reward_latencies) / len(delayed_reward_latencies)
    latency_avg_immediate_reward = sum(immediate_reward_latencies) / len(immediate_reward_latencies)
    latency_avg_rewarded = sum(rewarded_latencies) / len(rewarded_latencies)
    latency_avg_no_reward = sum(no_reward_latencies) / len(no_reward_latencies)

    return {
        "latency_avg_all_trials": latency_avg_all_trials,
        "latency_avg_delayed_reward": latency_avg_delayed_reward,
        "latency_avg_immediate_reward": latency_avg_immediate_reward,
        "latency_avg_rewarded": latency_avg_rewarded,
        "latency_avg_no_reward": latency_avg_no_reward
    }

if __name__ == "__main__":
    file_path = r"C:\Users\gonca\PycharmProjects\test\latency.txt"

    try:
        result = process_file(file_path)

        print("Latency Average of All Trials:", result["latency_avg_all_trials"])
        print("Latency Average of Delayed Reward Trials (REWARD 3):", result["latency_avg_delayed_reward"])
        print("Latency Average of Immediate Reward Trials (REWARD 1):", result["latency_avg_immediate_reward"])
        print("Latency Average of Rewarded Trials (REWARD 1 + REWARD 3):", result["latency_avg_rewarded"])
        print("Latency Average of No Rewarded Trials:", result["latency_avg_no_reward"])

    except FileNotFoundError:
        print(f"File not found at {file_path}. Please ensure the file exists and the path is correct.")
