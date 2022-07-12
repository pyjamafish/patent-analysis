import polars as pl
from importlib import resources
from datetime import datetime

RESOURCE_PATH = resources.files("patent_analysis.resources.mini")


def get_patent_lf() -> pl.LazyFrame:
    return (
        pl.scan_csv(
            file=str(RESOURCE_PATH.joinpath("patent.tsv")),
            sep="\t",
            dtypes={"date": pl.Date}
        )
        .select(["id", "date"])
        .filter(
            pl.col("date") >= pl.lit(datetime(1999, 1, 1))
        )
    )


def get_citation_lf() -> pl.LazyFrame:
    return (
        pl.scan_csv(
            file=str(RESOURCE_PATH.joinpath("uspatentcitation.tsv")),
            sep="\t",
        )
        .select(["patent_id", "citation_id"])
    )


print(
    get_citation_lf()
    .join(get_patent_lf(), left_on="citation_id", right_on="id")
    .rename(
        {
            "patent_id": "citing_patent",
            "citation_id": "cited_patent",
            "date": "cited_patent_issue_date"
        }
    )
    .filter(
        pl.col("cited_patent_issue_date") <= pl.lit(datetime(2019, 12, 31))
    )
    .collect()
)
