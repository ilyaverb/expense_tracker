SELECT c_width AS width, c_depth AS depth, c_height AS height, count
FROM
	(
		SELECT
		CEIL(width / 5) * 5 AS c_width, CEIL(depth / 5) * 5 AS c_depth, CEIL(height / 5) * 5 AS c_height,
		COUNT(*)
		FROM public.notebooks_notebook
		GROUP BY c_width, c_depth, c_height
	) AS ceil_values
ORDER BY width, depth, height;