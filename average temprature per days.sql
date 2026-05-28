SELECT
    temperature_category,
    COUNT(*) AS total_days,
    AVG(max_temperature) AS average_temperature
FROM `pipeline-497605.weather_pipeline.weather_data`
GROUP BY temperature_category
ORDER BY average_temperature DESC;