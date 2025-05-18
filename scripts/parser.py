import pandas as pd

def lire_transaction(fichier):
    try:
        df = pd.read_csv(fichier)

        colonnes = [
            "Transaction_Date",
            "Transaction_Amount",
            "Transaction_Type",
            "Category",
            "Merchant_Name",
            "Payment_Method",
            "Transaction_Status"
        ]

        df = df[colonnes]

        df["Transaction_Date"] = pd.to_datetime(df["Transaction_Date"])
        df["Transaction_Amount"] = df["Transaction_Amount"].astype(float)
        df = df[df["Transaction_Status"] == "Success"]

        return df

    except Exception as e:
        print(f"Erreur de lecture : {e}")
        return None


if __name__ == "__main__":
    chemin = "data/transaction_banque.csv"
    df = lire_transaction(chemin)

    if df is not None:
        print(df.head())