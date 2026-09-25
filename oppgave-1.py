# Task 1.1
# try:
#     study_sessions = int(input("How many study sessions: "))
#     minutes_per_session = int(input("How many minutes per session: "))
#     total_time = minutes_per_session * study_sessions #To make it easy to convert the time to h and m
#     while study_sessions <= 0 or minutes_per_session <= 0:
#         print("Please enter a higher number than 0.")
# except ValueError:
#     print("Error, try again. Please make sure the number are whole (1,2,3) and higher than 0.")
#
# else :
#     time = int(total_time)
#     hour = time // 60
#     minute = time % 60
#     if time >= 60:
#         print(f"The total time is {hour} hours and {minute} minutes.")
#     else :
#         print(f"The total time is {time} minutes.")
from typing import cast


# Task 1.2
# Samler alltid funkjsonene på toppen:
def text_reverse(text: str):
    return text[::-1]
def counting_without_space(text: str):
    without = len(text.replace(" ", ""))
    return without
"""
Text_reverse gir teksten tilbake baklengs.
Counting_without_space lar deg bruke len() uten at den teller med mellomrom.
Parameteren er string.

"""

# text = str(input("Please enter text here: "))
# print("Your text in reverse:", text_reverse(text))
# print("Antall tegn i teksten (med mellomrom):", len(text))
# print("Antall tegn i teksten (uten mellomrom):",counting_without_space(text))
# text_in_lower = text.lower()
# print("Teksten din i små bokstaver:", text_in_lower)
# word_python = "python"
# print("Inneholder teksten ordet python:", (word_python in text_in_lower))


# Task 1.3
# try:
#     numb1 = int(input("Please enter a starting number: "))
#     numb2 = int(input("Please enter an ending number: "))
# except ValueError:
#     print("Error, try again. Please enter a whole number. For example 1, 2 or 3.")
# except ZeroDivisionError:
#     print("Error, try again. Cannot divide by zero. ")






