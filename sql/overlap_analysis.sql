SELECT
    provider,
    lang,
    COUNT(*) AS overlap_cases
FROM annotation_sheet
WHERE possible_drift = 1
AND possible_compression = 1
GROUP BY provider, lang
ORDER BY provider, lang;
