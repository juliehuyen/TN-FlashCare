# This page is the home page of your front application

# Import Streamlit packages
import streamlit as st

# Page Title
st.title("🚑 FlashCare - Optimisation de la prise en charge aux urgences")

# Introduction
st.markdown("""
Bienvenue dans le projet **FlashCare**, développé dans le cadre du cours de développement d'application à l'Université Paris Dauphine.

Ce projet vise à concevoir une **application innovante** pour améliorer la gestion des patients dans les services **d’urgence hospitalière**, en répondant à des problématiques concrètes rencontrées sur le terrain.

---

## 🚀 Technologies Utilisées

1. **Streamlit** : Pour construire une interface web simple, rapide et interactive.
2. **Cohere** : Pour exploiter la puissance du NLP (traitement du langage naturel) afin de suggérer des diagnostics à partir de symptômes décrits.
3. **FastAPI** : Pour créer un backend performant et évolutif, capable de traiter et d’exposer les données nécessaires à l’application.

---

## 🎯 Objectif du Projet

Créer une application web qui :
- **Réduit le stress des patients** en leur donnant des informations sur leur parcours aux urgences.
- **Facilite le tri médical** grâce à une suggestion automatisée de diagnostics basée sur les symptômes.
- **Améliore la coordination entre les personnels administratifs et médicaux**.
- **Fluidifie le parcours de soin**, de l'arrivée à la sortie des urgences.

---

## 🧭 Déroulé du Projet

1. **Phase 1 : Analyse & Design**
   - Étude des irritants des patients et personnels soignants.
   - Définition des parcours utilisateurs et du processus métier.

2. **Phase 2 : Développement**
   - Interface avec **Streamlit**
   - Backend en **FastAPI**
   - Intégration NLP avec **Cohere**

3. **Phase 3 : Déploiement**
   - Mise en ligne sur une plateforme (ex : Streamlit Cloud, Render, Heroku…)
   - Tests utilisateurs et ajustements

---

## 🛠 Fonctionnalités Clés à venir

- Simulation de tri d’urgence en fonction des symptômes
- Interface patient avec suivi des étapes
- Espace personnel administratif simplifié
- Tableau de bord médical avec centralisation des données

---

## 📝 Évaluation du Projet

Le projet sera évalué selon les critères suivants :
- Pertinence de la solution proposée
- Intégration des technologies demandées
- Qualité de l’expérience utilisateur (UX/UI)
- Robustesse de l’architecture logicielle

Bonne chance à toutes les équipes ! 💪

---
""")
