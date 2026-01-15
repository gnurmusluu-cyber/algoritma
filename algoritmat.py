import streamlit as st
import time

# Sayfa Konfigürasyonu
st.set_page_config(page_title="Algorit-Mat v2.0", page_icon="💎", layout="wide")

# PROFESYONEL CSS: Glassmorphism ve Cyber-Ice Teması
st.markdown("""
    <style>
    /* Arka Plan */
    .stApp {
        background: radial-gradient(circle, #0a192f 0%, #020c1b 100%);
        color: #e6f1ff;
    }
    
    /* Kart Yapısı (Glassmorphism) */
    .main-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 30px;
        border: 1px solid rgba(0, 242, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    /* Başlık ve Metin Renkleri */
    h1, h2, h3 { color: #00f2ff !important; font-family: 'Segoe UI', sans-serif; }
    
    /* Buton Tasarımı */
    .stButton>button {
        background: linear-gradient(90deg, #00f2ff, #0066ff);
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 50px;
        font-weight: 600;
        transition: 0.3s all ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# Üst Başlık ve Tanıtım
st.markdown('<div class="main-card">', unsafe_allow_html=True)
col_title, col_logo = st.columns([4, 1])
with col_title:
    st.title("💎 Algorit-Mat: Master Edition")
    st.markdown("*Matematiksel Zeka, Algoritmik Güçle Buluşuyor.*")
with col_logo:
    st.markdown("### 📐+🐍")
st.markdown('</div>', unsafe_allow_html=True)

st.write("") # Boşluk

# Modern Sekmeli Navigasyon
tab1, tab2, tab3, tab4 = st.tabs(["⚡ Laboratuvar", "📈 Analiz", "🤝 Ekibimiz", "🎨 Tasarım Notları"])

with tab1:
    st.subheader("🛠️ Algoritma Laboratuvarı")
    st.info("Deneyimli öğretmenlerimizin rehberliğinde hazırlanan modülleri keşfedin.")
    
    with st.expander("📌 Modül: Üçgen Eşitsizliği Denetleyicisi", expanded=True):
        c1, c2, c3 = st.columns(3)
        a = c1.number_input("Kenar A", min_value=1, value=7)
        b = c2.number_input("Kenar B", min_value=1, value=10)
        c = c3.number_input("Kenar C", min_value=1, value=5)
        
        if st.button("Sistemi Çalıştır"):
            with st.status("Veriler işleniyor...", expanded=True) as status:
                st.write("Matematiksel kural denetleniyor...")
                time.sleep(0.5)
                is_valid = (abs(a - b) < c < (a + b)) and (abs(a - c) < b < (a + c)) and (abs(b - c) < a < (b + a))
                status.update(label="Analiz Tamamlandı!", state="complete")
            
            if is_valid:
                st.balloons()
                st.success(f"🎨 **Başarılı!** Bu değerler mükemmel bir üçgen oluşturur.")
            else:
                st.error("⚠️ **Hata!** Girdiğiniz değerler üçgen eşitsizliği kuralını bozuyor.")

with tab2:
    st.subheader("📊 Geri Bildirim ve Saha Verileri")
    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.metric(label="Öğrenci Memnuniyeti", value="%88", delta="↑ %12")
    with col_v2:
        st.metric(label="Kalıcı Öğrenme Oranı", value="%94", delta="↑ %15")
    
    st.markdown("> 'Bu uygulama sayesinde formüller sadece birer sayı olmaktan çıkıp, kontrol edebildiğim birer araca dönüştü.' [cite: 186]")

with tab3:
    st.subheader("👥 Proje Yürütücüleri")
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.write("**Bilişim Teknolojileri Öğretmeni**")
        st.caption("Sistem Mimarisi & Python Geliştirme")
    with col_t2:
        st.write("**İlköğretim Matematik Öğretmeni**")
        st.caption("Pedagojik Tasarım & Müfredat Uyumu")

with tab4:
    st.subheader("🖼️ Görsel Standartlar")
    st.write("Uygulama tasarlanırken YetGen bonus kaynaklarından faydalanılmıştır: [cite: 133, 140]")
    st.markdown("- **İllüstrasyonlar:** Storyset ")
    st.markdown("- **İkonlar:** Flaticon [cite: 143]")
    st.markdown("- **AI Sunum:** Gamma.app [cite: 147]")
