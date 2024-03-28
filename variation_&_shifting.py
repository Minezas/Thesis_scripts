def process_file(file_path):
    # Open the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    lever_order = []  # Initialize list to store order of levers
    shifts = 0  # Initialize counter for shifts between levers
    prev_lever = None  # Initialize variable to store previous lever
    variation = 0  # Initialize counter for variations
    variations_list = []  # Initialize list to store variations

    # Loop through each line in the file
    for line in lines:
        # Check if the line contains a response to a lever
        if "Response: Lever" in line:
            # Extract the lever pressed from the line
            lever = line.split("Response: Lever ")[1][0]

            # Determine the lever pressed and append to lever_order
            if lever == "A":
                lever_order.append(1)  # Lever associated with REWARD(1)
            elif lever == "B":
                lever_order.append(2)  # Lever associated with REWARD(3)

            # Check for shifts between levers
            if prev_lever is not None and lever != prev_lever:
                shifts += 1

            # Update the previous lever
            prev_lever = lever

        # Check if the line indicates an omission trial
        elif "Omission" in line:
            lever_order.append(0)  # Omission trial, no lever pressed

        # Track variations
        if "REWARD(3)" in line:
            variation += 1
        elif "REWARD(1)" in line:
            variation -= 1

        # Append the current variation to the variations list
        variations_list.append(variation)

    # Return the lever order, shifts, and variations list
    return lever_order, shifts, variations_list

if __name__ == "__main__":
    # Input and output file paths
    input_file_path = "session.txt"  # Replace with the actual path to your input file
    output_lever_path = "order_of_levers.txt"  # Change the output file name if desired
    output_variation_path = "variation.txt"  # Change the output file name if desired

    # Process the input file
    lever_order, shifts, variations_list = process_file(input_file_path)

    # Write lever order to output file
    with open(output_lever_path, 'w') as output_lever_file:
        for lever in lever_order:
            output_lever_file.write(str(lever) + '\n')

    # Write variations list to output file
    with open(output_variation_path, 'w') as output_variation_file:
        for variation in variations_list:
            output_variation_file.write(str(variation) + '\n')

    # Print shifts between levers and variations
    print("Shifts between levers:", shifts)
    print("Variations:", variations_list)

