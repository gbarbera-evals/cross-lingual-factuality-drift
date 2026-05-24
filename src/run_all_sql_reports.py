import duckdb
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_PATH = BASE_DIR / "data" / "prompts" / "annotation_sheet.csv"
SQL_DIR = BASE_DIR / "sql"
REPORTS_DIR = BASE_DIR / "reports"

REPORTS_DIR.mkdir(exist_ok=True)

con = duckdb.connect()

con.execute(f"""
CREATE OR REPLACE TABLE annotation_sheet AS
SELECT *
FROM read_csv_auto('{DATA_PATH.as_posix()}')
""")

for sql_file in SQL_DIR.glob("*.sql"):
    query = sql_file.read_text(encoding="utf-8")
    result = con.execute(query).fetchdf()

    output_path = REPORTS_DIR / f"{sql_file.stem}.csv"
    result.to_csv(output_path, index=False, encoding="utf-8")

    print(f"Saved: {output_path}")