import csv 
import json
import os

def generate_report(cleaned_data , invalid_date , duplicate_data):
    total_transaction = len(cleaned_data) + len(invalid_date) + len(duplicate_data)
    total_revenue = 0.0
    revenue_by_category = {}
    transactions_per_status = {}
    unique_customers = set()
    for row in cleaned_data:
        total_revenue += row['amount']
        revenue_by_category[row['category']] = revenue_by_category.get(row['category'], 0) + row['amount']
        transactions_per_status[row['status']] = transactions_per_status.get(row['status'], 0) + 1
        unique_customers.add(row['customer_id'])
    count_unique_customers = len(unique_customers)
    revenue_by_category = {k : round(v, 2) for k , v in revenue_by_category.items()}
    total_revenue=  round(total_revenue , 2)
    return {
            "invalid_data": len(invalid_date),
            "duplicate_data": len(duplicate_data),
            "cleaned_data": len(cleaned_data),
            "total_transaction": total_transaction,
            "total_revenue": total_revenue, 
            "revenue_by_category": revenue_by_category, 
            "transactions_per_status": transactions_per_status, 
            "count_unique_customers": count_unique_customers
            }


def export_to_csv(data , output_path):
    if not data:
        return
    if os.path.dirname(output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w' , newline='' , encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames= data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def export_to_json(data , output_path):
    if os.path.dirname(output_path):
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path , 'w', encoding='utf-8') as f:
        json.dump(data , f , indent=4)  

