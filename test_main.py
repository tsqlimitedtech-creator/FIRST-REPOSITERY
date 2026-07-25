import tempfile
from pathlib import Path

import pandas as pd

from main import process_excel


def create_sample_excel(path: Path) -> None:
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
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Sheet2", index=False, header=False, startrow=3)


def test_process_excel_creates_unified_report(tmp_path: Path) -> None:
    input_path = tmp_path / "input.xlsx"
    output_path = tmp_path / "output.xlsx"

    create_sample_excel(input_path)
    result_df = process_excel(str(input_path), str(output_path))

    assert output_path.exists()
    assert len(result_df) == 2
    assert "DRIVER_PHONE_NO" in result_df.columns
    assert result_df.loc[0, "TRUCK_NO"] == "T1"
    assert result_df.loc[1, "DRIVER_NAME"] == "Bob"
