def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    variation = 0
    variations_list = []

    for line in lines:
        if "REWARD(3)" in line:
            variation += 1
        elif "REWARD(1)" in line:
            variation -= 1

        # For every trial, regardless of response, append the current variation
        variations_list.append(variation)

    return variations_list

if __name__ == "__main__":
    input_file_path = "latency.txt"  # Replace with the actual path to your input file
    output_file_path = "variation.txt"  # Change the output file name if needed

    variations_list = process_file(input_file_path)

    with open(output_file_path, 'w') as output_file:
        for variation in variations_list:
            output_file.write(str(variation) + '\n')

    print("Variations:", variations_list)
