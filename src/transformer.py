
from validator import validator



def remove_duplicates(data):
    unique_list , duplicate_list = [] , []
    seen_ids = set()
    for row in data:
        txn_id = row['transaction_id'].strip()
        if txn_id not in seen_ids:
            seen_ids.add(txn_id)
            unique_list.append(row)
        else:
            duplicate_list.append(row)

    return unique_list , duplicate_list


def normalize(data):
    for row in data:
        row['customer_id'] = row['customer_id'].lower().strip()
        row['category'] = row['category'].lower().strip()
        row['status'] = row['status'].lower().strip()
        row['amount'] = float(row['amount'])
    return data


def trasform(data):
    valid_data , unvalid_data = validator(data)
    unique_data , duplicate_data = remove_duplicates(valid_data)
    data = normalize(unique_data)
    return data  ,  unvalid_data , duplicate_data 
