# README

## Run
1. pip install -r requirements.txt
2. python -m src.extract_case --case "inputs/HSBC PB Case Challenge 2026 Qualifier Round Case.pdf"
3. python -m src.backtest --config config/config.yaml
4. python -m src.scenarios --config config/config.yaml
5. python -m src.robustness --config config/config.yaml
6. python -m src.report --config config/config.yaml

All outputs are generated under ./outputs (tables + charts + markdown slide content).
