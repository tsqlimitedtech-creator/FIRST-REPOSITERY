# Division-5 Excel Consolidation API

This repository now includes a FastAPI service for processing Division-5 daily report Excel files.

## Features

- Reads `Sheet2` from uploaded `.xlsx` or `.xls` files
- Skips the first 3 header rows
- Normalizes columns to a standard schema
- Adds tracking metadata fields
- Returns a consolidated Excel file with a single sheet named `Unified_Tracking_Master`

## Run the service

```bash
pip install .
uvicorn app:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Endpoints

- `GET /` — basic health/info response
- `POST /process` — upload an Excel file and download a consolidated output
- `GET /docs` — interactive OpenAPI documentation

### POST /process

Use `multipart/form-data` with the following fields:

- `file`: the uploaded `.xlsx` or `.xls` report
- `output_name` (optional): desired output filename

Example cURL:

```bash
curl -X POST "http://127.0.0.1:8000/process" \
  -F "file=@sample.xlsx" \
  -F "output_name=sample_unified.xlsx" \
  --output sample_unified.xlsx
```

## Local CLI usage

```bash
python main.py -i input.xlsx -o output.xlsx
```

## Notes

- `main.py` contains the core Excel processing logic
- `app.py` exposes that logic via a web API
- Dependencies are managed via `pyproject.toml`
