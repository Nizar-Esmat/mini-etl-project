from datetime import datetime
from collections import Counter

STATUS = ['completed', 'refunded', 'pending']

def validator(data):
    valid_data = []
    invalid_data = []
    for row in data:
        errors = []

        for filds in ("transaction_id", "customer_id", "category"):
            if not (row.get(filds) or "").strip():
                errors.append(f"{filds} is empty")

        data_va = (row.get('date') or "").strip()
        try:
            datetime.strptime(data_va, "%Y-%m-%d")
        except ValueError:
            errors.append("Invalid date format")
        amout_val = (row.get('amount') or "").strip()
        try:
            if float(amout_val) <= 0:
                errors.append("Invalid amount")
        except ValueError:
            errors.append("Invalid amount")

        status_val = (row.get('status') or "").strip().lower()
        if status_val not in STATUS:
            errors.append("Invalid status")

        if errors:
            invalid_data.append({"row": row, "errors": errors})
        else:
            valid_data.append(row)

    return valid_data , invalid_data


def getidcount(data):
    id_count = Counter(row['transaction_id'] for row in data)
    return [{'id': id, 'count': count} for id, count in id_count.items()]


def checkDublicate(data):
    orignalids = [row['transaction_id'] for row in data]
    setorignalids = set(orignalids)
    return len(orignalids) != len(setorignalids)