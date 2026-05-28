import streamlit as st
import urllib.parse
import re

# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="KeSa Homemade",
    layout="centered"
)

# =========================================
# VALIDASI INPUT
# =========================================

def valid_text(teks, min_char):

    teks = teks.strip()

    if len(teks) < min_char:
        return False

    if not re.search(r"[A-Za-zÀ-ÿ]", teks):
        return False

    if not re.fullmatch(
        r"[A-Za-zÀ-ÿ0-9\s,./\-]+",
        teks
    ):
        return False

    return True

# =========================================
# ONGKIR
# =========================================

ongkir_data = {
    "Babelan": 22000,
    "Bojongmangu": 18000,
    "Cabangbungin": 42000,
    "Cibarusah": 8000,
    "Cibitung": 12000,
    "Cikarang Barat": 5000,
    "Cikarang Pusat": 8000,
    "Cikarang Selatan": 4000,
    "Cikarang Timur": 14000,
    "Cikarang Utara": 9000,
    "Karangbahagia": 17000,
    "Kedungwaringin": 19000,
    "Muaragembong": 35000,
    "Pebayuran": 24000,
    "Serang Baru": 5000,
    "Setu": 11000,
    "Sukakarya": 18000,
    "Sukatani": 17000,
    "Tambelang": 16000,
    "Tambun Selatan": 12000,
    "Tambun Utara": 16000,
    "Tarumajaya": 26000
}

free_ongkir_area = [
    "Cikarang Selatan",
    "Cikarang Barat",
    "Cikarang Pusat",
    "Cikarang Utara"
]

minimal_free_ongkir = 100000

# =========================================
# HEADER
# =========================================

st.title("🍨 KeSa Homemade")

st.subheader(
    "Order Foods & Drinks"
)

st.info(
    "🎁 Free Ongkir minimal Rp100.000 "
    "khusus Cikarang Selatan, "
    "Cikarang Barat, "
    "Cikarang Pusat, "
    "dan Cikarang Utara"
)

# =========================================
# INPUT CUSTOMER
# =========================================

nama = st.text_input("Nama Pembeli")

alamat = st.text_area("Alamat Pengiriman")

kecamatan = st.selectbox(
    "Pilih Kecamatan",
    list(ongkir_data.keys())
)

catatan = st.text_area("Catatan Tambahan")

# =========================================
# MENU ORDER
# =========================================

st.markdown("---")
st.subheader("🛒 Pilih Menu")

qty_asinaneslilin = st.number_input(
    "Paket Asinan + Es Lilin - Rp 15.500",
    min_value=0,
    value=0
)

qty_paketelk = st.number_input(
    "Paket Es Lilin Kecil (isi 10) - Rp 25.000",
    min_value=0,
    value=0
)

qty_paketelb = st.number_input(
    "Paket Es Lilin Besar (isi 5) - Rp 20.000",
    min_value=0,
    value=0
)

qty_mojito = st.number_input(
    "Es Mojito - Rp 12.000",
    min_value=0,
    value=0
)

qty_sogem = st.number_input(
    "Es Soda Gembira - Rp 12.000",
    min_value=0,
    value=0
)

qty_matcha = st.number_input(
    "Es Matcha Susu - Rp 12.000",
    min_value=0,
    value=0
)

qty_lemon = st.number_input(
    "Es Teh Lemon Cheong - Rp 10.000",
    min_value=0,
    value=0
)

qty_jeruk = st.number_input(
    "Es Jeruk Selasih - Rp 8.000",
    min_value=0,
    value=0
)

# =========================================
# HARGA
# =========================================

harga_asinaneslilin = 15500
harga_paketelk = 25000
harga_paketelb = 20000
harga_mojito = 12000
harga_sogem = 12000
harga_matcha = 12000
harga_lemon = 10000
harga_jeruk = 8000

# =========================================
# TOTAL PER MENU
# =========================================

total_asinaneslilin = (
    qty_asinaneslilin * harga_asinaneslilin
)

total_paketelk = qty_paketelk * harga_paketelk

total_paketelb = qty_paketelb * harga_paketelb

total_mojito = qty_mojito * harga_mojito

total_sogem = qty_sogem * harga_sogem

total_matcha = qty_matcha * harga_matcha

total_lemon = qty_lemon * harga_lemon

total_jeruk = qty_jeruk * harga_jeruk

# =========================================
# SUBTOTAL
# =========================================

subtotal = (
    total_asinaneslilin
    + total_paketelk
    + total_paketelb
    + total_mojito
    + total_sogem
    + total_matcha
    + total_lemon
    + total_jeruk
)

# =========================================
# ONGKIR
# =========================================

