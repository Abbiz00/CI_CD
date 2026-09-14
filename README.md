.
├── .github/workflows/
│   └── python_ci_cd.yml      # GitHub Actions workflow
├── src/
│   └── example.py             # Källkod
├── tests/
│   └── unit/
│       └── test_example.py    # Enhetstester
├── pytest.ini                 # pytest-konfiguration
├── requirements.txt           # Python-beroenden
└── README.md                  # Du är här



Funktioner i src/example.py
square(n) - Returnerar kvadraten av n
add(a, b) - Returnerar summan av a och b
multiply(a, b) - Returnerar produkten av a och b


Installation
git clone https://github.com/Abbiz00/CI_CD
cd CI_CD

pip install -r requirements.txt

Enhetstest
pytest -m unit

Linting
flake8 src tests