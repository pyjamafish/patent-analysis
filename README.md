# Patent data analysis
This repo contains code that counts patent citations.

## Data sources
The patent and citation data used by this repository is provided by PatentsView.

The sample used by this repository is taken from KPSS.
> Leonid Kogan, Dimitris Papanikolaou, Amit Seru, Noah Stoffman, Technological Innovation, Resource Allocation, and Growth, The Quarterly Journal of Economics, Volume 132, Issue 2, May 2017, Pages 665–712, https://doi.org/10.1093/qje/qjw040

## `resources` packages layout
* `patentsview` is for the original files from [patentsview.org](https://patentsview.org/download/data-download-tables).
    These files are too large, so they are not committed.
* `truncated` contains the tables limited to 10 lines, used to test reading in the data.
* `mini` contains hand-made data, used to test data operations.
* `stripped` contains every row from `patentsview`, but without quotes and with only the relevant columns.
    These files are too large, so they are not committed.

