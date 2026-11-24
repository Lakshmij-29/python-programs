import pandas as pd

bank = pd.read_csv("bank_statement.csv")
records = pd.read_csv("company_ledger.csv")
bank["Amount"] = pd.to_numeric(bank["Amount"], errors="coerce")
records["Amount"] = pd.to_numeric(records["Amount"], errors="coerce")
matched = bank.merge(records, on=["Transaction_ID", "Amount"], how="inner")
unmatched = bank[~bank["Transaction_ID"].isin(matched["Transaction_ID"])]
matched.to_csv("matched_transactions.csv", index=False)
unmatched.to_csv("unmatched_transactions.csv", index=False)
print("Matched:", len(matched))
print("Unmatched:", len(unmatched))
