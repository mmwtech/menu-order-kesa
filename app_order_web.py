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

qty_asinan = st.number_input(
    "Asinan Buah",
    min_value=0,
    value=0
)

qty_eslilin = st.number_input(
    "Es Lilin",
    min_value=0,
    value=0
)

qty_frozen = st.number_input(
    "Frozen Snack",
    min_value=0,
    value=0
)

qty_couple = st.number_input(
    "Paket Couple",
    min_value=0,
    value=0
)

qty_keluarga = st.number_input(
    "Paket Keluarga",
    min_value=0,
    value=0
)

# =========================================
# HARGA
# =========================================

harga_asinan = 20000
harga_eslilin = 3000
harga_frozen = 15000
harga_couple = 35000
harga_keluarga = 65000

# =========================================
# TOTAL PER MENU
# =========================================

total_asinan = qty_asinan * harga_asinan
total_eslilin = qty_eslilin * harga_eslilin
total_frozen = qty_frozen * harga_frozen
total_couple = qty_couple * harga_couple
total_keluarga = qty_keluarga * harga_keluarga

# =========================================
# GRAND TOTAL
# =========================================

total = (
    total_asinan
    + total_eslilin
    + total_frozen
    + total_couple
    + total_keluarga
)

# =========================================
# RINGKASAN
# =========================================

st.markdown("---")
st.subheader("🧾 Ringkasan Order")

if qty_asinan > 0:
    st.write(
        f"Asinan Buah : "
        f"{qty_asinan} x Rp {harga_asinan:,}"
    )

if qty_eslilin > 0:
    st.write(
        f"Es Lilin : "
        f"{qty_eslilin} x Rp {harga_eslilin:,}"
    )

if qty_frozen > 0:
    st.write(
        f"Frozen Snack : "
        f"{qty_frozen} x Rp {harga_frozen:,}"
    )

if qty_couple > 0:
    st.write(
        f"Paket Couple : "
        f"{qty_couple} x Rp {harga_couple:,}"
    )

if qty_keluarga > 0:
    st.write(
        f"Paket Keluarga : "
        f"{qty_keluarga} x Rp {harga_keluarga:,}"
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

Asinan Buah : {qty_asinan}
Es Lilin : {qty_eslilin}
Frozen Snack : {qty_frozen}
Paket Couple : {qty_couple}
Paket Keluarga : {qty_keluarga}

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