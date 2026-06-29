import streamlit as st
import pandas as pd

from datetime import datetime

from color_system import (
    generate_harmony_from_hex,
    hex_to_rgb,
    rgb_to_hex,
    is_valid_hex
)

st.title("Color Laboratory")

# -----------------------------
# estado del laboratorio
# -----------------------------
if "colors" not in st.session_state:
    st.session_state.colors = []

# -----------------------------
# input
# -----------------------------
st.subheader("Add Color")

input_mode = st.radio(
    "Input Type",
    ["HEX", "RGB"],
    horizontal=True
)

if input_mode == "HEX":

    hex_input = st.text_input(
        "HEX",
        "#FF5733"
    )

else:

    rgb_cols = st.columns(3)

    with rgb_cols[0]:
        r_input = st.number_input(
            "R",
            min_value=0,
            max_value=255,
            value=255
        )

    with rgb_cols[1]:
        g_input = st.number_input(
            "G",
            min_value=0,
            max_value=255,
            value=87
        )

    with rgb_cols[2]:
        b_input = st.number_input(
            "B",
            min_value=0,
            max_value=255,
            value=51
        )

# -----------------------------
# botones
# -----------------------------
col1, col2, col3 = st.columns([1, 1, 4])

with col1:
    add = st.button("Add Color")

with col2:
    clear = st.button("Clear Laboratory")

# -----------------------------
# agregar color a lista
# -----------------------------
if add:

    if input_mode == "HEX":

        if is_valid_hex(hex_input):

            hex_value = hex_input.upper()

            r, g, b = hex_to_rgb(hex_value)

            st.session_state.colors.append(
    {
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hex": hex_value,
        "r": r,
        "g": g,
        "b": b
    }
)

        else:
            st.error("Invalid HEX format")

    else:

        hex_value = rgb_to_hex(
            r_input,
            g_input,
            b_input
        )

        st.session_state.colors.append(
    {
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "hex": hex_value,
        "r": r_input,
        "g": g_input,
        "b": b_input
    }
)

# -----------------------------
# limpiar laboratorio
# -----------------------------
if clear:
    st.session_state.colors = []

# -----------------------------
# función visual
# -----------------------------
def box(color):
    return f"""
    <div style="text-align:center;">
        <div style="
            width:70px;
            height:30px;
            background:{color};
            border:1px solid #ccc;
            margin:auto;">
        </div>
        <div style="
            font-size:12px;
            margin-top:4px;">
            {color}
        </div>
    </div>
    """

# -----------------------------
# encabezados
# -----------------------------
headers = st.columns(10)

headers[0].markdown("**HEX**")
headers[1].markdown("**R**")
headers[2].markdown("**G**")
headers[3].markdown("**B**")
headers[4].markdown("**BASE**")
headers[5].markdown("**A1**")
headers[6].markdown("**A2**")
headers[7].markdown("**COMP**")
headers[8].markdown("**T1**")
headers[9].markdown("**T2**")

st.divider()

# -----------------------------
# render del laboratorio
# -----------------------------
for sample in st.session_state.colors:

    r = sample["r"]
    g = sample["g"]
    b = sample["b"]

    hex_color = sample["hex"]

    palette = generate_harmony_from_hex(hex_color)

    cols = st.columns(10)

    cols[0].write(hex_color)
    cols[1].write(r)
    cols[2].write(g)
    cols[3].write(b)

    cols[4].markdown(box(palette["base"]), unsafe_allow_html=True)
    cols[5].markdown(box(palette["analog_1"]), unsafe_allow_html=True)
    cols[6].markdown(box(palette["analog_2"]), unsafe_allow_html=True)
    cols[7].markdown(box(palette["complementary"]), unsafe_allow_html=True)
    cols[8].markdown(box(palette["triad_1"]), unsafe_allow_html=True)
    cols[9].markdown(box(palette["triad_2"]), unsafe_allow_html=True)
    # -----------------------------
# -----------------------------
# export CSV
# -----------------------------
if st.session_state.colors:

    export_data = []

    for sample in st.session_state.colors:

        palette = generate_harmony_from_hex(sample["hex"])

        export_data.append(
            {
                "DateTime": sample["datetime"],
                "HEX": sample["hex"],
                "R": sample["r"],
                "G": sample["g"],
                "B": sample["b"],
                "BASE": palette["base"],
                "A1": palette["analog_1"],
                "A2": palette["analog_2"],
                "COMP": palette["complementary"],
                "T1": palette["triad_1"],
                "T2": palette["triad_2"]
            }
        )

    df = pd.DataFrame(export_data)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Export CSV",
        data=csv,
        file_name="color_laboratory.csv",
        mime="text/csv"
    )