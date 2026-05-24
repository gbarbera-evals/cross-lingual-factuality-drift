import duckdb

con = duckdb.connect()

con.execute("""
CREATE OR REPLACE TABLE annotation_sheet AS
SELECT *
FROM read_csv_auto(
'../data/prompts/annotation_sheet.csv'
)
""")

query = open(
"../sql/final_category_language_drift.sql",
encoding="utf-8"
).read()

result = con.execute(
query
).fetchdf()

print(result)