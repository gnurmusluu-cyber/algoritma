import streamlit as st
import time

# Sayfa Yapılandırması ve "Siber-Buz" Teması
st.set_page_config(page_title="Algorit-Mat Prototip", page_icon="📐", layout="wide")

# CSS ile Görsel Standartlar
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00d4ff; }
    .stButton>button { background-color: #00d4ff; color: #000; border-radius: 10px; font-weight: bold; }
    .stSuccess { background-color: #1e3a2f; color: #00ff00; }
    </style>
    """, unsafe_allow_status=True)

# Yan Menü - Navigasyon
with st.sidebar:
    st.title("🚀 Algorit-Mat")
    page = st.radio("Menü", ["🏠 Ana Sayfa", "📐 Üçgen Modülü", "📊 Geri Bildirimler", "🏆 Liderlik Tablosu"])
    st.info("Nitelikli Eğitim İçin Matematik & Kodlama [cite: 22]")

if page == "🏠 Ana Sayfa":
    st.header("Algorit-Mat'a Hoş Geldin Genç Yazılımcı!")
    st.write("Matematiği sadece çözme, onu algoritmalarla inşa et! [cite: 168]")
    st.image("https://img.freepik.com/free-vector/coding-concept-illustration_114360-1209.jpg", width=500)

elif page == "📐 Üçgen Modülü":
    st.header("Üçgen Eşitsizliği Laboratuvarı")
    st.write("Kural: Bir üçgen oluşturmak için kenarlar şu şartı sağlamalıdır: $|a - b| < c < a + b$")
    
    col1, col2, col3 = st.columns(3)
    with col1: a = st.number_input("Kenar a", min_value=1, value=5)
    with col2: b = st.number_input("Kenar b", min_value=1, value=5)
    with col3: c = st.number_input("Kenar c", min_value=1, value=5)

    if st.button("Algoritmayı Test Et"):
        with st.spinner("Mantık kontrol ediliyor..."):
            time.sleep(1)
            # Kritik Özellik: Mantıksal Kontrol [cite: 176]
            if (abs(a - b) < c < (a + b)) and (abs(a - c) < b < (a + c)) and (abs(b - c) < a < (b + a)):
                st.success(f"✅ Başarılı! {a}, {b}, {c} değerleri ile bir üçgen çizilebilir.")
                st.code(f"IF (abs({a}-{b}) < {c} < ({a}+{b})): PRINT 'Üçgen'")
            else:
                st.error("❌ Hata! Matematiksel kurallara göre bu bir üçgen oluşturamaz.")
                st.warning("İpucu: Bir kenar uzunluğu, diğer ikisinin farkından büyük olmalıdır.")

elif page == "📊 Geri Bildirimler":
    st.header("Süreç Geri Bildirimleri [cite: 184]")
    st.write("Müşteri görüşmelerinden elde edilen veriler[cite: 185]:")
    st.bar_chart({"Olumlu": 85, "Geliştirilmeli": 15})
    st.blockquote("'Matematiği kodlayarak öğrenmek çok daha kalıcıymış!' - Öğrenci [cite: 186]")

elif page == "🏆 Liderlik Tablosu":
    st.header("Topluluk Sıralaması")
    st.table({"Öğrenci": ["Mert", "Ayşe", "Can"], "Puan": [1250, 1100, 950]})