import datetime

# Define time differences for each branch from UTC
portland_offset = datetime.timedelta(hours=-7)  # Pacific Daylight Time (PDT)
nyc_offset = datetime.timedelta(hours=-4)  # Eastern Daylight Time (EDT)
london_offset = datetime.timedelta(hours=1)  # British Summer Time (BST)

# Get current UTC time
utc_time = datetime.datetime.now(datetime.timezone.utc)

# Calculate current time in each branch's time zone
portland_time = utc_time + portland_offset
nyc_time = utc_time + nyc_offset
london_time = utc_time + london_offset

# Define opening and closing hours for each branch
opening_time = datetime.time(9, 0)
closing_time = datetime.time(17, 0)

# Determine if each branch is open or closed
portland_status = "Open" if opening_time <= portland_time.time() < closing_time else "Closed"
nyc_status = "Open" if opening_time <= nyc_time.time() < closing_time else "Closed"
london_status = "Open" if opening_time <= london_time.time() < closing_time else "Closed"

# Print the status of each branch
print("Portland HQ is", portland_status)
print("NYC branch is", nyc_status)
print("London branch is", london_status)
