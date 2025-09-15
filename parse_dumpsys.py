import re

def parse_data(data):
    result = {}
    strings = data.split("\n")
    result.update(separate_objects(strings))
    result.update(separate_key_values(strings))
    return result

def separate_objects(strings):
    result = {}

    for string_idx, string in enumerate(strings):
        start_idx = 0
        counter = 0

        for idx, ch in enumerate(string):
            if counter == 0:
                start_idx = idx
            if re.match(r"[{\[]", ch):
                counter += 1
            elif re.match(r"[}\]]", ch):
                counter -= 1

                if counter == 0:
                    while start_idx > 0 and string[start_idx] != ",":
                        start_idx -= 1
                    new_string = remove_redundant_comas(string[start_idx:idx + 1])
                    key_value = get_key_value(new_string.strip())
                    result[key_value[0]] = key_value[1]
                    string = string[0:start_idx] + string[idx + 1:]
                    string = remove_redundant_comas(string)
                    strings[string_idx] = string
        if len(string) == 0:
            strings.pop(string_idx)

    return result

def separate_key_values(strings):
    result = {}

    for string in strings:
        if len(re.findall(r",|\n|$", string)) > len(re.findall(r"[:=]", string)):
            key_value = get_key_value(string.strip())
            result[key_value[0]] = key_value[1]
            continue

        string = string + "\n"
        start_idx = 0
        counter = 0

        for idx, ch in enumerate(string):
            if re.match(r"[=:]", ch):
                counter += 1
            elif re.match(r",|\n|$", ch):
                counter -= 1

                if counter == 0 or idx == len(string) - 1:
                    key_value = get_key_value(string[start_idx:idx].strip())
                    result[key_value[0]] = key_value[1]
                    start_idx = idx + 1

    return result

def remove_redundant_comas(string):
    if string.endswith(","):
        string = string[:-1]
    if string.startswith(","):
        string = string[1:]
    return string

def get_key_value(string):
    for idx, ch in enumerate(string):
        if re.match(r"[=:]", ch):
            return [string[0:idx].strip(), string[idx + 1:].strip()]
    return None