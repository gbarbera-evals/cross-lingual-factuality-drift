SELECT
COUNT(*) AS empty_labels
FROM annotation_sheet
WHERE
TRIM(drift_type) = '';