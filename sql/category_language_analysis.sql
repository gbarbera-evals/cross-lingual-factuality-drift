SELECT
    category,
    provider,
    lang,
    ROUND(
        100.0 *
        SUM(possible_drift)
        / COUNT(*),
        2
    ) AS drift_rate
FROM annotation_sheet
GROUP BY category, provider, lang
ORDER BY category, provider, lang;