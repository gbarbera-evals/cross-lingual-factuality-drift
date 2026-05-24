SELECT
    category,
    provider,
    lang,
    COUNT(*) AS confirmed_cases
FROM annotation_sheet
WHERE
TRIM(drift_type)
!= 'no_drift'
AND
TRIM(drift_type)
!= ''
GROUP BY
category,
provider,
lang
ORDER BY
provider,
lang,
confirmed_cases DESC;