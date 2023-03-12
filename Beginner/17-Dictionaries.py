# https://www.youtube.com/watch?v=rfscVS0vtbw&t=7637s

# Dictionaries are used to store data values in key:value pairs.

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"]) # prints November.
print(monthConversions.get("Dec")) # prints December.
print(monthConversions.get("Luv", "Not a valid key"))