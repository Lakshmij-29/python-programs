from collections import Counter
import re

error_counts = Counter()
with open("application.log", encoding="utf-8") as file:
    for line in file:
        match = re.search(r"\b(ERROR|WARNING|CRITICAL)\b", line)
        if match:
            error_counts[match.group()] += 1
for level, count in error_counts.most_common():
    print(f"{level}: {count}")
print("Total flagged events:", sum(error_counts.values()))
