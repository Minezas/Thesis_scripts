def read_coordinates_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        inner_coordinates = []
        for line in lines:
            # Remove parentheses and split the line into x and y values
            values = line.replace('(', '').replace(')', '').replace('_', ',').split(',')

            # Handle different coordinate formats
            if len(values) == 4:
                # (x, xdecimal_part, y, ydecimal_part) format
                x = int(values[0])
                decimal_x = int(values[1])
                y = int(values[2])
                decimal_y = int(values[3])
                inner_coordinates.append((x, decimal_x, y, decimal_y))
            elif len(values) == 3:
                # Check if the second value exceeds the range for X
                if int(values[1]) > 500:
                    # (x, xdecimal_part, y) format
                    x = int(values[0])
                    decimal_x = int(values[1])
                    y = int(values[2])
                    inner_coordinates.append((x, decimal_x, y, 0))
                else:
                    # (x, y, ydecimal_part) format
                    x = int(values[0])
                    y = int(values[1])
                    decimal_y = int(values[2])
                    inner_coordinates.append((x, 0, y, decimal_y))
    return inner_coordinates


# Specify the full path to the 'data' file
file_path = 'data'

# Read the coordinates using the provided function
coordinates = read_coordinates_from_file(file_path)

# Create a new document with separate columns for x and y coordinates
with open('formatted_coordinates.txt', 'w') as new_file:
    
    for x, decimal_x, y, decimal_y in coordinates:
        new_file.write(f'{x}.{decimal_x:04d}              {y}.{decimal_y:04d}\n')
