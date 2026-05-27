import streamlit as st
import urllib.parse

# =========================================
# CONFIG
# =========================================

st.set_page_config(
    page_title="KeSa Homemade",
    layout="centered"
)

# =========================================
# HEADER
# =========================================

st.title("🍨 KeSa Homemade")
st.subheader(
    "Order Foods & Drinks Minimal Rp 50.000 "
    "Free Delivery Cikarang"
)

# =========================================
# INPUT CUSTOMER
# =========================================

nama = st.text_input("Nama Pembeli")

alamat = st.text_area("Alamat Pengiriman")

catatan = st.text_area("Catatan Tambahan")

# =========================================
# MENU ORDER
# =========================================

st.markdown("---")
st.subheader("🛒 Pilih Menu")

qty_asinaneslilin = st.number_input(
    "Paket Asinan + Es Lilin - Rp 16.000",
    min_value=0,
    value=0
)

qty_paketelk = st.number_input(
    "Paket Es Lilin Kecil (isi 10) - Rp 25.000",
    min_value=0,
    value=0
)

qty_paketelb = st.number_input(
    "Paket Es Lilin Besar (isi 6) - Rp 25.000",
    min_value=0,
    value=0
)

qty_mojito = st.number_input(
    "Es Mojito - Rp 15.000",
    min_value=0,
    value=0
)

qty_sogem = st.number_input(
    "Es Soda Gembira - Rp 15.000",
    min_value=0,
    value=0
)

# MENU BARU

qty_matcha = st.number_input(
    "Es Matcha Susu - Rp 15.000",
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

harga_asinaneslilin = 16000
harga_paketelk = 25000
harga_paketelb = 25000
harga_mojito = 15000
harga_sogem = 15000

harga_matcha = 15000
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
# GRAND TOTAL
# =========================================

total = (
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

st.subheader(f"💰 Total : Rp {total:,}")

# =========================================
# VALIDASI MINIMAL ORDER
# =========================================

minimal_order = 50000

if total > 0 and total < minimal_order:

    kurang = minimal_order - total

    st.warning(
        f"Minimal order delivery Rp 50.000\n\n"
        f"Tambah order lagi Rp {kurang:,}"
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

Total : Rp {total:,}

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

if total >= minimal_order:

    if st.button("📲 Kirim Order ke WhatsApp"):

        st.markdown(
            f"""
            <a href="{link_wa}" target="_blank">
                Klik di sini untuk membuka WhatsApp
            </a>
            """,
            unsafe_allow_html=True
        )