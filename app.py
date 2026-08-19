
st.markdown('<p class="subtitle">รูปจะถูกส่งเข้า Cloudinary โดยตรง · ปลอดภัย</p>', unsafe_allow_html=True)
st.markdown('<hr class="divider">', unsafe_allow_html=True)

st.markdown("#### 📋 จำนวนใบเสร็จในรูป")
mode = st.radio("โหมด", [ "2 ใบเสร็จ"], label_visibility="collapsed")
num_receipts = int(mode[0])

# ── ชื่อผู้กรอก (พิมพ์เอง) ──
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown("#### 🙋 ชื่อผู้กรอก")
reporter_name = st.text_input(
    "ชื่อผู้กรอก",
    placeholder="พิมพ์ชื่อผู้กรอกข้อมูล",
    label_visibility="collapsed",
)

# ── แบรนด์ (เลือกได้ 1 รายการ) ──
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown("#### 🏷️ แบรนด์")
st.markdown('<div class="brand-box">เลือกแบรนด์ของใบเสร็จให้ตรงกับรายการที่กำลังส่ง</div>', unsafe_allow_html=True)
brand_options = ["-- กรุณาเลือกแบรนด์ --", "CJ", "MiniBig", "C Test"]
    brand_options,
    label_visibility="collapsed",
)

# ── ชื่อผู้กรอก (พิมพ์เอง) ──
st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown("#### 🙋 ชื่อผู้กรอก")
reporter_name = st.text_input(
    "ชื่อผู้กรอก",
    placeholder="พิมพ์ชื่อผู้กรอกข้อมูล",
    label_visibility="collapsed",
)

# ── เลือกสาขา (พิมพ์ค้นหาชื่อได้) แทนการพิมพ์เอง ──
st.markdown('<hr class="divider">', unsafe_allow_html=True)
