#Task 1.1
study_sessions = int(input("How many study sessions: "))
minutes_per_session = int(input("How many minutes per session: "))
total_time = minutes_per_session * study_sessions
if study_sessions <= 0 or minutes_per_session <= 0:
    print("Error, try again. Please make sure the numbers are whole and higher than 0.")
else :
    time = int(total_time)
    hour = time // 60
    minute = time % 60
    if time >= 60:
        print(f"The total time is {hour} hours and {minute} minutes.")
    else :
        print(f"The total time is {time} minutes.")


