import io
from pathlib import Path

import pandas as pd
from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def create_sample_excel_bytes() -> bytes:
    df = pd.DataFrame(
        {
            "S_N": [1, 2],
            "TRUCK_NO": ["T1", "T2"],
            "PRODUCT": ["P1", "P2"],
            "TRUCK_TYPE": ["TypeA", "TypeB"],
            "DRIVER_NAME": ["Alice", "Bob"],
            "DESTINATION_1": ["LocA", "LocB"],
            "DESTINATION_2": ["LocC", "LocD"],
        }
    )
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Sheet2", index=False, header=False, startrow=3)
    buffer.seek(0)
    return buffer.read()


def test_process_endpoint_returns_excel(tmp_path: Path) -> None:
    payload = {
        "output_name": "test_output.xlsx",
    }
    files = {
        "file": ("sample.xlsx", create_sample_excel_bytes(), "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"),
    }
    response = client.post("/process", data=payload, files=files)

    assert response.status_code == 200
    assert response.headers["content-disposition"] == "attachment; filename=test_output.xlsx"

    output_path = tmp_path / "downloaded.xlsx"
    output_path.write_bytes(response.content)

    df = pd.read_excel(output_path, sheet_name="Unified_Tracking_Master")
    assert len(df) == 2
    assert "DRIVER_PHONE_NO" in df.columns
    assert df.loc[0, "TRUCK_NO"] == "T1"
