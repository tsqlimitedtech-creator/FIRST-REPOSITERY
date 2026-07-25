"""FastAPI wrapper for the Division-5 report consolidation service."""

from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from main import process_excel

app = FastAPI(
    title="Division-5 Excel Consolidation API",
    description="Upload a Division-5 Excel report and receive a unified tracking report.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Upload an Excel file to POST /process. See /docs for API documentation.",
    }


@app.post("/process")
async def process_excel_file(
    file: UploadFile = File(...), output_name: Optional[str] = None
) -> StreamingResponse:
    if not file.filename.lower().endswith((".xlsx", ".xls")):
        raise HTTPException(status_code=400, detail="Upload must be an .xlsx or .xls file.")

    suffix = Path(file.filename).suffix
    output_name = output_name or f"{Path(file.filename).stem}_unified.xlsx"

    with tempfile.TemporaryDirectory() as tmp_dir:
        input_path = Path(tmp_dir) / f"input{suffix}"
        output_path = Path(tmp_dir) / output_name

        input_path.write_bytes(await file.read())

        try:
            process_excel(str(input_path), str(output_path))
        except Exception as exc:
            raise HTTPException(status_code=400, detail=str(exc))

        if not output_path.exists():
            raise HTTPException(status_code=500, detail="Failed to generate consolidated report.")

        response = StreamingResponse(
            output_path.open("rb"),
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
        response.headers["Content-Disposition"] = f"attachment; filename={output_name}"
        return response
