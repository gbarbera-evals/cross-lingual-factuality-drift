SELECT
    provider,
    lang,
    TRIM(drift_type) AS drift_type,
    COUNT(*) AS cases
FROM annotation_sheet
WHERE drift_type != ''
GROUP BY
provider,
lang,
TRIM(drift_type)
ORDER BY provider, lang;