from reader import reader
from transformer import trasform
from reporter import generate_report, export_to_csv, export_to_json


def main(input_path, cleaned_csv_path, report_json_path, invalid_json_path , valid_json_path , duplicate_json_path):
    try:
        raw_data = reader(input_path)
        cleaned_data, invalid_data, duplicate_data = trasform(raw_data)

        report = generate_report(cleaned_data, invalid_data, duplicate_data)

        export_to_csv(cleaned_data, cleaned_csv_path)
        export_to_json(report, report_json_path)
        export_to_json(invalid_data,  invalid_json_path)
        export_to_json(cleaned_data,  valid_json_path)
        export_to_json(duplicate_data,  duplicate_json_path)


        print("ETL pipeline completed successfully.")
        print(f"Total records read: {len(raw_data)}")
        print(f"Valid: {len(cleaned_data)} | Invalid: {len(invalid_data)} | Duplicates: {len(duplicate_data)}")
        print(f"Cleaned CSV saved to: {cleaned_csv_path}")
        print(f"JSON report saved to: {report_json_path}")

    except (FileNotFoundError, ValueError, OSError) as e:
        print(f"Pipeline error: {e}")


if __name__ == "__main__":
    main(
        input_path="data/input/raw_transactions.csv",
        cleaned_csv_path="data/output/cleaned_data.csv",
        report_json_path="data/output/report.json",
        invalid_json_path="data/output/invalid_data.json",
        valid_json_path="data/output/valid_data.json",
        duplicate_json_path="data/output/duplicate_data.json"
    )