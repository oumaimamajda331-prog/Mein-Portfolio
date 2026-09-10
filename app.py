import streamlit as st
import pandas as pd

# 1. Seiteneinstellungen
st.set_page_config(
    page_title="Portfolio | Oumaima Majda",
    page_icon="",
    layout="wide"
)

# 2. Seitenleiste (Navigation & Profil)
with st.sidebar:
    st.title("Oumaima Majda")
    st.caption("Studentin B.Sc. Wirtschaftsinformatik (3. Semester)")
    st.caption("📍 Mannheim, Deutschland")
    st.markdown("---")
    
    page = st.radio(
        "Navigation", 
        ["Über mich & Profil", "AI-Bestellsystem (Projekt)", " Live-Demo Simulation", "Kontakt"]
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
        st.subheader("Ausbildung")
        st.markdown("**B.Sc. Wirtschaftsinformatik** (Seit 09/2025)")
        st.caption("Hochschule Ludwigshafen | 3. Semester")
        st.markdown("* Schwerpunkte: Data Analytics, Datenbanken, Programmierung, Webtechnologien")
        
        st.markdown("**Privates Studienkolleg Leipzig** (10/2023 – 07/2024)")
        st.caption("Technischer Schwerpunkt | Abschlussnote: 2,5")

    with col2:
        st.subheader(" Kenntnisse & Tools")
        st.markdown("**Programmierung & Datenanalyse:**")
        st.code("Python (Pandas, NumPy)\nFastAPI\nStreamlit\nSQL\nJava\nHTML / CSS / JavaScript")
        
        st.markdown("**Datenbanken & Tools:**")
        st.code("SQLite\nMariaDB\nGit & GitHub\nMS Office / Excel")

# --- SEITE 2: AI-BESTELLSYSTEM (PROJEKT MIT BILDERN) ---
elif page == "AI-Bestellsystem (Projekt)":
    st.title(" Enterprise AI Order Extraction System")
    st.markdown("`Python` `FastAPI` `Streamlit` `SQLite` `Pandas` `Git` `REST API`")
    
    st.write("""
    Vollfunktionaler, KI-gestützter Bestellverarbeitungsworkflow zur Automatisierung manueller Prozesse.
    Unstrukturierte Freitext-Bestellungen und E-Mails werden analysiert, validiert, in einer SQLite-Datenbank 
    gespeichert und visuell als Management-Dashboard aufbereitet.
    """)
    
    st.link_button(" GitHub Repository öffnen", "https://github.com/oumaimamajda331-prog/AI-Bestellsystem")
    st.markdown("---")
    
    st.subheader(" Live-Einblicke in die Anwendung")
    
    col_img1, col_img2 = st.columns(2)
    
    with col_img1:
        st.image("images/bild1.png", caption="1. Bestell-Eingabe, Extraktion & SQL-Datenbank", use_container_width=True)

    with col_img2:
        st.image("images/bild2.png", caption="2. Analytics & Management KPI Dashboard", use_container_width=True)

# --- SEITE 3: LIVE-DEMO SIMULATION ---
elif page == " Live-Demo Simulation":
    st.title(" Interaktive Live-Demo")
    st.subheader("Testumgebung für das AI-Bestellsystem")
    st.write("Geben Sie eine Beispielbestellung ein, um die Datenstrukturierung live im Portfolio zu testen:")
    
    default_text = "Sehr geehrte Damen und Herren, hier ist Sabine Hoffmann von der TechCloud GmbH. Wir benötigen dringend 4 Stück vom Modell UltraBook 15 zum Einzelpreis von jeweils 80 Euro."
    user_input = st.text_area("Bestelltext (Freitext eingeben):", value=default_text, height=100)
    
    if st.button("Bestellung parsen & verarbeiten"):
        st.success("Bestellung erfolgreich extrahiert und für die TechCloud GmbH freigegeben!")
        
        # Simulierter Auswertungs-DataFrame passend zu deinem Screenshot
        parsed_data = {
            "ID": [4],
            "Kunden-Name": ["TechCloud GmbH"],
            "Produkt": ["UltraBook 15"],
            "Menge": [4],
            "Preis pro Stück": ["80 €"],
            "Gesamtpreis": ["320 €"],
            "Status": ["Freigegeben"]
        }
        df = pd.DataFrame(parsed_data)
        
        st.markdown("###  Extrahierte Tabellendaten (Pandas Output)")
        st.dataframe(df, use_container_width=True)
        
        st.markdown("###  Datenbank-Status (SQLite)")
        st.json({
            "status": 200,
            "database": "SQLite",
            "table": "orders",
            "kunden_name": "TechCloud GmbH",
            "records_inserted": 1
        })

# --- SEITE 4: KONTAKT ---
elif page == "Kontakt":
    st.title(" Kontakt aufnehmen")
    st.write("Suchen Sie eine engagierte Werkstudentin im Bereich IT / Data?")
    
    st.markdown("### Kontaktdaten")
    st.markdown("**Name:** Oumaima Majda")
    st.markdown("**Standort:** Mannheim, Deutschland")
    st.markdown("**E-Mail:** oumaimamajda331@gmail.com")
    st.markdown("**Telefon:** +49 162 3579584")
    st.markdown("**GitHub:** [oumaimamajda331-prog](https://github.com/oumaimamajda331-prog)")