log_file = "all.log"
warning_logfile = "warning.log"

warnings = []
with open(log_file, 'r') as file:
    for line in file.readlines():
        if "WARNING" in line:
            warnings.append(line)

with open(warning_logfile, 'w') as file:
    for item in warnings:
        file.write(item)
