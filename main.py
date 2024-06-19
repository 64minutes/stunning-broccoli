def say_hello(user="world", occupation = "Jobless"):
  print(f"Hello, {user}, my occupation is {occupation}.")


def get_name():
  return input("What is your name?\n")

def get_occupation():
  return input("What is your occupation?\n")


if __name__ == "__main__":
  say_hello(get_name(), get_occupation())