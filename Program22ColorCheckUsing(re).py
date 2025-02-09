"""
    This is an upgraded program for the color code this involves one more library which is webcolors to actually print
    the color name to us instead of just printing what we entered...
    Extra function involved is get_color_name()
    next change is in if statement...
"""

import re
import webcolors


def get_color_name(hex_code):
    try:
        return webcolors.hex_to_name(hex_code)
    except ValueError:
        return "No matching color name found."


def main():
    code = input("Hexadecimal Color Code: ")

    pattern = r"^#[0-9a-fA-F]{6}$"
    match = re.search(pattern, code)

    if match:
        color_name = get_color_name(code)
        if color_name != "No matching color name found.":
            print(f"Valid Hexadecimal Color Code!\nMatched with: {match.group()}\nColor Name: {color_name}")
        else:
            print("Valid Hexadecimal Code, but no matching color name found.")
    else:
        print("Invalid Hexadecimal Color Code!")


main()
