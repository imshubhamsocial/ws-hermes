#!/usr/bin/env bash
# Automated Model Benchmark Suite: Google Gemma 4 Exact
set -euo pipefail
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "=========================================================="
echo "Testing Model: Google Gemma 4 Exact (Temp: 0.2, Top_P: 0.95)"
echo "=========================================================="
python3 "${DIR}/benchmark_speed.py" 200 0.2 0.95
echo "BENCHMARK COMPLETED."
