import re

# Function to count HTTP status codes in access logs
def count_status_codes(log_file_path):
    status_categories = {
        "1xx": r"\s1\d{2}\s",
        "2xx": r"\s2\d{2}\s",
        "3xx": r"\s3\d{2}\s",
        "4xx": r"\s4\d{2}\s",
        "5xx": r"\s5\d{2}\s"
    }

    # Initialize a dictionary with zero counts
    status_counts = {"1xx": 0, "2xx": 0, "3xx": 0, "4xx": 0, "5xx": 0}

    with open(log_file_path, "r") as file:
        for line in file:
            for category, pattern in status_categories.items():
                if re.search(pattern, line):
                    status_counts[category] += 1

    return status_counts

# Example usage
log_file_path = "access.log"  # Replace with the path to your log file
status_counts = count_status_codes(log_file_path)

# Print the count of each status category
for category, count in status_counts.items():
    print(f"{category}: {count}")