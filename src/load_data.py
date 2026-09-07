"""Étape 1 : chargement des données CRM Lumina & Co."""

from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent.parent / "Lumina & Co - CRM"


def load_data() -> dict[str, pd.DataFrame]:
    files = {
        "customers": "customers.csv",
        "transactions": "transactions.csv",
        "touchpoints": "touchpoints.csv",
        "campaigns": "campaigns.csv",
    }

    data = {}
    for name, filename in files.items():
        path = DATA_DIR / filename
        if not path.exists():
            raise FileNotFoundError(f"Fichier introuvable : {path}")
        data[name] = pd.read_csv(path)

    return data


if __name__ == "__main__":
    data = load_data()
    for name, df in data.items():
        print(f"{name}: {df.shape[0]} lignes, {df.shape[1]} colonnes")
        print(df.dtypes)
        print()
