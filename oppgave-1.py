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
#Samler alltid funkjsonene på toppen, her funksjonen jeg senere henter frem for å reversere teksten:
def text_reverse(text: str):
    return text[::-1]

# antall tegn med og uten mellomrom
# teksten med små bokstaver
# om teksten inneholder ordet python, uavhengig av store og små bokstaver

text = str(input("Please enter text here: "))

print("Your text in reverse:", text_reverse(text))

word_python = "Python" or "PYTHON" or "python"













