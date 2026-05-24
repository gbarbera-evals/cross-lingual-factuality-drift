SELECT
    provider,
    lang,
    COUNT(*) AS outputs,
    SUM(possible_drift) AS drift_candidates,
    ROUND(
        100.0 * SUM(possible_drift)
        / COUNT(*),
        2
    ) AS drift_rate
FROM annotation_sheet
GROUP BY provider, lang
ORDER BY provider, lang;