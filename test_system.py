from color_system import generate_harmony

palette = generate_harmony(255, 87, 51)

print(palette)
def generate_harmony_from_hex(hex_color):
    if not is_valid_hex(hex_color):
        raise ValueError("HEX inválido")

    r, g, b = hex_to_rgb(hex_color)

    return generate_harmony(r, g, b)