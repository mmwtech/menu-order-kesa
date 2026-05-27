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
st.subheader("Order Frozen Snack & Drinks")

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
    "Asinan plus es lilin",
    min_value=0,
    value=0
)

qty_paketelk = st.number_input(
    "Paket Es Lilin Kecil",
    min_value=0,
    value=0
)

qty_paketelb = st.number_input(
    "Paket Es Lilin Besar",
    min_value=0,
    value=0
)

qty_mojito = st.number_input(
    "Es Mojito",
    min_value=0,
    value=0
)

qty_sogem = st.number_input(
    "Es Soda Gembira",
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

# =========================================
# TOTAL PER MENU
# =========================================

total_asinaneslilin = qty_asinaneslilin * harga_asinaneslilin
total_paketelk = qty_paketelk * harga_paketelk
total_paketelb = qty_paketelb * harga_paketelb
total_mojito = qty_mojito * harga_mojito
total_sogem = qty_sogem * harga_sogem

# =========================================
# GRAND TOTAL
# =========================================

total = (
    total_asinaneslilin
    + total_paketelk
    + total_paketelb
    + total_mojito
    + total_sogem
)

# =========================================
# RINGKASAN
# =========================================

st.markdown("---")
st.subheader("🧾 Ringkasan Order")

if qty_asinaneslilin > 0:
    st.write(
        f"Asinan plus Es Lilin : "
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

st.markdown("---")

st.subheader(f"💰 Total : Rp {total:,}")

# =========================================
# WHATSAPP
# =========================================

nomor_wa = "6281804525422"

pesan = f"""
Halo KeSa Homemade 👋

Saya ingin order:

Nama : {nama}

====================

Asinan plus Es Lilin : {qty_asinaneslilin}
Paket Es Lilin Kecil : {qty_paketelk}
Paket Es Lilin Kecil : {qty_paketelb}
Es Mojito : {qty_mojito}
Es Soda Gembira : {qty_sogem}

====================

Total : Rp {total:,}

Alamat:
{alamat}

Catatan:
{catatan}
"""

pesan_encode = urllib.parse.quote(pesan)

link_wa = (
    f"https://wa.me/{6281804525422}"
    f"?text={pesan_encode}"
)

# =========================================
# BUTTON
# =========================================

if st.button("📲 Kirim Order ke WhatsApp"):

    st.markdown(
        f"""
        <a href="{link_wa}" target="_blank">
            Klik di sini untuk membuka WhatsApp
        </a>
        """,
        unsafe_allow_html=True
    )
