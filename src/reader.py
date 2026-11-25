import csv

REQUIRED_COLUMNS = set ({'transaction_id', 'customer_id', 'category', 'amount', 'date', 'status'})
def reader(path):
    trascationList = []
    try :
        with open(path, 'r', newline='', encoding='utf-8') as f:
            csv_reader = csv.DictReader(f , delimiter='\t')
            for row in csv_reader:
                trascationList.append(row)
            if len(trascationList) == 0:
                raise ValueError('the file is empty')
            if set(trascationList[0].keys()) != REQUIRED_COLUMNS:
                raise ValueError('the file is not valid')
        return trascationList
    except FileNotFoundError:
        raise FileNotFoundError(f'the file not found {path}')
