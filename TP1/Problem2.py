total_seconds = 9875
hours = (total_seconds)//3600
remaining_second = (total_seconds) % 3600
minutes = (remaining_second) // 60
seconds = (remaining_second) % 60

print(f"{hours} h {minutes} min {seconds} s")

#Check total_seconds equal remaining_second 
rebuild_second = hours*3600 + minutes*60 + seconds
print(f"Check: {rebuild_second == total_seconds}")

#Test the method with difference total_sceonds
for test_seconds in (3600, 59, 86399):
    h = (test_seconds) // 3600
    remain_seconds = (test_seconds) % 3600
    m = (remain_seconds)//60
    s = (remain_seconds) % 60
    print(f"{test_seconds} seconds = {h} h {m} min {s} s")