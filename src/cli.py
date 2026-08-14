from __future__ import annotations

import argparse
from pathlib import Path
import yaml
from .pipeline import run_pipeline


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the synthetic multi-tenant data quality pipeline")
    parser.add_argument("--input", default="samples")
    parser.add_argument("--output", default="output")
    parser.add_argument("--config", default="config/pipeline.yaml")
    args = parser.parse_args()

    config = yaml.safe_load(Path(args.config).read_text(encoding="utf-8")) or {}
    results = run_pipeline(Path(args.input), Path(args.output), config)
    for code, rec in results.items():
        print(f"{code}: source={rec.source_rows} filtered={rec.filtered_rows} eligible={rec.eligible_rows} exported={rec.exported_rows} PASS={rec.passed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
