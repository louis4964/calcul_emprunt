import tkinter as tk
from valeur_maison_emprunt_2 import calcul_apport_a_cote_pret,calcul_apport_immobilier

root = tk.Tk()
root.title("Calcul crédit immobilier")

result_frame_1 = tk.Frame(root)
result_frame_1.grid(row=13, column=0, columnspan=2, pady=10)

result_frame_2 = tk.Frame(root)
result_frame_2.grid(row=13, column=4, columnspan=2, pady=10)


tk.Label(root, text="Calcul crédit immobilier - Particulier", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Salaire net mensuel").grid(row=1, column=0, sticky="w", padx=5, pady=5)
S1 = tk.Entry(root)
S1.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Taux du crédit immobilier").grid(row=2, column=0, sticky="w", padx=5, pady=5)
T1 = tk.Entry(root)
T1.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Durée du crédit (années)").grid(row=3, column=0, sticky="w", padx=5, pady=5)
n1 = tk.Entry(root)
n1.grid(row=3, column=1, padx=5, pady=5)

tk.Label(root, text="Montant de l'apport (0 si aucun)").grid(row=4, column=0, sticky="w", padx=5, pady=5)
A1 = tk.Entry(root)
A1.grid(row=4, column=1, padx=5, pady=5)

def lancer_calcul():
    for widget in result_frame_1.winfo_children():
        widget.destroy()  # clear previous results
    try:
        salaire = float(S1.get())
        taux = float(T1.get())
        duree = float(n1.get())
        apport = float(A1.get())
        interets, maison_valeur, frais_notaire, capital = calcul_apport_a_cote_pret(salaire, taux, duree, apport)

        headers = ["Bilan", "Valeur"]
        stats = [
            ("Intérêts bancaire", round(interets, 2)),
            ("Crédit et montant de la maison", round(maison_valeur, 2)),
            (f"Capital à disposition sur {duree} années.", round(capital, 2)),
            ("Frais notaire", round(frais_notaire, 2))
        ]

        for i, header in enumerate(headers):
            tk.Label(result_frame_1, text=header, font=("Arial", 10, "bold")).grid(row=0, column=i, padx=5, pady=5)

        for i, (label, value) in enumerate(stats, start=1):
            tk.Label(result_frame_1, text=label).grid(row=i, column=0, padx=5, pady=5)
            tk.Label(result_frame_1, text=value).grid(row=i, column=1, padx=5, pady=5)
    except ValueError:
        print("Merci d'entrer des nombres valides.")

button = tk.Button(root, text="Lancer", command=lancer_calcul)
button.grid(row=5, column=0, padx=10, pady=10)


################################################################################################################################################"
# "
tk.Label(root, text="Calcul crédit immobilier - Professionnel", font=("Arial", 14, "bold")).grid(row=0, column=4, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Salaire net mensuel ").grid(row=1, column=4, sticky="w", padx=5, pady=5)
S2 = tk.Entry(root)
S2.grid(row=1, column=5, padx=5, pady=5)

tk.Label(root, text="Taux du crédit immobilier (ex : 0.04 pour 4 %)").grid(row=2, column=4, sticky="w", padx=5, pady=5)
T2 = tk.Entry(root)
T2.grid(row=2, column=5, padx=5, pady=5)

tk.Label(root, text="Durée du crédit (années)").grid(row=3, column=4, sticky="w", padx=5, pady=5)
n2 = tk.Entry(root)
n2.grid(row=3, column=5, padx=5, pady=5)

tk.Label(root, text="Montant de l'apport (0 si aucun)").grid(row=4, column=4, sticky="w", padx=5, pady=5)
A2 = tk.Entry(root)
A2.grid(row=4, column=5, padx=5, pady=5)

tk.Label(root, text="Type de bien ( ancien ou neuf )").grid(row=5, column=4, sticky="w", padx=5, pady=5)
Bien = tk.Entry(root)
Bien.grid(row=5, column=5, padx=5, pady=5)

tk.Label(root, text="Taux d'assurance (par défaut  0.3 %)").grid(row=6, column=4, sticky="w", padx=5, pady=5)
taux = tk.Entry(root)
taux.grid(row=6, column=5, padx=5, pady=5)

tk.Label(root, text="marge de securite : pourcentage de prudence (par défaut 0.9)").grid(row=7, column=4, sticky="w", padx=5, pady=5)
marge = tk.Entry(root)
marge.grid(row=7, column=5, padx=5, pady=5)

tk.Label(root, text="Frais de dossier (par défaut 1000 €) ").grid(row=8, column=4, sticky="w", padx=5, pady=5)
frais= tk.Entry(root)
frais.grid(row=8, column=5, padx=5, pady=5)

def lancer_calcul_2():
    for widget in result_frame_2.winfo_children():
        widget.destroy()  # clear previous results
    try:
        salaire_mensuel = float(S2.get())
        taux_annuel = float(T2.get())
        duree_annees = float(n2.get()) if n2.get() else 0
        apport = float(A2.get()) if A2.get() else 0
        type_bien = Bien.get() if Bien.get() else "ancien"
        taux_assurance = float(taux.get()) if taux.get() else 0.003
        marge_securite = float(marge.get()) if marge.get() else 0.9
        frais_dossier = float(frais.get()) if frais.get() else 1000

        #mensualite_max, capital_emprunt, prix_bien_ht_frais, frais_notaire, budget_total = calcul_apport_immobilier(
        #    salaire_mensuel, taux_annuel, duree_annees, apport, type_bien, taux_assurance, marge_securite, frais_dossier)
        
        taux_notaire = 0.075 if type_bien == "ancien" else 0.03
        capital_emprunt = ( salaire_mensuel*0.3*12*duree_annees ) / ( 1 + taux_annuel + taux_notaire)
        mensualite_max = capital_emprunt/(duree_annees*12)
        frais_notaire = taux_notaire*capital_emprunt
        budget_total = capital_emprunt + apport + frais_notaire
        prix_bien_ht_frais = capital_emprunt

        headers = ["Bilan", "Valeur"]
        stats = [
            ("Mensualite maximale", round(mensualite_max, 2)),
            ("Prix estimé du bien (hors frais notaire) ", round(prix_bien_ht_frais, 2)),
            ("Frais notaire éstimés", round(frais_notaire, 2)),
            ("Budget immobilier disponible (apport inclus) - notaire + prix estimé du bien", round(budget_total, 2)),
            ("Budget total disponible",round(duree_annees*12*salaire_mensuel*0.3,2)),
            ("Intérêts bancaire" , round((duree_annees*salaire_mensuel*12*0.3 - capital_emprunt) ))
        ]

        for i, header in enumerate(headers):
            tk.Label(result_frame_2, text=header, font=("Arial", 10, "bold")).grid(row=0, column=i, padx=5, pady=5)

        for i, (label, value) in enumerate(stats, start=1):
            tk.Label(result_frame_2, text=label).grid(row=i, column=0, padx=5, pady=5)
            tk.Label(result_frame_2, text=value).grid(row=i, column=1, padx=5, pady=5)
    except ValueError:
        print("Merci d'entrer des nombres valides.")

button = tk.Button(root, text="Lancer", command=lancer_calcul_2)
button.grid(row=9, column=4, padx=10, pady=10)


###########################################################################################################################################

button_quit = tk.Button(root, text="Quitter", command=root.destroy)
button_quit.grid(row=12, column=3, padx=10, pady=10)

root.mainloop()


# Faire logiciel pour emprunt ( avec pourcentage salaire, etc)