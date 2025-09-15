from parse_dumpsys import parse_data


def get_package_data(package, text):
    strings = text.splitlines()
    package_strings = []
    text_shift = 0
    for s in strings:
        if text_shift != 0:
            if len(s) - len(s.lstrip()) <= text_shift:
                break
            package_strings.append(s.strip())
        if package in s:
            text_shift = len(s) - len(s.lstrip())
    return "\n".join(package_strings)

package_name = "YouTube playerlib com.google.android.apps.youtube.music"

def main():
    with open("output.txt") as f:
        text = f.read()
        package_data = get_package_data(package_name, text)
        data = parse_data(package_data)
        for k, v in data.items():
            print(k + "=" + v)

if __name__ == "__main__":
    main()