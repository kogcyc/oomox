import sys
from string import Template

def scale_hex(hex_color, scale_factor):
    """
    Scales the RGB values of a hex color.
    
    Args:
        hex_color (str): Hex color code (6 characters, e.g. '001122').
        scale_factor (float): Multiplier for RGB channels (e.g. 1.2 to lighten, 0.8 to darken).
        
    Returns:
        str: Scaled hex color code.
    """
    # Extract R, G, B components
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    
    # Scale with clamping (0-255)
    r = max(0, min(255, int(r * scale_factor)))
    g = max(0, min(255, int(g * scale_factor)))
    b = max(0, min(255, int(b * scale_factor)))
    
    # Return formatted hex
    return f"{r:02x}{g:02x}{b:02x}"

# Read arguments
filename = sys.argv[1]
color1 = sys.argv[2]
color2 = sys.argv[3]
color3 = sys.argv[4]
color4 = sys.argv[5]

with open(filename,'r') as fp:
    fs = fp.read()

replaced = fs.replace("{color1}", color1).replace("{color2}", color2).replace("{color3}", color3).replace("{color4}", color4)
print(replaced)
