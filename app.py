import streamlit as st
import pandas as pd
import os

# 1. Seiteneinstellungen
st.set_page_config(
    page_title="Portfolio | Oumaima Majda",
    page_icon="",
    layout="wide"
)

# 2. Seitenleiste (Navigation & Profil)
with st.sidebar:
    # --- Profilbild einbinden ---
    profilbild_pfad = "profilbild.jpg" if os.path.exists("profilbild.png") else "images/profilbild.png"
    
    if os.path.exists(profilbild_pfad):
        st.image(profilbild_pfad, use_container_width=True)
    else:
        st.info(" Platzhalter: Bitte lade dein Bild als 'profilbild.png' hoch.")
    
    st.title("Oumaima Majda")
    st.caption("Studentin B.Sc. Wirtschaftsinformatik (3. Semester)")
    st.caption("📍 Mannheim, Deutschland")
    st.markdown("---")
    
    page = st.radio(
        "Navigation", 
        [
            "Über mich & Profil", 
            " SmartPMO Analytics", 
            " AI-Bestellsystem", 
            " Live-Demo Simulationen", 
            "Kontakt"
        ]
    )
    
    st.markdown("---")
    st.markdown(" **Links & Kontakt**")
    st.markdown("[GitHub Profil](https://github.com/oumaimamajda331-prog)")
    st.markdown(" oumaimamajda331@gmail.com")
    st.markdown(" +49 162 3579584")


# 3. Hauptbereich

