def parse(feetinches):
    parts = feetinches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return feet, inches


def convert(feet, inches):
    meters= feet * 0.3048 + inches * 0.0254
    return meters
