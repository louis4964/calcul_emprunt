# Simulateur de Crédit Immobilier - Interface Tkinter

## Description
Ce logiciel a été conçu pour permettre aux particuliers d’estimer leur capacité d’achat immobilier à travers deux approches :
1. En tenant compte d’un apport à côté du prêt.
2. En intégrant l’apport dans le montant du bien immobilier.

L’application offre une interface conviviale avec visualisation des résultats sous forme de tableaux.

## Fonctionnalités
1. **Simulation 1 – Apport à côté du prêt** : Calcule la valeur maximale du bien immobilier selon les revenus, le taux d’emprunt, la durée du crédit et un apport éventuel.
2. **Simulation 2 – Apport inclus dans le bien** : Intègre davantage de paramètres comme le type de bien (ancien/neuf), taux d’assurance, marge de sécurité, etc.
3. **Affichage clair** : Présentation des frais de notaire, mensualités, capital emprunté, budget total, etc.
4. **Interface utilisateur** : Interface graphique réalisée avec Tkinter pour une utilisation simple et rapide.

## Utilisation
- Remplissez les champs nécessaires dans les deux panneaux de calcul :
  - Salaire mensuel
  - Taux du crédit
  - Durée
  - Apport
  - Type de bien, assurance, frais de dossier (selon simulation)
- Cliquez sur **Lancer** pour obtenir les résultats de chaque simulation.
- Cliquez sur **Quitter** pour fermer l'application.

## Structure
- `simulateur_immobilier.py` : Fichier principal contenant l’interface Tkinter et les appels aux fonctions de calcul.
- `valeur_maison_emprunt_2.py` : Module avec les fonctions :
  1. `calcul_apport_a_cote_pret` – Simulation 1
  2. `calcul_apport_immobilier` – Simulation 2
- `test_logiciel.py` : Fichier de test unitaire (utilise `pytest`).
- `README.md` : Documentation du projet.
- `requirements.txt` *(optionnel)* : Dépendances Python.

## Contributions 
Les suggestions, améliorations ou corrections sont les bienvenues.
Merci de soumettre une pull request ou d’ouvrir une issue.

## Licence 
Projet sous licence MIT — usage personnel ou éducatif autorisé.

## Auteur 
Louis Thomas