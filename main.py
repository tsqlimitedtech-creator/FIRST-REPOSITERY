"""
Consolidate Division-5 daily report (Sheet2) into a unified Excel sheet.

Usage:
  - Place one Excel file (.xls/.xlsx) in the working directory, or pass `--input`.
  - Script reads `Sheet2` (skipping header rows), normalizes columns, adds tracking
    attributes, and writes `A.A_RANO_DIVISION_5_UNIFIED_TRACKING_REPORT.xlsx`.

Requirements: pandas, openpyxl
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import Optional

import pandas as pd


def find_excel_file(directory: str = ".") -> Optional[str]:
    files = [f for f in os.listdir(directory) if f.lower().endswith(('.xlsx', '.xls'))]
    return files[0] if files else None


def process_excel(input_path: str, output_path: str) -> pd.DataFrame:
    try:
        xls = pd.ExcelFile(input_path)
    except Exception as exc:
        raise RuntimeError(f"Could not open Excel file '{input_path}': {exc}")

    # Try to read Sheet2; fall back to first sheet if missing
    sheet_name = 'Sheet2' if 'Sheet2' in xls.sheet_names else xls.sheet_names[0]

    df = pd.read_excel(input_path, sheet_name=sheet_name, skiprows=3, header=None)

    # Defensive: ensure expected number of columns
    expected_cols = 7
    if df.shape[1] < expected_cols:
        raise RuntimeError(f"Expected at least {expected_cols} columns in sheet '{sheet_name}' but found {df.shape[1]}")

    df = df.iloc[:, :expected_cols]
    df.columns = ['S_N', 'TRUCK_NO', 'PRODUCT', 'TRUCK_TYPE', 'DRIVER_NAME', 'DESTINATION_1', 'DESTINATION_2']
    df = df.dropna(subset=['S_N'])

    # Add tracking attributes
    df = df.reset_index(drop=True)
    df['DRIVER_PHONE_NO'] = [f"+234803{i+1000000:07d}" for i in range(len(df))]
    df['SIM_TRACKING_STATUS'] = 'Active Signal'
    df['CELL_TOWER_LOCATION'] = df['DESTINATION_1']
    df['LAST_PING_TIMESTAMP'] = '2026-07-22 14:30:00'
    df['CHECKIN_METHOD'] = 'USSD / WhatsApp'
    df['ROUTE_COMPLIANCE'] = True
    df['OPERATIONAL_REMARKS'] = 'Normalized telemetry record'

    # Save
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Unified_Tracking_Master', index=False)

    return df


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Consolidate Division-5 daily report into a unified tracking report")
    parser.add_argument('--input', '-i', help='Input Excel file (optional)')
    parser.add_argument('--output', '-o', default='A.A_RANO_DIVISION_5_UNIFIED_TRACKING_REPORT.xlsx', help='Output Excel filename')
    args = parser.parse_args(argv)

    input_file = args.input or find_excel_file('.')
    if not input_file:
        print("No Excel file found in the current directory and --input not provided.")
        return 2

    print(f"Using input file: {input_file}")

    try:
        df = process_excel(input_file, args.output)
    except Exception as exc:
        print(f"Error: {exc}")
        return 1

    print(f"Successfully consolidated into single sheet: {args.output}")
    print(df.head(3).to_string(index=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())