SELECT
    provider,
    COUNT(*) AS confirmed_cases
FROM annotation_sheet
WHERE drift_type != ''
AND drift_type != 'no_drift'
GROUP BY provider;