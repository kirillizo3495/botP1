# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("Hello Bot!!!!")

    # Press the green button in the gutter to run the script.
    print("Привет, напиши как тебя зовут.")
    name = input()
    print("А сколько тебе лет?")
    old = int(input())
    if old <= 20:
        print("Ооо ты очень молодой ", name ,".")
    else:
        print('Ого тебе уже больше 20 ты уже староват', name)


if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
