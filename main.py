def say_hello(user="world"):
  print(f"Hello, {user}")


def get_name():
  return input("What is your name? \n")


say_hello(get_name())