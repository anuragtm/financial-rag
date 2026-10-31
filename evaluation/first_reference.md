# Development reference: Visa revenue growth

## Question
What was Visa's net revenue in fiscal year 2025 and fiscal year 2024, and what was the percentage increase?

## Source
- Document: visa_2025_annual_report.pdf
- Printed page: 60
- PDF viewer page position: Not yet verified
- Evidence: Net revenue row and corresponding column headings
- Reporting periods: Years ended September 30, 2025 and 2024
- Units: USD millions

## Verified inputs
- Fiscal 2025 net revenue: 40000
- Fiscal 2024 net revenue: 35926

## Calculation
- Absolute increase: 40000 - 35926 = 4074 million USD
- Percentage increase: (4074 / 35926) * 100
- Rounded percentage increase: 11.34%

## Expected result
Visa's net revenue increased from $35,926 million in FY 2024 to $40,000 in FY 2025, an increase of $4,074 million or aprrox 11.34% of growth

## Evaluation role
Manually checked development example
Do not count this example as an unseen final test question

## Extraction observations
- physical page 75 corresponds to printed page 60.
- pypdf preserved the relevant years, units and revenue figures.
- Other pages contain valid supporting evidence too.
- Year columns appear in different orders across tables. (like in page 4 vs page 75)
- Calculated growth from displayed figures is approx 11.34% whereas the report present growth rounded to 11%.

## Exact-phrase retrieval baseline
- Query: NET REVENUE
- Result: 22 matching pages, including verified PDF page 75.
- Query: How much did Visa's net revenue grow in 2025?
- Result: 0 matching pages.
- Limitation: exact-phrase matching misses relevant evidence when the question's wording does not appear verbatim in the document.


## Word-overlap ranking baseline(based on rank_pages.py)
- Query: How much did Visa's net revenue grow in 2025? (my question for all testing)
- Top 5 PDF pages(high scored) : Page 21, 43, 4, 6, 7
- Pages 21 and 43 scored 5 but did not contain the required revenue figures or actual year-over-year increase.
- Page 4 ranked third and contained both required revenue figures.
- Verified statement i.e. Page 75 scored 4 and was outside the top five.
- our current methosd is unique-word overlapping scoring(jaccard index)


## Observed Limitation
Matching all query words does not establish that a page answers the question. Words can occur in unrelated contexts on the same page. Equal scores are resolved by page number, not evidence quality.
- RAG needs evidence that supports the answer, not just matching words.

## BM25 baseline
- Same question and 136-page collection.
- Top five PDF pages: 21, 44, 22, 60, 61.
- Pages 21, 44, and 22 discuss related topics but do not answer the question about actual 2025 revenue growth.
- Pages 60 and 61 contain the required revenue figures.
- First supporting result: rank 4, versus rank 3 for word overlap.
- BM25 did not improve first-supporting-result rank on this example.

## Additional failure observations
- Related financial language is not sufficient evidence.
- Market opportunity figures must not be mistaken for company revenue.
- BM25 does not require every query word to match.
- One development question cannot establish overall retrieval quality.

## BM25 wording-sensitivity check
- Original question: first supporting evidence at rank 4.
- Rephrased question naming both years: supporting evidence at rank 1.
- Keywords "Visa net revenue 2024 2025": supporting evidence at rank 1.
- The same underlying information need produced different rankings.
- Several query terms changed, so no single cause was isolated.
- These are variations of one development example, not three independent test questions. Keep all results, including the weaker original resul