

status_codes = [200, 200, 404, 200, 500, 503, 404, 200]

success = status_codes.count(200)
failures = len([code for code in status_codes if code >= 400])
failure_rate = failures / len(status_codes) * 100

print("Total Requests:", len(status_codes))
print("Successful Requests:", success)
print("Failed Requests:", failures)
print("Failure Rate:", round(failure_rate, 2), "%")
