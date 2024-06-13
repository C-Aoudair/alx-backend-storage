-- This script  lists all bands with Glam rock as their main style, ranked by their longevity

SELECT 
    band_name, 
    (2022 - formed) - (CASE WHEN split != '0' THEN (2022 - CAST(split AS UNSIGNED)) ELSE 0 END) AS lifespan
FROM 
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
