import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="Algorit-Mat Pro", layout="wide")

# SİBER-BUZ TEMASI (Görsel Standartlar)
st.markdown("""
    <style>
    .stApp { background: #050a12; color: #00f2ff; }
    .math-card { 
        background: rgba(0, 242, 255, 0.1); 
        padding: 20px; border-radius: 15px; 
        border: 1px solid #00f2ff; margin-bottom: 20px;
    }
    .code-box { 
        background: #000; border: 1px solid #00f2ff; 
        padding: 15px; border-radius: 10px; font-family: 'Courier New', monospace;
        color: #00ffcc;
    }
    .step-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 10px; border-radius: 8px;
        border-left: 4px solid #00f2ff; margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Hafıza Yönetimi (Session State)
if 'steps' not in st.session_state:
    st.session_state.steps = []

# Başlık ve Matematiksel Kural [cite: 168]
st.title("🧪 Algorit-Mat: Blok Tabanlı Mantık Atölyesi")
st.markdown('<div class="math-card">', unsafe_allow_html=True)
st.subheader("📐 Üçgen Eşitsizliği Teoremi")
st.latex(r"|a - b| < c < a + b") #
st.write("Hedef: Kenarların bu kurala uygunluğunu denetleyen algoritmayı kur!")
st.markdown('</div>', unsafe_allow_html=True)

# Blok Tanımları [cite: 177]
available_blocks = {
    "📥 Veri Al": "a, b, c = inputs()",
    "🧮 Hesapla": "fark = abs(a-b); toplam = a+b",
    "🔍 Kontrol Et": "if fark < c < toplam:",
    "📤 Çıktı Ver": "print('Üçgen Çizilebilir')"
}

col_left, col_right = st.columns([1, 1.2])

with col_left:
    st.subheader("🧩 Bloklar")
    # Her butona tıklandığında listeye ekle ve sayfayı yenile
    for block_name in available_blocks.keys():
        if st.button(f"➕ {block_name}", key=f"btn_{block_name}"):
            if block_name not in st.session_state.steps:
                st.session_state.steps.append(block_name)
                st.rerun() # Sayfayı anında yenileyerek hatayı engeller

    if st.button("🗑️ Algoritmayı Sıfırla"):
        st.session_state.steps = []
        st.rerun()

with col_right:
    st.subheader("🏗️ Senin Algoritman")
    # Liste boşsa uyarı ver, doluysa blokları göster
    if not st.session_state.steps:
        st.info("Sol taraftaki bloklara tıklayarak algoritmanı inşa etmeye başla!")
    else:
        for i, step in enumerate(st.session_state.steps):
            st.markdown(f'<div class="step-card"><b>Adım {i+1}:</b> {step}</div>', unsafe_allow_html=True)
            if i < len(st.session_state.steps) - 1:
                st.markdown("  ↓  ")
        
        # PYTHON KODUNU ANLIK GÖRÜNTÜLEME [cite: 178]
        st.markdown("### 🐍 Python Kod Karşılığı")
        st.markdown('<div class="code-box">', unsafe_allow_html=True)
        for step in st.session_state.steps:
            st.text(available_blocks[step])
        st.markdown('</div>', unsafe_allow_html=True)

# TEST VE ÇALIŞTIRMA [cite: 175, 176]
if len(st.session_state.steps) == 4:
    st.markdown("---")
    st.success("🎯 Algoritma tamamlandı! Şimdi test edebilirsin.")
    
    c1, c2, c3 = st.columns(3)
    val_a = c1.number_input("Kenar A", value=10)
    val_b = c2.number_input("Kenar B", value=12)
    val_c = c3.number_input("Kenar C", value=5)
    
    if st.button("🚀 Algoritmayı Çalıştır"):
        # Doğru Sıralama Kontrolü [cite: 22]
        correct_order = ["📥 Veri Al", "🧮 Hesapla", "🔍 Kontrol Et", "📤 Çıktı Ver"]
        if st.session_state.steps == correct_order:
            if abs(val_a - val_b) < val_c < (val_a + val_b):
                st.balloons()
                st.success("✅ Algoritma Doğru: Bu bir üçgendir!")
            else:
                st.error("❌ Algoritma Doğru: Bu bir üçgen değildir!")
        else:
            st.warning("⚠️ Sıralama Hatası: Algoritma basamakların mantıklı değil. Önce veriyi almalı, sonra hesaplamalısın!")
