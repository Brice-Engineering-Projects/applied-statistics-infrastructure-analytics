# Structure

```text
applied infrastructure analytics/
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── assets/
│   ├── diagrams/
│   ├── figures/
│   └── images/
│
├── data/
│   ├── raw/
│   │   ├── hydrology/
│   │   ├── water_distribution/
│   │   ├── wastewater/
│   │   ├── groundwater/
│   │   └── reliability/
│   │
│   ├── processed/
│   │
│   └── external/
│
├── docs/
│   ├── architecture/
│   │   ├── project_structure.md
│   │   ├── coding_standards.md
│   │   └── development_workflow.md
│   │
│   ├── lessons/
│   │   ├── 00_pdf_cdf.md
│   │   ├── 01_descriptive_statistics.md
│   │   ├── 02_probability_distributions.md
│   │   ├── 03_return_periods.md
│   │   ├── ...
│   │
│   └── references/
│       ├── formulas.md
│       ├── probability_reference.md
│       └── bibliography.md
│
├── examples/
│   ├── histogram_example.py
│   ├── monte_carlo_example.py
│   ├── regression_example.py
│   └── bayesian_example.py
│
├── notebooks/
│   ├── 00_pdf_cdf/
│   │   └── lesson.ipynb
│   │
│   ├── 01_descriptive_statistics/
│   │   └── lesson.ipynb
│   │
│   ├── 02_probability_distributions/
│   │   └── lesson.ipynb
│   │
│   ├── 03_return_periods/
│   │   └── lesson.ipynb
│   │
│   └── ...
│
├── src/
│   └── applied_infrastructure_analytics/
│       │
│       ├── __init__.py
│       │
│       ├── io/
│       │   ├── __init__.py
│       │   ├── loaders.py
│       │   └── validation.py
│       │
│       ├── descriptive/
│       │   ├── __init__.py
│       │   ├── central_tendency.py
│       │   ├── dispersion.py
│       │   └── percentiles.py
│       │
│       ├── probability/
│       │   ├── __init__.py
│       │   ├── histogram.py
│       │   ├── pdf.py
│       │   ├── cdf.py
│       │   ├── distributions.py
│       │   └── return_periods.py
│       │
│       ├── inference/
│       │   ├── confidence_intervals.py
│       │   ├── hypothesis_tests.py
│       │   └── bayesian.py
│       │
│       ├── regression/
│       │   ├── linear.py
│       │   ├── polynomial.py
│       │   └── diagnostics.py
│       │
│       ├── timeseries/
│       │   ├── autocorrelation.py
│       │   ├── decomposition.py
│       │   └── forecasting.py
│       │
│       ├── reliability/
│       │   ├── markov.py
│       │   ├── monte_carlo.py
│       │   ├── reliability.py
│       │   └── risk.py
│       │
│       ├── visualization/
│       │   ├── histogram.py
│       │   ├── boxplot.py
│       │   ├── scatter.py
│       │   ├── time_series.py
│       │   └── probability.py
│       │
│       └── utils/
│           ├── constants.py
│           ├── formatting.py
│           └── helpers.py
│
├── tests/
│   ├── io/
│   ├── descriptive/
│   ├── probability/
│   ├── inference/
│   ├── regression/
│   ├── reliability/
│   └── visualization/
│
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
├── uv.lock
└── LICENSE
```
