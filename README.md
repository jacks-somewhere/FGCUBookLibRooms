# FGCUBookLibRooms

# Description
Book a Florida Gulf Coast University study room up to 2 weeks in advance using Selenium, Python, and Chrome. 

# Versions
There are 3 versions that you can pick from, please check the descriptions under each to pick the right version for you. Run the fgculibrary_SHOW_listrooms_selenium.py program first to make sure that everything is running correctly. Check the FAQ to see how to change date, time, room, and submited booking information.

## fgculibrary_SHOW_listrooms_selenium.py
- Tries all rooms in a list and books the first available. The list does NOT need to be any order such as ascending.
- **HEAD** (WILL show you the browser as it runs, do NOT interact with it)

## fgculibrary_allrooms_selenium.py
- Tries all the rooms in ascending order starting at 110 and books the first available.
- **Headless** (runs in the background, will not show you the browser)

## fgculibrary_listrooms_selenium.py
- Tries all rooms in a list and books the first available. The list does NOT need to be any order such as ascending.
- **Headless** (runs in the background, will not show you the browser)

# FAQ

## How do I changed the booking date, do not book rooms, book rooms, or my information?
  ### Booking Date
  - Look for the line "for i in range(3):". the number 3 will be how many days ahead the program moves. Changing this number to 7 will have the program check the rooms 7 days from the current date. For example, if the program was started on the 11th with "for i in range(7):". It will try and book a room on the 18th.
  ### Do Not Book Rooms
  - Look for the line "noBookRoomList = [113,116]" near the top of the program. To add a room number, add the number and a comma to the list. For example, [110,126,113,116] (110 and 126 where added). To remove a room, remove the number and it's comma. For example, [116] (113 was removed), [] (to have no excluded rooms), or [110,116] (113 was removed and 110 was added).
  ### Book Rooms
  - Look for the line "roomlist = [140,110,111,115,116,338]" near the top of the program. To add a room number, add the number and a comma. For example, [110,140,110,111,115,116,338] (110 was added).
  ### Changing Booking Information
  - Look for "firstname = 'first name here'" and the 2 lines under it. Enter your information in the correct areas INSIDE the ' ' WITHOUT spaces. For your email, enter the first section ONLY. It will add @eagle.fgcu.edu for you.

### I ran fgculibrary_xxx_selenium.py and I did not get a confirmation email. What happened and how do I fix it?
  Try running it again and check the logs for errors. Try running fgculibrary_SHOW_listrooms_selenium.py to see if you can find the issue.
  It may be, 
  - It encountered a random error and quit.
    - Run it again and try rebooting. That fixes a lot of issues.
  - The URL or an element changed and that caused it to break.
    - Changing the URL or element to the new one. Hint, use inspect for elements.
  - It is running to fast for your computer.
    - Try adding time to the time.sleeps or adding them in at necessary points.

### How do I start the program?
  Double click on the file to start it manually or have it set to start on a certain date and time.

### What do I need to install to get this working?
  You will need to download ChromeDriver, Python, and Selenium.
  - ChromeDriver
    - https://developer.chrome.com/docs/chromedriver/downloads
  - Python 
    - https://www.python.org/downloads/
  - Selenium 
    - https://selenium-python.readthedocs.io/

### What version was this program built on?
  As of 4/11/25, it was built and tested only on Windows 11, ChromeDriver stable ver 135.0.7049.84, Python ver 3.13.1, and Selenium ver 4.27.1
