import streamlit as st

# Sayfa Ayarları (Ferah ve Aydınlık Mod)
st.set_page_config(page_title="Algorit-Mat Akademi", page_icon="📐")

# Sadeleştirilmiş Stil
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; color: #334155; }
    .rule-box { background-color: #f1f5f9; padding: 20px; border-radius: 10px; border-left: 5px solid #3b82f6; }
    .code-view { background-color: #1e293b; color: #38bdf8; padding: 15px; border-radius: 8px; font-family: monospace; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 Algorit-Mat Öğrenme Laboratuvarı")
st.write("Matematik ve Yazılımın Buluştuğu Nokta")

# 1. BÖLÜM: Matematiksel Temel [cite: 173]
st.markdown('<div class="rule-box">', unsafe_allow_html=True)
st.subheader("📐 Üçgen Eşitsizliği Kuralı")
st.write("Bir üçgen oluşturmak için seçilen kenarlar şu şartı sağlamalıdır:")
st.latex(r"|a - b| < c < a + b")
st.markdown('</div>', unsafe_allow_html=True)

# 2. BÖLÜM: Algoritma İnşası (Hata Vermeyen Seçim Yapısı)
st.subheader("🧩 Algoritmanı İnşa Et")
st.caption("Algoritma basamaklarını mantıklı bir sırayla aşağıdan seç:")

# Seçenekler ve Kod Karşılıkları
options_dict = {
    "1. Verileri Al": "a, b, c = girdi()",
    "2. Fark ve Toplamı Hesapla": "fark = abs(a-b); toplam = a+b",
    "3. Kuralı Kontrol Et": "if fark < c < toplam:",
    "4. Sonucu Yazdır": "print('Üçgen Çizilebilir!')"
}

# Sıralı Seçim Alanı
user_sequence = st.multiselect(
    "Algoritma Basamaklarını Seç:", 
    options=list(options_dict.keys()),
    help="Doğru sıra: Veri -> Hesaplama -> Kontrol -> Çıktı"
)

# Kod Görünümü
if user_sequence:
    st.markdown("### 🐍 Oluşan Python Kodu")
    st.markdown('<div class="code-view">', unsafe_allow_html=True)
    for step in user_sequence:
        st.text(options_dict[step])
    st.markdown('</div>', unsafe_allow_html=True)

# 3. BÖLÜM: Test Alanı (Tüm basamaklar seçilince açılır)
if len(user_sequence) == 4:
    st.divider()
    st.subheader("🚀 Algoritmanı Test Et")
    c1, c2, c3 = st.columns(3)
    val_a = c1.number_input("Kenar a", min_value=1, value=5)
    val_b = c2.number_input("Kenar b", min_value=1, value=5)
    val_c = c3.number_input("Kenar c", min_value=1, value=5)

    if st.button("Çalıştır"):
        # Doğru Sıralama Kontrolü
        if user_sequence == list(options_dict.keys()):
            if abs(val_a - val_b) < val_c < (val_a + val_b):
                st.success("🎯 Başarılı! Algoritman doğru ve bu bir üçgendir.")
            else:
                st.error("❌ Algoritman doğru ama bu değerlerle üçgen çizilemez.")
        else:
            st.warning("⚠️ Mantık Hatası: Adımları yanlış sırayla dizdin! Önce veriyi almalısın.")
else:
    st.info("Algoritmanı tamamlamak için sol taraftan 4 basamağı da seçmelisin.")
