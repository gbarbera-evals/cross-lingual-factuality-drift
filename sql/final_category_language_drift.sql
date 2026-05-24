SELECT
    category,
    provider,
    lang,
    COUNT(*) AS outputs,
    SUM(
        CASE
            WHEN TRIM(drift_type) != 'no_drift'
            THEN 1
            ELSE 0
        END
    ) AS confirmed_drift,
    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN TRIM(drift_type) != 'no_drift'
                THEN 1
                ELSE 0
            END
        )
        / COUNT(*),
        2
    ) AS drift_rate
FROM annotation_sheet
GROUP BY category, provider, lang
ORDER BY category, provider, lang;