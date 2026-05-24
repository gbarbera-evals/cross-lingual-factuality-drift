SELECT
    prompt_id,
    provider,
    MAX(response_chars)
    -
    MIN(response_chars)
    AS char_gap
FROM annotation_sheet
GROUP BY prompt_id, provider
ORDER BY char_gap DESC
LIMIT 10;