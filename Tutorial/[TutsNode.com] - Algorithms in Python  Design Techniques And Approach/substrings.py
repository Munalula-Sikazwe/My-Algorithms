def get_substrings(string):
    if len(string) == 0:
        return ""
    else:
        first_letter = string[0]
        rest = get_substrings(string[1:])
        result = ""

        for substring in rest.split(","):
            result += f",{first_letter}{substring}"
            result += f",{substring}"

        return result[1:]
