
# Project Changelog

All important changes to the project and dataset
are recorded here.

## [0.2.0] - Stage 2: Data Acquisition and Validation

### Added
- Acquired the ULB credit card fraud dataset.
- Added dataset metadata and data dictionary.
- Added ROCCC data-quality assessment.
- Added Python data-validation script.
- Added reproducible data-cleaning script.

### Validation
- Checked expected column names and ordering.
- Checked numeric data types.
- Checked missing values.
- Checked infinite values.
- Checked Class label values.
- Checked negative transaction time.
- Reported exact duplicate records.

### Cleaning Decisions
- Preserved the original raw CSV.
- Did not automatically remove duplicate records.
- Did not automatically remove outliers.
- Did not modify transaction amounts.
- Retained Class for evaluation only.

### Pending
- Run validation against the downloaded dataset.
- Review actual validation output.
- Confirm processed dataset creation.
- Investigate any unexpected findings.
