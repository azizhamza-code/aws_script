import subprocess
import json


lambda_function_name = "http-crud-tutorial-function"
aws_command = "C:/Users/Hamza/Documents/project/aws_lab/.venv/Scripts/aws.cmd"

# Run the aws logs describe-log-groups command as a subprocess, and capture the output
describe_log_groups_output = subprocess.run(
    [aws_command,"logs", "describe-log-groups"],
    capture_output=True
)

# Parse the JSON output of the describe-log-groups command
describe_log_groups_json = json.loads(describe_log_groups_output.stdout)

# Extract the logGroupName of the Lambda function from the JSON data
log_group_name = None
for log_group in describe_log_groups_json["logGroups"]:
    if lambda_function_name in log_group["logGroupName"]:
        log_group_name = log_group["logGroupName"]
        break

# Print the logGroupName of the Lambda function
print(f"logGroupName: {log_group_name}")

# Use the logGroupName as the value of the --log-group-name parameter in the aws logs filter-log-events command
filter_log_events_output = subprocess.run(
    [aws_command, "logs", "filter-log-events", "--log-group-name", log_group_name, "--output", "text"],
    capture_output=True
)

# Print the output of the filter-log-events command
"""with open("logs.txt", "w") as f:
    f.write(filter_log_events_output.stdout.decode())"""