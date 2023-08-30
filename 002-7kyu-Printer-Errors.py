# https://www.codewars.com/kata/56541980fa08ab47a0000040

def printer_error(s):
    good = "nopqrstuvwxyz"
    return f"{len([c for c in s if c in good])}/{len(s)}"
