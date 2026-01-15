import streamlit as st
import time

# Sayfa yapılandırması
st.set_page_config(page_title="Algorit-Mat | YetGen 2025", page_icon="📐", layout="wide")

# Görsel Standartlar (Siber-Buz Teması)
st.markdown("""
    <style>
    .stApp { background-color: #060d14; color: #00f2ff; }
    .stButton>button { 
        background-color: #00f2ff; color: #000; 
        border: 2px solid #00f2ff; border-radius: 8px;
        width: 100%; font-weight: bold;
    }
    .stTextInput>div>div>input { background-color: #0c1a26; color: white; border: 1px solid #00f2ff; }
    .stSuccess { background-color: #0a2e2a; color: #00ffcc; border: 1px solid #00ffcc; }
    .stError { background-color: #2e0a0a; color: #ff4b4b; border: 1px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

# Yan Menü (Navigasyon) [cite: 163]
with st.sidebar:
    st.title("🚀 Algorit-Mat")
    st.markdown("---")
    choice = st.radio("Menü Seçimi:", ["Ana Sayfa", "Problem Çözücü", "Geri Bildirimler", "Takımımız"])
    st.markdown("---")
    st.info("Nitelikli Eğitim Hedefi: Somut Matematik & Algoritma")

# 1. Sayfa: Ana Sayfa (Değer Teklifi) [cite: 168]
if choice == "Ana Sayfa":
    st.header("Matematiği Kodla, Geleceği İnşa Et!")
    st.write("Algorit-Mat, soyut matematiksel kavramları algoritmalara dönüştürerek öğrenmeyi kalıcı hale getirir.")
    st.subheader("Neden Biz? [cite: 189]")
    col1, col2 = st.columns(2)
    with col1:
        st.write("✅ **Soyut Kavramları Somutlaştırır:** Formülleri çalışan kodlara dönüştürür.")
    with col2:
        st.write("✅ **Bilişimsel Düşünme:** Matematik problemleri üzerinden algoritma mantığını öğretir.")

# 2. Sayfa: Problem Çözücü (Kritik Özellikler) [cite: 175, 176]
elif choice == "Problem Çözücü":
    st.header("📐 Kritik Özellik: Üçgen Eşitsizliği Denetleyici")
    st.write("Matematiksel Kural: Bir kenar uzunluğu, diğer iki kenarın farkından büyük, toplamından küçük olmalıdır.")
    st.latex(r"|a - b| < c < a + b") # LaTeX kullanımı

    st.markdown("### Algoritma Girdileri")
    c1, c2, c3 = st.columns(3)
    with c1: a = st.number_input("Kenar a:", min_value=1, value=5)
    with c2: b = st.number_input("Kenar b:", min_value=1, value=5)
    with c3: c = st.number_input("Kenar c:", min_value=1, value=5)

    if st.button("Algoritmayı Çalıştır"):
        with st.spinner("Mantıksal denetim yapılıyor..."):
            time.sleep(1)
            # Algoritma Mantığı
            is_valid = (abs(a - b) < c < (a + b)) and (abs(a - c) < b < (a + c)) and (abs(b - c) < a < (b + a))
            
            if is_valid:
                st.success(f"🎨 Başarılı! {a}, {b} ve {c} değerleri ile bir üçgen çizilebilir.")
                st.code(f"if abs({a}-{b}) < {c} < ({a}+{b}):\n    print('Üçgen Çizilebilir')", language='python')
            else:
                st.error("⚠️ Hata! Matematiksel kurallara göre bu bir üçgen oluşturamaz.")
                st.write("Algoritma çıktısı: Koşul sağlanamadı.")

# 3. Sayfa: Geri Bildirimler (Sayısal Veriler) 
elif choice == "Geri Bildirimler":
    st.header("📊 Saha Doğrulaması")
    st.write("Müşteri görüşmeleri sonrası elde edilen veriler:")
    data = {"Kategori": ["Öğretmen Onayı", "Öğrenci İlgisi", "Uygulanabilirlik"], "Skor (%)": [92, 88, 95]}
    st.table(data)
    st.markdown("> 'İlk defa bir formülün neden var olduğunu anladım.' - *Persona Alıntısı* [cite: 186]")

# 4. Sayfa: Takımımız [cite: 187]
elif choice == "Takımımız":
    st.header("Ekip ve Roller [cite: 188]")
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Bilişim Teknolojileri Öğretmeni")
        st.write("Girişim fikrinin teknolojik altyapısı ve algoritma kurgusundan sorumlu.")
    with col_b:
        st.subheader("İlköğretim Matematik Öğretmeni")
        st.write("Müfredat uyumu, pedagojik içerik ve problem setlerinin tasarımı.")
