log_entry = "   ERROR-CODE: 404 - file_not_found - admin_node_7   "
print(f"the origin text: {log_entry}")

clean=log_entry.strip()
print(f"clean text: {clean}")

Standardize=clean.upper()
print(f"Convert text to uppercase: {Standardize}")

Replace=Standardize.replace("-", "_")
print(f"replace - to _ : {Replace}")

Extract=Replace[12:15]
print(f" text with 404: {Extract}")


Split=Replace.strip(" ")
print(f"Split the text: {Split}")
