pipeline_runs = [
    "Success",
    "Success",
    "Failed",
    "Success",
    "Failed"
]

successful = pipeline_runs.count("Success")
failed = pipeline_runs.count("Failed")

print("Total Runs:", len(pipeline_runs))
print("Successful Runs:", successful)
print("Failed Runs:", failed)

print("Success Rate:", round(successful / len(pipeline_runs) * 100, 2), "%")
