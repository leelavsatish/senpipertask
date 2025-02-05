import re

# Function to count 200 status codes in access logs
def count_200_status(log_file):
    pattern = r'\s200\s'  #Pattern for status code " 200 "
    count = 0

    with open(log_file, "r") as file:
        for line in file:
            if re.search(pattern, line):
                count += 1

    return count

log_file = "access.log" 
success_count = count_200_status(log_file)

# Print the count of HTTP 200 status codes
print(f"HTTP Success response Count: {success_count}")