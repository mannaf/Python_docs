# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('Invalid user response')
#         print(reminder)

def f(arg=5):
    print(arg)

f(6)