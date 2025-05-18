import pandas as pd
import matplotlib.pyplot as plt
from parser import lire_transaction
from analyse import total_par_categorie, bilan_mensuel

def afficher_pie_depenses(df):
    depenses = total_par_categorie(df)
    depenses.plot.pie(autopct='%1.1f%%', startangle=90, figsize=(8, 8))
    plt.title("Répartition des dépenses par catégorie")
    plt.ylabel("")  # Pour enlever "Transaction_Amount"
    plt.tight_layout()
    plt.show()

def afficher_bilan_mensuel(df):
    bilan = bilan_mensuel(df)
    bilan.plot(kind='bar', figsize=(10, 5), color='skyblue')
    plt.title("Bilan mensuel (revenus - dépenses)")
    plt.xlabel("Mois")
    plt.ylabel("Solde ($)")
    plt.xticks(rotation=45)
    plt.axhline(0, color='red', linestyle='--')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = lire_transaction("data/transaction_banque.csv")
    
    if df is not None:
        afficher_pie_depenses(df)
        afficher_bilan_mensuel(df)