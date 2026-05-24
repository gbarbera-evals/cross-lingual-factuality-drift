SELECT
    category,
    provider,
    SUM(possible_drift) AS drift_cases,
    ROUND(
        100.0 *
        SUM(possible_drift)
        / COUNT(*),
        2
    ) AS drift_rate
FROM annotation_sheet
GROUP BY category, provider
ORDER BY category, provider;