
                # แต่พิมพ์เก็บไว้ใน log ฝั่งเซิร์ฟเวอร์ให้เจ้าของระบบตามดูได้
                for r in fail:
                    print(f"UPLOAD FAILED: {r['filename']} — {r.get('detail', '')}")

                st.markdown(
                    f'<div class="error-box"><strong>❌ ไม่สำเร็จ {len(fail)} รูป โปรดลองอัพโหลดใหม่อีกครั้ง</strong>'
                    f'<br>(หาก Google Sheet ขัดข้องหลังอัปโหลด รูปจะถูกเก็บไว้และระบบจะลอง sync ใหม่อัตโนมัติ)</div>',
                    unsafe_allow_html=True,
                )

            if ok and not fail:
                st.session_state.show_sent_dialog = True
                st.session_state.sent_count = len(ok)
                st.rerun()

if st.session_state.show_sent_dialog:
    show_success_dialog()

st.markdown('<hr class="divider">', unsafe_allow_html=True)
st.markdown('<p style="text-align:center;color:#d1d5db;font-size:0.8rem;">รูปทั้งหมดจะถูกส่งเข้าบัญชี Cloudinary ของเจ้าของระบบเท่านั้น</p>', unsafe_allow_html=True)
