import colorsys

def rgb_to_hex(r, g, b):
    return "#{:02X}{:02X}{:02X}".format(r, g, b)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hsl(r, g, b):
    r, g, b = [x / 255.0 for x in (r, g, b)]
    return colorsys.rgb_to_hls(r, g, b)

def hsl_to_rgb(h, l, s):
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return int(r * 255), int(g * 255), int(b * 255)

def generate_harmony(r, g, b):
    h, l, s = rgb_to_hsl(r, g, b)

    def to_rgb(hue):
        return hsl_to_rgb(hue % 1.0, l, s)

    return {
        "base": rgb_to_hex(r, g, b),
        "complementary": rgb_to_hex(*to_rgb(h + 0.5)),
        "analog_1": rgb_to_hex(*to_rgb(h + 0.08)),
        "analog_2": rgb_to_hex(*to_rgb(h - 0.08)),
        "triad_1": rgb_to_hex(*to_rgb(h + 1/3)),
        "triad_2": rgb_to_hex(*to_rgb(h + 2/3)),
    }

def is_valid_hex(hex_color):
    if len(hex_color) != 7:
        return False

    if not hex_color.startswith("#"):
        return False

    try:
        int(hex_color[1:], 16)
        return True
    except ValueError:
        return False
def generate_harmony_from_hex(hex_color):
    if not is_valid_hex(hex_color):
        raise ValueError("HEX inválido")

    r, g, b = hex_to_rgb(hex_color)

    return generate_harmony(r, g, b)