ongkir_asli = ongkir_data[kecamatan]

if (
    kecamatan in free_ongkir_area
    and subtotal >= minimal_free_ongkir
):
    ongkir = 0
    free_ongkir = True
else:
    ongkir = ongkir_asli
    free_ongkir = False

# =========================================
# GRAND TOTAL
# =========================================

grand_total = subtotal + ongkir

# =========================================
# RINGKASAN
# =========================================

st.markdown("---")
st.subheader("🧾 Ringkasan Order")

if qty_asinaneslilin > 0:
    st.write(
        f"Paket Asinan + Es Lilin : "
        f"{qty_asinaneslilin} x Rp {harga_asinaneslilin:,}"
    )

if qty_paketelk > 0:
    st.write(
        f"Paket Es Lilin Kecil : "
        f"{qty_paketelk} x Rp {harga_paketelk:,}"
    )

if qty_paketelb > 0:
    st.write(
        f"Paket Es Lilin Besar : "
        f"{qty_paketelb} x Rp {harga_paketelb:,}"
    )

if qty_mojito > 0:
    st.write(
        f"Es Mojito : "
        f"{qty_mojito} x Rp {harga_mojito:,}"
    )

if qty_sogem > 0:
    st.write(
        f"Es Soda Gembira : "
        f"{qty_sogem} x Rp {harga_sogem:,}"
    )

if qty_matcha > 0:
    st.write(
        f"Es Matcha Susu : "
        f"{qty_matcha} x Rp {harga_matcha:,}"
    )

if qty_lemon > 0:
    st.write(
        f"Es Teh Lemon Cheong : "
        f"{qty_lemon} x Rp {harga_lemon:,}"
    )

if qty_jeruk > 0:
    st.write(
        f"Es Jeruk Selasih : "
        f"{qty_jeruk} x Rp {harga_jeruk:,}"
    )

st.markdown("---")

st.write(f"Subtotal : Rp {subtotal:,}")

if free_ongkir:
    st.success(
        f"🎉 FREE ONGKIR "
        f"(Normal Rp {ongkir_asli:,})"
    )
else:
    st.write(f"Ongkir : Rp {ongkir:,}")

st.subheader(
    f"💰 Grand Total : Rp {grand_total:,}"
)

# =========================================
# VALIDASI MINIMAL ORDER
# =========================================

minimal_order = 25000

if subtotal > 0 and subtotal < minimal_order:

    kurang = minimal_order - subtotal

    st.warning(
        f"Minimal order delivery Rp 25.000\n\n"
        f"Tambah order lagi Rp {kurang:,}"
    )

# =========================================
# VALIDASI FORM
# =========================================

nama_valid = valid_text(nama, 4)

alamat_valid = valid_text(alamat, 6)

if nama and not nama_valid:
    st.warning(
        "Nama minimal 4 huruf "
        "dan tidak boleh karakter aneh."
    )

if alamat and not alamat_valid:
    st.warning(
        "Alamat minimal 6 huruf "
        "dan tidak boleh karakter aneh."
    )

# =========================================
# WHATSAPP
# =========================================

nomor_wa = "6281804525422"

pesan = f"""
Halo KeSa Homemade 👋

Saya ingin order:

Nama : {nama}

====================

Paket Asinan + Es Lilin : {qty_asinaneslilin}
Paket Es Lilin Kecil : {qty_paketelk}
Paket Es Lilin Besar : {qty_paketelb}
Es Mojito : {qty_mojito}
Es Soda Gembira : {qty_sogem}
Es Matcha Susu : {qty_matcha}
Es Teh Lemon Cheong : {qty_lemon}
Es Jeruk Selasih : {qty_jeruk}

====================

Kecamatan : {kecamatan}

Subtotal : Rp {subtotal:,}
"""

if free_ongkir:
    pesan += "Ongkir : GRATIS\n"
else:
    pesan += f"Ongkir : Rp {ongkir:,}\n"

pesan += f"""
Grand Total : Rp {grand_total:,}

Alamat:
{alamat}

Catatan:
{catatan}
"""

pesan_encode = urllib.parse.quote(pesan)

link_wa = (
    f"https://wa.me/{nomor_wa}"
    f"?text={pesan_encode}"
)

# =========================================
# BUTTON ORDER
# =========================================

if (
    subtotal >= minimal_order
    and nama_valid
    and alamat_valid
):

    if st.button("📲 Kirim Order ke WhatsApp"):

        st.markdown(
            f"""
            <a href="{link_wa}" target="_blank">
                Klik di sini untuk membuka WhatsApp
            </a>
            """,
            unsafe_allow_html=True
        )