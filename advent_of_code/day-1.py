import requests


def main():
    input_data = get_data()
    print(f"{input_data}")

    elf_list = get_elves(input_data)
    print(f"{elf_list}")

    elf_list = calculate_calories(elf_list)
    print(f"{elf_list}")

    elf_list.sort(reverse=True)
    top_three = elf_list[0:3]
    print(f"Greediest elf consumed {max(elf_list)} calories")
    print(f"The greediest 3 elves consumed {sum(top_three)} calories")


def get_data():
    token = get_token()
    cookie = {
        "session": token
    }
    user_agent = {"User-Agent": "github.com/wimglenn/advent-of-code-data v{} by hey@wimglenn.com".format(
        requests.__version__)}
    response = requests.get("https://adventofcode.com/2022/day/1/input", cookies=cookie, headers=user_agent)
    return response.content.decode("utf-8")


def get_token():
    with open("token", "r") as file:
        return file.readline()


def get_elves(input_data):
    list_data = input_data.split("\n")
    elf_list = []
    elf = []
    for item in list_data:
        if item != "":
            elf.append(int(item))
        else:
            elf_list.append(elf)
            elf = []
    return elf_list


def calculate_calories(elf_list):
    result = []
    for elf in elf_list:
        result.append(sum(elf))

    return result


if __name__ == '__main__':
    main()
