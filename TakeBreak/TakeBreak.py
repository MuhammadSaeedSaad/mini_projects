import webbrowser
import time

break_count = 0
total_breaks = 3

print("this program started on "+time.ctime())

for break_count in range(total_breaks):
    time.sleep(2*60*60)
    webbrowser.open(r'https://www.youtube.com/watch?v=fBkctbHyss4&ab_channel=HosariOfficial')
    break_count = break_count + 1