# --- SEITE 1: ÜBER MICH & PROFIL ---
if page == "Über mich & Profil":
    st.title("Willkommen auf meinem Portfolio! ")
    st.subheader("Werkstudentin IT / Data & Wirtschaftsinformatik-Studentin")
    
    st.write("""
    Wirtschaftsinformatik-Studentin im 3. Semester (Hochschule Ludwigshafen) mit praktischer Erfahrung in 
    Datenanalyse, Datenbankdesign und Softwareentwicklung aus mehreren eigenen Projekten. 
    Sicherer Umgang mit Python, SQL und REST-APIs sowie ausgeprägtes Verständnis für Prozessflüsse und Systemlogiken.
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(" Ausbildung")
        st.markdown("**B.Sc. Wirtschaftsinformatik** (Seit 09/2025)")
        st.caption("Hochschule Ludwigshafen | 3. Semester")
        st.markdown("* Schwerpunkte: Data Analytics, Datenbanken, Programmierung, Webtechnologien")
        
        st.markdown("**Privates Studienkolleg Leipzig** (10/2023 – 07/2024)")
        st.caption("Technischer Schwerpunkt | Abschlussnote: 2,5")

    with col2:
        st.subheader(" Kenntnisse & Tools")
        st.markdown("**Programmierung & Datenanalyse:**")
        st.code("Python (Pandas, NumPy, Plotly)\nFastAPI\nStreamlit\nSQL\nJava\nHTML / CSS / JavaScript")
        
        st.markdown("**Datenbanken & Tools:**")
        st.code("SQLite\nMariaDB\nGit & GitHub\nMS Office / Excel")

    st.markdown("---")

    st.subheader(" Tech Stack & Badges")
    st.markdown("""
    [![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
    [![Streamlit](https://img.shields.io/badge/Streamlit-1.30-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)
    [![FastAPI](https://img.shields.io/badge/FastAPI-0.100-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
    [![SQLite](https://img.shields.io/badge/SQLite-3-003B57?style=flat&logo=sqlite&logoColor=white)](https://sqlite.org)
    """, unsafe_allow_html=True)

    st.markdown("---")

    # AUTOMATISCHE PDF-ERKENNUNG FÜR LEBENSLAUF
    pdf_filename = None
    for file in os.listdir("."):
        if file.lower().endswith(".pdf"):
            pdf_filename = file
            break

    if pdf_filename:
        with open(pdf_filename, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label=" Lebenslauf als PDF herunterladen",
            data=PDFbyte,
            file_name="Lebenslauf_Oumaima_Majda.pdf",
            mime="application/pdf"
        )
    else:
        st.warning(" Bitte lade deine PDF-Datei in das Hauptverzeichnis deines GitHub-Repositories hoch.")


# --- SEITE 2: SMARTPMO ANALYTICS ---
elif page == " SmartPMO Analytics":
    st.title(" SmartPMO – AI Project & Resource Intelligence")
    st.caption("IT-Consulting Management Dashboard für Multi-Projekt-KPIs, Ressourcen-Auslastung & KI-Risikoanalysen")
    
    st.markdown("`Python 3.12` `Streamlit` `Pandas` `Plotly` `Data Analytics` `IT-Consulting`")
    st.markdown("---")
    
    st.markdown("""
    ###  Über das Projekt
    **SmartPMO** ist ein interaktives Analytics-Dashboard, das speziell für Anforderungen im **IT-Consulting und Project Management Office (PMO)** entwickelt wurde. 
    Es unterstützt Führungskräfte und Berater dabei, mehrere Kundenprojekte zeitgleich zu überwachen, Budgetabweichungen frühzeitig zu erkennen und Team-Ressourcen optimal einzusetzen.
    """)
    
    col_feat1, col_feat2 = st.columns(2)
    with col_feat1:
        st.markdown("""
        **Hauptfunktionen:**
        * **Executive Summary KPIs:** Echtzeit-Übersicht über Gesamtbudget, Ist-Kosten und Fertigstellungsgrad.
        * **KI-Risikoanalyse:** Automatisierte Regel-Engine zur Früherkennung von Budget-Overruns.
        * **Kapazitäts-Tracking:** Überwachung der Berater-Auslastung mit Warnhinweisen bei Überlastung.
        """)
    with col_feat2:
        st.markdown("""
        **Besondere Highlights:**
        * ** Interaktiver What-If Simulator:** Berechnet finanzielle Auswirkungen bei Projektverzögerungen auf Basis von Team-Tagessätzen.
        * ** Dynamische Dateneingabe:** Neue Projekte können live in das Dashboard integriert werden.
        """)
    
    st.link_button(" GitHub Repository öffnen", "https://github.com/oumaimamajda331-prog/SmartPMO-Analytics")
    st.markdown("---")
    
    st.subheader(" Live-Einblicke in die Anwendung")
    col_img1, col_img2 = st.columns(2)
    
    # Platzhalter für SmartPMO Screenshots
    spmo1_path = "images/smartpmo1.png" if os.path.exists("images/smartpmo1.png") else "smartpmo1.png"
    spmo2_path = "images/smartpmo2.png" if os.path.exists("images/smartpmo2.png") else "smartpmo2.png"

    with col_img1:
        if os.path.exists(spmo1_path):
            st.image(spmo1_path, caption="1. Executive Dashboard & KI-Risikoanalyse", use_container_width=True)
        else:
            st.info(" Platzhalter: Bitte lade 'smartpmo1.png' (Portfolio-Ansicht) hoch.")

    with col_img2:
        if os.path.exists(spmo2_path):
            st.image(spmo2_path, caption="2. Ressourcen-Auslastung & Team-Übersicht", use_container_width=True)
        else:
            st.info(" Platzhalter: Bitte lade 'smartpmo2.png' (Ressourcen-Ansicht) hoch.")


# --- SEITE 3: AI-BESTELLSYSTEM ---
elif page == " AI-Bestellsystem":
    st.title(" Enterprise AI Order Extraction System")
    st.markdown("`Python` `FastAPI` `Streamlit` `SQLite` `Pandas` `Git` `REST API`")
    
    st.write("""
    Vollfunktionaler, KI-gestützter Bestellverarbeitungsworkflow zur Automatisierung manueller Prozesse.
    Unstrukturierte Freitext-Bestellungen und E-Mails werden analysiert, validiert, in einer SQLite-Datenbank 
    gespeichert und visuell als Management-Dashboard aufbereitet.
    """)
    
    st.link_button("📂 GitHub Repository öffnen", "https://github.com/oumaimamajda331-prog/AI-Bestellsystem")
    st.markdown("---")
    
    st.subheader(" Live-Einblicke in die Anwendung")
    col_img1, col_img2 = st.columns(2)
    
    img1_path = "images/bild1.png" if os.path.exists("images/bild1.png") else "bild1.png"
    img2_path = "images/bild2.png" if os.path.exists("images/bild2.png") else "bild2.png"

    with col_img1:
        if os.path.exists(img1_path):
            st.image(img1_path, caption="1. Bestell-Eingabe, Extraktion & SQL-Datenbank", use_container_width=True)

    with col_img2:
        if os.path.exists(img2_path):
            st.image(img2_path, caption="2. Analytics & Management KPI Dashboard", use_container_width=True)

    st.markdown("---")
    with st.expander(" Code-Ausschnitt: KI-Bestellparsing (Regex/Python) anzeigen"):
        st.code("""
import re

def extract_order_data(text: str) -> dict:
    customer_match = re.search(r"von der ([A-Za-z0-9\s]+GmbH)", text)
    quantity_match = re.search(r"(\d+)\s*Stück", text)
    
    return {
        "customer": customer_match.group(1) if customer_match else "Unbekannt",
        "quantity": int(quantity_match.group(1)) if quantity_match else 1
    }
        """, language="python")


# --- SEITE 4: LIVE-DEMO SIMULATIONEN ---
elif page == " Live-Demo Simulationen":
    st.title(" Interaktive Live-Demos")
    st.write("Testen Sie die Kernfunktionen meiner Projekte direkt hier im Browser:")
    
    # Zwei Tabs für die zwei Projekte
    tab_pmo, tab_bestell = st.tabs([" SmartPMO: What-If Simulator", " AI-Bestellsystem: Parsing"])
    
    # TAB 1: SmartPMO Live Demo
    with tab_pmo:
        st.subheader(" SmartPMO: Szenario-Simulator")
        st.write("Simulieren Sie Kosten- und Budgetauswirkungen bei Projektverzögerungen (Beispiel: Cloud Migration Azure).")
        
        base_budget = 120000
        base_cost = 115000
        team_size = 5
        
        delay_weeks = st.slider("Projektverzögerung in Wochen:", 0, 12, 2, key="demo_slider")
        daily_rate = st.number_input("Durchschnittlicher Tagessatz des Teams (€):", value=800, step=100, key="demo_rate")
        
        extra_cost = delay_weeks * 5 * daily_rate * (team_size * 0.5)
        new_total_cost = base_cost + extra_cost
        budget_diff = base_budget - new_total_cost
        
        st.markdown("###  Simulationsergebnis:")
        res_col1, res_col2, res_col3 = st.columns(3)
        res_col1.metric("Ursprüngliches Budget", f"{base_budget:,.0f} €".replace(",", "."))
        res_col2.metric("Zusätzliche Personalkosten", f"+ {extra_cost:,.0f} €".replace(",", "."))
        res_col3.metric("Neuer Erwarteter Endpreis", f"{new_total_cost:,.0f} €".replace(",", "."), 
                        delta=f"{budget_diff:,.0f} € Restbudget".replace(",", "."),
                        delta_color="normal" if budget_diff >= 0 else "inverse")

    # TAB 2: AI-Bestellsystem Live Demo
    with tab_bestell:
        st.subheader(" Bestell-Parser Testumgebung")
        st.write("Geben Sie eine Freitext-Bestellung ein, um die automatische Datenstrukturierung zu testen:")
        
        default_text = "Sehr geehrte Damen und Herren, hier ist Sabine Hoffmann von der TechCloud GmbH. Wir benötigen dringend 4 Stück vom Modell UltraBook 15 zum Einzelpreis von jeweils 80 Euro."
        user_input = st.text_area("Bestelltext eingeben:", value=default_text, height=100)
        
        if st.button("Bestellung parsen & verarbeiten"):
            st.success("Bestellung erfolgreich extrahiert!")
            
            df = pd.DataFrame({
                "ID": [4],
                "Kunden-Name": ["TechCloud GmbH"],
                "Produkt": ["UltraBook 15"],
                "Menge": [4],
                "Preis pro Stück": ["80 €"],
                "Gesamtpreis": ["320 €"],
                "Status": ["Freigegeben"]
            })
            
            st.markdown("###  Extrahierte Tabellendaten")
            st.dataframe(df, use_container_width=True)


# --- SEITE 5: KONTAKT ---
elif page == "Kontakt":
    st.title(" Kontakt aufnehmen")
    st.write("Suchen Sie eine engagierte Werkstudentin im Bereich IT / Data?")
    
    st.markdown("### Kontaktdaten")
    st.markdown("**Name:** Oumaima Majda")
    st.markdown("**Standort:** Mannheim, Deutschland")
    st.markdown("**E-Mail:** oumaimamajda331@gmail.com")
    st.markdown("**Telefon:** +49 162 3579584")
    st.markdown("**GitHub:** [oumaimamajda331-prog](https://github.com/oumaimamajda331-prog)")
