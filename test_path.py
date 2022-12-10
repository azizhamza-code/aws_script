
import subprocess
import json


aws_command = "C:/Users/Hamza/Documents/project/aws_lab/.venv/Scripts/aws.cmd"
lambda_function_name = "http-crud-tutorial-function"

# Run the aws logs describe-log-groups command as a subprocess, and capture the output
describe_log_groups_output = subprocess.run(
    [aws_command,"logs", "describe-log-groups"],
    capture_output=True
)
describe_log_groups_json = json.loads(describe_log_groups_output.stdout)

print(describe_log_groups_json)
log_group_name = None
for log_group in describe_log_groups_json["logGroups"]:
    if lambda_function_name in log_group["logGroupName"]:
        log_group_name = log_group["logGroupName"]
        break

# Print the logGroupName of the Lambda function
print(f"logGroupName: {log_group_name}")