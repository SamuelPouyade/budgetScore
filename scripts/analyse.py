import pandas as pd
from parser import lire_transaction

def total_par_categorie(df):
    depenses = df[df["Transaction_Type"] == "Debit"]
    resume = depenses.groupby("Category")["Transaction_Amount"].sum().sort_values(ascending=False)

    return resume


def total_entrees(df):
    entrees = df[df["Transaction_Type"] == "Credit"]
    total = entrees["Transaction_Amount"].sum()
    return total

def bilan_mensuel(df):
    df = df.copy()

    # Extraire le mois sous forme 'AAAA-MM'
    df["Mois"] = df["Transaction_Date"].dt.to_period("M").astype(str)

    df["Montant_Reel"] = df.apply(
        lambda row: -row["Transaction_Amount"] if row["Transaction_Type"] == "Debit" else row["Transaction_Amount"],
        axis=1
    )

    bilan = df.groupby("Mois")["Montant_Reel"].sum().sort_index()

    return bilan

if __name__ == "__main__":
    df = lire_transaction("data/transaction_banque.csv")

    if df is not None:
        print("💸 Total des dépenses par catégorie :\n")
        print(total_par_categorie(df),"\n")

        revenu_total = total_entrees(df)
        print(f"✅ Total des entrées (revenus) : {revenu_total:.2f} $\n")

        print("📊 Bilan mensuel :\n")
        print(bilan_mensuel(df),"\n")