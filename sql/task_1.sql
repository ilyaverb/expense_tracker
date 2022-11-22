SELECT public.notebooks_brand.title, COUNT(public.notebooks_notebook.brand_id)
FROM public.notebooks_brand
JOIN public.notebooks_notebook ON public.notebooks_brand.id=public.notebooks_notebook.brand_id
GROUP BY public.notebooks_brand.title
ORDER BY count DESC;