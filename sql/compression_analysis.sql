SELECT
    provider,
    lang,
    SUM(possible_compression) AS compression_cases,
    ROUND(
        100.0 *
        SUM(possible_compression)
        / COUNT(*),
        2
    ) AS compression_rate
FROM annotation_sheet
GROUP BY provider, lang
ORDER BY provider, lang;