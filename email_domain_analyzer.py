from collections import Counter

with open("email_list.txt", encoding="utf-8") as file:
    emails = [line.strip().lower() for line in file if "@" in line]
domains = [email.rsplit("@", 1)[1] for email in emails]
counts = Counter(domains)
for domain, count in counts.most_common():
    print(domain, ":", count)
print("Unique domains:", len(counts))
