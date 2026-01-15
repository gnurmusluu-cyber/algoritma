import streamlit as st
import time

# Sayfa Konfigürasyonu
st.set_page_config(page_title="Algorit-Mat Pro", page_icon="🧬", layout="wide")

# Gelişmiş Tasarım Notları
st.markdown("""
    <style>
    .stApp { background: #040911; color: #e6f1ff; }
    .logic-box { 
        background: rgba(0, 242, 255, 0.05); 
        padding: 20px; border-radius: 15px; 
        border-left: 5px solid #00f2ff;
        margin-bottom: 20px;
    }
    .code-block { background: #000000; border: 1px solid #333; padding: 10px; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧬 Algorit-Mat: Mantık ve Kod Atölyesi")

# 1. BÖLÜM: Matematiksel Kural (LaTeX)
st.markdown('<div class="logic-box">', unsafe_allow_html=True)
st.subheader("1. Matematiksel Temel")
st.write("Üçgen eşitsizliği kuralını hatırlayalım:")
st.latex(r"|a - b| < c < a + b") #
st.markdown('</div>', unsafe_allow_html=True)

# 2. BÖLÜM: Algoritma İnşası (Sürükle-Bırak/Sıralama Simülasyonu)
st.subheader("2. Algoritmanı İnşa Et")
st.info("Üçgenin çizilebilir olduğunu kontrol eden kodu doğru sırayla oluştur!")

# Algoritma adımları (Karışık halde)
options = [
    "IF koşulu kontrol et", 
    "Kenar uzunluklarını al", 
    "MUTLAK DEĞER hesapla", 
    "SONUCU ekrana yazdır"
]

# Öğrencinin seçimi (Sıralama mantığı)
user_logic = st.multiselect(
    "Algoritma adımlarını sırasıyla seç:",
    options,
    help="Doğru mantık sırası: Veri alma -> Hesaplama -> Kontrol -> Çıktı"
)

# 3. BÖLÜM: Python Kod Görünümü ve Çalıştırma
if len(user_logic) == 4:
    st.success("🎯 Algoritma yapısı kuruldu! Şimdi değerleri girebilirsin.")
    
    # Python Kodunu Göster (Kritik Özellik #2) 
    with st.expander("🐍 Python Kod Karşılığını Gör"):
        st.code("""
def ucgen_kontrol(a, b, c):
    # Adım 1: Verileri Al (Inputs)
    # Adım 2: Mutlak Değer ve Toplam Hesabı (Process)
    # Adım 3: Koşul Kontrolü (Decision)
    if abs(a - b) < c < (a + b):
        return True
    return False
        """, language='python')

    # Değer Girişi
    col1, col2, col3 = st.columns(3)
    a = col1.number_input("Kenar A", value=7)
    b = col2.number_input("Kenar B", value=10)
    c = col3.number_input("Kenar C", value=5)

    if st.button("Algoritmayı Çalıştır"):
        # Doğru mantık sırası kontrolü (Eğitici geri bildirim)
        correct_order = ["Kenar uzunluklarını al", "MUTLAK DEĞER hesapla", "IF koşulu kontrol et", "SONUCU ekrana yazdır"]
        
        if user_logic == correct_order:
            if (abs(a - b) < c < (a + b)):
                st.balloons()
                st.markdown("### ✅ SONUÇ: Üçgen Çizilebilir!")
            else:
                st.error("❌ SONUÇ: Üçgen Çizilemez! (Matematiksel kural ihlali)")
        else:
            st.warning("⚠️ Algoritma mantığın doğru çalışıyor ama sıralama hatan var! Önce veriyi almalı, sonra hesaplamalısın.")
else:
    st.warning("Lütfen algoritmanın tüm adımlarını (4 adım) mantıklı bir sırayla seçerek kilidi aç.")
