responses = [200, 200, 500, 404, 200]

success = responses.count(200)
errors = len(responses) - success

print("Successful Requests:", success)
print("Failed Requests:", errors)

if errors > 2:
    print("API health unstable")
else:
    print("API running normally")
