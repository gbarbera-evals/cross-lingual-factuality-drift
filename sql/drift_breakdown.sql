SELECT
    provider,
    drift_type,
    COUNT(*) AS cases
FROM annotation_sheet
WHERE drift_type != ''
GROUP BY provider, drift_type
ORDER BY provider, cases DESC;