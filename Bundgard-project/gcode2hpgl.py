import re

# Define your scaling factors based on your calculations
scale_x = 10.0 # 1000.0
scale_y = 10.0 # 1000.0

def parse_gcode(gcode_file, hpgl_file):
    z_is_negative = False  # Track Z state (cutting or not)
    
    with open(gcode_file, 'r') as gcode, open(hpgl_file, 'w') as hpgl:
        for line in gcode:
            line = line.strip()

            # Ignore comments
            if line.startswith('(') and line.endswith(')'):
                continue

            # Handle Z-axis movements
            z_match = re.search(r'Z([-+]?\d*\.\d+|\d+)', line)
            if z_match:
                z_value = float(z_match.group(1))
                
                if z_value < 0 and not z_is_negative:
                    hpgl.write('PD;\n')  # Pen down (start cutting)
                    z_is_negative = True
                elif z_value >= 0 and z_is_negative:
                    hpgl.write('PU;\n')  # Pen up (stop cutting)
                    z_is_negative = False

            # Handle rapid movement (G00)
            if line.startswith('G00'):
                coords = extract_coordinates(line)
                if coords:
                    # Apply scaling
                    scaled_coords = apply_scaling(coords)
                    hpgl.write(f'PU{scaled_coords};\n')  # Pen up for rapid move

            # Handle linear movement (G01)
            elif line.startswith('G01'):
                coords = extract_coordinates(line)
                if coords:
                    # Apply scaling
                    scaled_coords = apply_scaling(coords)
                    hpgl.write(f'PA{scaled_coords};\n')  # Move to point

            # Handle spindle stop (M5) or program end (M2)
            elif line.startswith('M5') or line.startswith('M2'):
                hpgl.write('PU;\n')  # Pen up (stop cutting)

            # Handle tool width with PW (optional)
            if 'S' in line:
                spindle_speed = extract_spindle_speed(line)
                hpgl.write(f'PW{spindle_speed};\n')  # Adjust pen width

        # End the HPGL program
        hpgl.write('SP;\n')

# Helper function to extract coordinates (X, Y)
def extract_coordinates(line):
    x_match = re.search(r'X([-+]?\d*\.\d+|\d+)', line)
    y_match = re.search(r'Y([-+]?\d*\.\d+|\d+)', line)

    x = x_match.group(1) if x_match else None
    y = y_match.group(1) if y_match else None

    if x and y:
        return f'{x},{y}'
    #return None

# Function to apply scaling
def apply_scaling(coords):
    x_str, y_str = coords.split(',')
    x_scaled = float(x_str) * scale_x
    y_scaled = float(y_str) * scale_y
    return f'{x_scaled:.1f},{y_scaled:.1f}'

# Helper function to extract spindle speed (optional)
def extract_spindle_speed(line):
    match = re.search(r'S(\d+)', line)
    if match:
        return match.group(1)
    #return None

# Call the function with your input and output files
parse_gcode('back.ngc', 'output.plt')


# For at få drill filerne til at virke, så skal man fjerne punktum fra X og Y koordinaterne, samt fjerne de aller sidste to decimaler:
#
# Fra: X-21.52500 Y18.02500
# Til: X-21525 Y18025
#
# Dette svarer til en factor 1000
