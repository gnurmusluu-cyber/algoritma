import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="Algorit-Mat Akademi", layout="wide")

# EDU-MODERN TASARIM (Aydınlık ve Ferah)
st.markdown("""
    <style>
    /* Ana Arka Plan */
    .stApp { background: #f8fafc; color: #1e293b; }
    
    /* Bölüm Kartları */
    .section-card { 
        background: #ffffff; 
        padding: 25px; border-radius: 12px; 
        border: 1px solid #e2e8f0; 
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
    /* Matematik Kural Alanı */
    .math-header { background: #eff6ff; border-left: 6px solid #3b82f6; padding: 15px; border-radius: 8px; }
    
    /* Blok Butonları */
    .stButton>button {
        background: #ffffff; color: #3b82f6; border: 2px solid #3b82f6;
        border-radius: 8px; width: 100%; font-weight: 600;
    }
    .stButton>button:hover { background: #3b82f6; color: #ffffff; }
    
    /* Kod Kutusu (Siyah Konsol) */
    .code-output { 
        background: #1e293b; color: #38bdf8; 
        padding: 15px; border-radius: 8px; 
        font-family: 'Consolas', monospace; font-size: 0.9rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Hafıza Yönetimi
if 'steps' not in st.session_state:
    st.session_state.steps = []

# ÜST BAŞLIK
st.title("🎓 Algorit-Mat Öğrenme Laboratuvarı")
st.markdown("---")

# 1. BÖLÜM: MATEMATİKSEL KURAL
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="math-header"><h3>📐 Üçgen Eşitsizliği Kuralları</h3></div>', unsafe_allow_html=True)
st.write("Bir üçgenin çizilebilmesi için her bir kenar, diğer iki kenarın farkından büyük, toplamından küçük olmalıdır:")
st.latex(r"|a - b| < c < a + b") #
st.markdown('</div>', unsafe_allow_html=True)

# Blok Tanımları
available_blocks = {
    "📥 Verileri Tanımla": "a, b, c = kenar_input()",
    "🧮 Fark ve Toplam": "fark = abs(a-b)\ntoplam = a+b",
    "🔍 Kuralı Denetle": "if fark < c < toplam:",
    "📤 Sonucu Yazdır": "print('Geometrik olarak mümkün!')"
}

# 2. BÖLÜM: ÇALIŞMA ALANI
col_left, col_right = st.columns([1, 1.3])

with col_left:
    st.subheader("🧩 Algoritma Blokları")
    st.caption("Adımları sırasıyla seçerek yapını kur:")
    for b_name in available_blocks.keys():
        if st.button(f"{b_name}", key=f"b_{b_name}"):
            if b_name not in st.session_state.steps:
                st.session_state.steps.append(b_name)
                st.rerun()

    if st.button("🔄 Labı Temizle", type="secondary"):
        st.session_state.steps = []
        st.rerun()

with col_right:
    st.subheader("🏗️ Mantık Akış Şeması")
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    if not st.session_state.steps:
        st.warning("Henüz bir blok eklemedin. Sol taraftaki menüden ilk adımı seç!")
    else:
        for i, step in enumerate(st.session_state.steps):
            st.info(f"**{i+1}. Adım:** {step}")
            if i < len(st.session_state.steps) - 1:
                st.markdown("<center>⬇️</center>", unsafe_allow_html=True)
        
        st.markdown("### 🐍 Python Kod Karşılığı")
        st.markdown('<div class="code-output">', unsafe_allow_html=True)
        for step in st.session_state.steps:
            st.text(available_blocks[step])
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 3. BÖLÜM: SİMÜLASYON TESTİ
if len(st.session_state.steps) == 4:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.subheader("🚀 Algoritmanı Dene")
    
    t1, t2, t3 = st.columns(3)
    a_val = t1.number_input("Kenar A", min_value=1, value=6)
    b_val = t2.number_input("Kenar B", min_value=1, value=8)
    c_val = t3.number_input("Kenar C", min_value=1, value=10)
    
    if st.button("Laboratuvarı Çalıştır"):
        correct_order = ["📥 Verileri Tanımla", "🧮 Fark ve Toplam", "🔍 Kuralı Denetle", "📤 Sonucu Yazdır"]
        if st.session_state.steps == correct_order:
            if abs(a_val - b_val) < c_val < (a_val + b_val):
                st.balloons()
                st.success("✅ Algoritma Onaylandı: Bu bir üçgendir!")
            else:
                st.error("❌ Algoritma Doğru Çalıştı: Bu değerler kuralı ihlal ediyor.")
        else:
            st.warning("⚠️ Mantık Hatası: Blokların sırası pedagojik olarak hatalı!")
    st.markdown('</div>', unsafe_allow_html=True)
