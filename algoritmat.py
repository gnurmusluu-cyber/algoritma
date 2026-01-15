import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="Algorit-Mat | Blok Tabanlı Eğitim", layout="wide")

# SİBER-BUZ TEMASI (Profesyonel Görünüm)
st.markdown("""
    <style>
    .stApp { background: #050a12; color: #00f2ff; }
    .block-container { padding-top: 2rem; }
    .math-card { 
        background: rgba(0, 242, 255, 0.1); 
        padding: 20px; border-radius: 15px; 
        border: 1px solid #00f2ff; text-align: center;
    }
    .code-box { 
        background: #000; border: 1px solid #333; 
        padding: 15px; border-radius: 10px; font-family: 'Courier New', monospace;
    }
    </style>
    """, unsafe_allow_html=True)

# Başlık ve Matematiksel Kural
st.title("🧪 Algorit-Mat: Mantık İnşa Atölyesi")
st.markdown('<div class="math-card">', unsafe_allow_html=True)
st.subheader("📐 Üçgen Eşitsizliği Teoremi")
st.latex(r"|a - b| < c < a + b")
st.info("Kural: Bir kenar, diğer ikisinin farkından büyük, toplamından küçük olmalıdır.")
st.markdown('</div>', unsafe_allow_html=True)

# Session State ile Algoritma Takibi
if 'steps' not in st.session_state:
    st.session_state.steps = []

# Blok Seçenekleri
available_blocks = {
    "📥 Veri Al": "a, b, c = inputs()",
    "🧮 Hesapla": "fark = abs(a-b); toplam = a+b",
    "🔍 Kontrol Et": "if fark < c < toplam:",
    "📤 Çıktı Ver": "print('Üçgen Çizilebilir')"
}

st.write("")
col_left, col_right = st.columns([1, 1.2])

with col_left:
    st.subheader("🧩 Kullanılabilir Bloklar")
    st.write("Bloklara tıklayarak algoritmanı oluştur:")
    
    for block_name in available_blocks.keys():
        if st.button(f"+ {block_name}", key=block_name):
            if block_name not in st.session_state.steps:
                st.session_state.steps.append(block_name)

    if st.button("🗑️ Algoritmayı Sıfırla", type="secondary"):
        st.session_state.steps = []
        st.rerun()

with col_right:
    st.subheader("🏗️ Senin Algoritman")
    if not st.session_state.steps:
        st.warning("Henüz bir blok eklemedin. Sol taraftan başla!")
    else:
        # Algoritma Görsel Akışı
        for i, step in enumerate(st.session_state.steps):
            st.markdown(f"**Adım {i+1}:** `{step}`")
            if i < len(st.session_state.steps) - 1:
                st.markdown("  ↓  ")
        
        # PYTHON KODUNU ANLIK GÖRÜNTÜLEME
        st.markdown("### 🐍 Python Kod Karşılığı")
        st.markdown('<div class="code-box">', unsafe_allow_html=True)
        for step in st.session_state.steps:
            st.text(available_blocks[step])
        st.markdown('</div>', unsafe_allow_html=True)

# ÇALIŞTIRMA VE TEST
if len(st.session_state.steps) == 4:
    st.divider()
    st.success("🎯 Tebrikler! Tam bir algoritma yapısı kurdun.")
    
    # Test Girdileri
    c1, c2, c3 = st.columns(3)
    val_a = c1.number_input("Kenar A", value=10)
    val_b = c2.number_input("Kenar B", value=12)
    val_c = c3.number_input("Kenar C", value=5)
    
    if st.button("🚀 Algoritmayı Test Et"):
        # Doğru Sıralama Kontrolü
        correct_order = ["📥 Veri Al", "🧮 Hesapla", "🔍 Kontrol Et", "📤 Çıktı Ver"]
        if st.session_state.steps == correct_order:
            if abs(val_a - val_b) < val_c < (val_a + val_b):
                st.balloons()
                st.success("✅ Algoritma Çalıştı: Bu değerlerle bir üçgen çizilebilir!")
            else:
                st.error("❌ Algoritma Çalıştı: Bu değerlerle üçgen çizilemez!")
        else:
            st.warning("⚠️ Mantık Hatası: Blokların sırası hatalı. Önce veri almalı, sonra hesaplama yapmalısın!")
