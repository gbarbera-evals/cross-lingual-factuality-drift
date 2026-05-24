SELECT
    COUNT(*) AS remaining_reviews
FROM annotation_sheet
WHERE possible_drift = 1
AND (
    drift_type IS NULL
    OR drift_type = ''
);