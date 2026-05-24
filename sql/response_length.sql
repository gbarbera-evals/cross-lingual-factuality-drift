SELECT
    category,
    provider,
    lang,
    ROUND(
        AVG(response_chars),
        1
    ) AS avg_chars
FROM annotation_sheet
GROUP BY category, provider, lang
ORDER BY category, provider, lang;