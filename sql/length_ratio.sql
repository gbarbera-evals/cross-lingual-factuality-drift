SELECT
    provider,
    lang,
    ROUND(
        AVG(length_ratio),
        3
    ) AS avg_ratio
FROM annotation_sheet
GROUP BY provider, lang;