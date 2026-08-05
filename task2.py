import time
minutes = int(input("Enter test minutes: "))
seconds = int(input("Enter test seconds: "))
total_seconds = (minutes * 60) + seconds
if total_seconds <= 0 or  seconds < 0 or minutes < 0 or seconds > 59:
    print("Invalid test duration.")
    exit()
elif total_seconds > 300:
    print("Safety limit exceeded! Test duration capped to 05:00.")
    total_seconds = 300
while total_seconds >= 0:
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    if total_seconds > 30:
        print(f"\rPOWER ON | Remaining: {minutes:02}:{seconds:02}",end="")
    elif total_seconds > 10:
        print(f"\rSTABILIZING SYSTEM | Remaining: {minutes:02}:{seconds:02}", end="")
    else:
        print(f"\rCOOLDOWN PHASE | Do not touch | {minutes:02}:{seconds:02}", end="")
    time.sleep(1)
    total_seconds -= 1
print("\nPower test completed successfully.")