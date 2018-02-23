import webbrowser;
import time;

total_breaks = 3;
break_count = 0;
print("The program started at " + time.ctime());
while(break_count < total_breaks):
    time.sleep(10)  
    webbrowser.open("http://www.youtube.com")
    break_count += 1
print("The program has ended at " + time.ctime());
