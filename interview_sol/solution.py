import re
from collections import Counter

# regex pattern to match the log
pattern = re.compile(r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.*)')

# function to parse the line
def parse_lines(line):
    match = pattern.match(line)
    if match:
        timestamp, time, level, server_message = match.groups()
        return {
            "timestamp": timestamp,
            "time": time,
            "level": level,
            "server_message": server_message
        }
    else:
        return None


# counters and storage
error_count = 0
error_types = Counter()
replica_lags = []

with open("/home/ubuntu/release.log", "r") as f:
    for line in f:
        data = parse_lines(line)

        if not data:
            continue

        # Count ERROR lines
        if data["level"] == "ERROR":
            error_count += 1

            # extract error type (last word)
            error_type = data["server_message"].strip().split()[-1]
            error_types[error_type] += 1

        # Extract replica lag
        lag_match = re.search(r"Replica lag detected: (\d+) seconds", data["server_message"])
        if lag_match:
            replica_lags.append(int(lag_match.group(1)))


# Unique errors
unique_errors = list(error_types.keys())

# Repeated errors
repeated_errors = [err for err, count in error_types.items() if count > 1]

# Max lag
max_lag = max(replica_lags) if replica_lags else 0

# Decision logic
block = False

if "ReplicationLagThresholdExceeded" in error_types:
    block = True

if repeated_errors:
    block = True

decision = "BLOCK" if block else "ALLOW"


# Output
print(f"Errors found: {error_count}\n")

print("Unique errors:")
for err in unique_errors:
    print(f"- {err}")

print("\nRepeated errors:")
if repeated_errors:
    for err in repeated_errors:
        print(f"- {err}")
else:
    print("None")

print(f"\nMax replica lag observed: {max_lag} seconds")
print(f"\nRelease decision: {decision}")

# Exit code (important for CI/CD)
exit(1 if decision == "BLOCK" else 0)
