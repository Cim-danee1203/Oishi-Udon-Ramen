import streamlit as st

# 1. Cấu hình trang web
st.set_page_config(
    page_title="OISHI UDON & RAMEN",
    page_icon="🍜",
    layout="wide"
)

# Custom CSS giao diện
st.markdown("""
    <style>
    .stApp { background-color: #FAF6F0; }
    h1 { color: #A91D3A; text-align: center; margin-bottom: 5px; }
    .subtitle { text-align: center; color: #555; font-size: 1.1rem; margin-bottom: 25px; }
    .price { color: #C70039; font-weight: bold; font-size: 1.15rem; }
    .vat-note { font-size: 0.85rem; color: #777; font-style: italic; }
    </style>
""", unsafe_allow_html=True)

st.title("RAMEN & UDON OISHI")
st.markdown("<p class='subtitle'>Thực Đơn Mì & Cơm Nhật Bản - Đặt Món Trực Tuyến</p>", unsafe_allow_html=True)

# 2. DỮ LIỆU MENU
udon_menu = [
    {"id": "ubt1", "name": "Udon Bò Trứng", "sizes": {"Size S": 79000, "Size M": 99000}, "desc": "Sợi Udon dẻo dai kết hợp thịt bò xào mềm thơm và trứng onsen."},
    {"id": "ub", "name": "Udon Bò", "sizes": {"Size S": 69000, "Size M": 89000}, "desc": "Sợi Udon truyền thống phủ lớp thịt bò xào xốt Nhật đậm đà."},
    {"id": "unt", "name": "Udon Ngắm Trăng", "price": 39000, "desc": "Udon súp Dashi thanh ngọt kết hợp trứng lòng đào mềm béo."},
    {"id": "ubct", "name": "Udon Bò Cay Trứng", "price": 109000, "desc": "Udon bò cay xè chuẩn vị đậm đà kèm trứng mềm béo."},
    {"id": "utbt", "name": "Udon Trộn Bò Trứng", "price": 89000, "desc": "Udon khô trộn sốt đặc biệt, bò xào và trứng."},
    {"id": "ukchc", "name": "Udon Kim Chi Heo Cay", "price": 89000, "desc": "Nước dùng kimchi cay chua nhẹ từ Kimchi và thịt heo thái mỏng."},
    {"id": "ukchsc", "name": "Udon Kim Chi Hải Sản Cay", "price": 119000, "desc": "Nước súp Kimchi cay đậm đà chua nhẹ với tôm, mực và hải sản tươi."}
]

ramen_menu = [
    {"id": "sho", "name": "Shoyu Tonkostu Ramen", "price": 89000, "desc": "Nước dùng xương heo Tonkotsu béo ngậy kết hợp nước tương Shoyu."},
    {"id": "ryo", "name": "Ryoaki Tonkostu Ramen", "sizes": {"Size S": 69000, "Size M": 89000}, "desc": "Tonkotsu chuẩn vị truyền thống Ryoaki béo thơm lừng."},
    {"id": "soboro", "name": "Rayu Soboro Tonkostu Ramen", "price": 99000, "desc": "Thịt băm Soboro xào cay kết hợp dầu ớt Rayu béo ngậy."},
    {"id": "rcdgc", "name": "Ramen Cay Đùi Gà Chiên", "price": 89000, "desc": "Súp ramen cay đậm đà kèm đùi gà chiên giòn rụm."},
    {"id": "rayushoyu", "name": "Ramen Shoyu Tonkostu Cay", "price": 95000, "desc": "Súp Shoyu Tonkotsu thêm vị cay nồng kích thích vị giác."},
    {"id": "rkchc", "name": "Ramen KimChi Heo Cay", "price": 89000, "desc": "Mì Ramen kết hợp Kimchi cay chua nhẹ và thịt heo lát."},
    {"id": "rkchsc", "name": "Ramen KimChi Hải Sản Cay", "price": 119000, "desc": "Hải sản tươi ngon cùng Kimchi cay trong nước súp Ramen."},
    {"id": "rtcc", "name": "Ramen Trộn Chả Cá", "price": 69000, "desc": "Ramen khô trộn sốt kèm các loại chả cá Nhật Bản."},
    {"id": "rtsdc", "name": "Ramen Trộn Sò Điệp Cay", "price": 89000, "desc": "Ramen khô trộn cồi sò điệp xào sốt cay đặc biệt."}
]

kingkong_menu = [
    {"id": "k1", "name": "Rayu Shoyu Ramen King Kong", "price": 169000, "desc": "Tô khổng lồ gấp đôi topping: Rayu, thịt xá xíu, trứng và mì."},
    {"id": "k2", "name": "Rayu Soboro Tonkostu Ramen King Kong", "price": 169000, "desc": "Tô siêu bự dành cho tín đồ Ramen cay đậm đà béo ngậy."},
    {"id": "k3", "name": "Shoyu Ramen King Kong", "price": 159000, "desc": "Khẩu phần khổng lồ chuẩn vị Shoyu truyền thống."},
    {"id": "k4", "name": "Tonkostu Ramen King Kong", "price": 169000, "desc": "Tô Ramen Tonkotsu King Kong siêu đầy đặn."},
    {"id": "udb", "name": "Udon Đặc Biệt", "price": 189000, "desc": "Tô Udon King Kong tổng hợp đầy đủ thịt bò, chả cá chiên, tôm tempura, chả cá đậu, trứng onsen."}
]

rice_menu = [
    {"id": "ccrb", "name": "Cơm Cà Ri Bò", "price": 99000, "desc": "Cơm dẻo ăn kèm sốt Cà Ri Nhật Bản đậm đà và thịt bò mềm."},
    {"id": "ccrdgc", "name": "Cơm Cà Ri Đùi Gà Chiên", "price": 99000, "desc": "Đùi gà chiên giòn rụm phủ sốt Cà Ri Nhật thơm lừng."},
    {"id": "ccrgk", "name": "Cơm Cà Ri Gà Karaage", "price": 99000, "desc": "Gà chiên Karaage chuẩn vị kết hợp sốt Cà Ri."},
    {"id": "gyudon", "name": "Cơm Bò", "price": 69000, "desc": "Cơm phủ thịt bò xào hành tây xốt Nhật đậm đà."},
    {"id": "gyudon trứng", "name": "Cơm Bò Trứng", "price": 79000, "desc": "Cơm bò xào kèm trứng lòng đào mềm béo."},
    {"id": "ebi Tendon", "name": "Cơm Tôm Tempura", "price": 89000, "desc": "Cơm nóng ăn cùng tôm Tempura chiên xù giòn rụm."},
    {"id": "Chikuwa tendon", "name": "Cơm Chả Cá Chiên", "price": 69000, "desc": "Cơm phủ chả cá chiên giòn rưới sốt Chikuwa."}
]

side_menu = [
    {"id": "s1", "name": "Gà Chiên Karaage (3pcs)", "price": 49000, "desc": "Thịt đùi gà lọc xương chiên giòn kiểu Nhật."},
    {"id": "s2", "name": "Gyoza (5pcs)", "price": 69000, "desc": "Bánh xếp Nhật Bản nhân thịt heo áp chảo."},
    {"id": "s3", "name": "Đùi Gà Chiên", "price": 39000, "desc": "Đùi gà chiên xù lớp vỏ giòn rụm."},
    {"id": "s4", "name": "Tôm Tempura (3pcs)", "price": 99000, "desc": "Tôm chiên bột Tempura giòn nhẹ chuẩn vị Nhật."},
    {"id": "s5", "name": "Takoyaki", "price": 69000, "desc": "Bánh bạch tuộc nướng rưới sốt Takoyaki và cá bào."}
]

drink_menu = [
    {"name": "Pepsi", "price": 20000},
    {"name": "7 Up", "price": 20000},
    {"name": "Trà Chanh", "price": 15000},
    {"name": "Coca Cola", "price": 20000},
    {"name": "Mirinda", "price": 20000},
    {"name": "Pepsi Zero", "price": 20000},
    {"name": "Oolong Tea Plus+", "price": 22000},
    {"name": "Trà Đào", "price": 28000},
    {"name": "Trà Atiso", "price": 28000},
    {"name": "Aquafina", "price": 15000},
    {"name": "Saigon Special", "price": 35000},
    {"name": "Saigon Chill", "price": 35000}
]
# Gộp tất cả menu lại để phục vụ tính năng tìm kiếm
all_menu = udon_menu + ramen_menu + kingkong_menu + rice_menu + side_menu + drink_menu

# 3. Khởi tạo Giỏ hàng trong Session State
if "cart" not in st.session_state:
    st.session_state.cart = []

def add_to_cart(item_name, price):
    st.session_state.cart.append({"name": item_name, "price": price})
    st.toast(f"✅ Đã thêm: {item_name}")

# 4. BỐ CỤC CỘT (MENU & GIỎ HÀNG)
col_menu, col_cart = st.columns([2.2, 1])

with col_menu:
    st.caption("📌 *Tất cả giá niêm yết bên dưới chưa bao gồm 8% VAT.*")
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        " UDON", " RAMEN", " SIZE KING KONG", " MÓN CƠM", " MÓN PHỤ", " NƯỚC UỐNG"
    ])

    # --- TAB 1: UDON ---
    with tab1:
        for item in udon_menu:
            st.subheader(item["name"])
            st.write(item["desc"])
            if "sizes" in item:
                size_choice = st.radio("Chọn Size:", list(item["sizes"].keys()), key=f"sz_{item['id']}", horizontal=True)
                price = item["sizes"][size_choice]
                full_name = f"{item['name']} ({size_choice})"
            else:
                price = item["price"]
                full_name = item["name"]
            
            st.markdown(f"<p class='price'>{price:,} VNĐ</p>", unsafe_allow_html=True)
            if st.button("➕ Thêm món này", key=f"btn_{item['id']}"):
                add_to_cart(full_name, price)
            st.divider()

    # --- TAB 2: RAMEN ---
    with tab2:
        for item in ramen_menu:
            st.subheader(item["name"])
            st.write(item["desc"])
            if "sizes" in item:
                size_choice = st.radio("Chọn Size:", list(item["sizes"].keys()), key=f"sz_{item['id']}", horizontal=True)
                price = item["sizes"][size_choice]
                full_name = f"{item['name']} ({size_choice})"
            else:
                price = item["price"]
                full_name = item["name"]
            
            st.markdown(f"<p class='price'>{price:,} VNĐ</p>", unsafe_allow_html=True)
            if st.button("➕ Thêm món này", key=f"btn_{item['id']}"):
                add_to_cart(full_name, price)
            st.divider()

    # --- TAB 3: KING KONG ---
    with tab3:
        for item in kingkong_menu:
            st.subheader(item["name"])
            st.write(item["desc"])
            st.markdown(f"<p class='price'>{item['price']:,} VNĐ</p>", unsafe_allow_html=True)
            if st.button("➕ Thêm món này", key=f"btn_{item['id']}"):
                add_to_cart(item["name"], item["price"])
            st.divider()

    # --- TAB 4: CƠM ---
    with tab4:
        for item in rice_menu:
            st.subheader(item["name"])
            st.write(item["desc"])
            st.markdown(f"<p class='price'>{item['price']:,} VNĐ</p>", unsafe_allow_html=True)
            if st.button("➕ Thêm món này", key=f"btn_{item['id']}"):
                add_to_cart(item["name"], item["price"])
            st.divider()

    # --- TAB 5: MÓN PHỤ ---
    with tab5:
        for item in side_menu:
            st.subheader(item["name"])
            st.write(item["desc"])
            st.markdown(f"<p class='price'>{item['price']:,} VNĐ</p>", unsafe_allow_html=True)
            if st.button("➕ Thêm món này", key=f"btn_{item['id']}"):
                add_to_cart(item["name"], item["price"])
            st.divider()

    # --- TAB 6: THỨC UỐNG ---
    with tab6:
        for idx, item in enumerate(drink_menu):
            st.subheader(item["name"])
            st.markdown(f"<p class='price'>{item['price']:,} VNĐ</p>", unsafe_allow_html=True)
            if st.button("➕ Thêm đồ uống", key=f"drk_{idx}"):
                add_to_cart(item["name"], item["price"])
            st.divider()

# --- CỘT GIỎ HÀNG & ĐẶT HÀNG ---
with col_cart:
    st.subheader("🛒 Giỏ Hàng Của Bạn")
    
    if not st.session_state.cart:
        st.info("Giỏ hàng đang trống.")
    else:
        subtotal = 0
        for i, order in enumerate(st.session_state.cart):
            st.write(f"• **{order['name']}**")
            st.write(f"  └ {order['price']:,} VNĐ")
            subtotal += order['price']
        
        vat = int(subtotal * 0.08) # Thuế VAT 8%
        total = subtotal + vat
        
        st.divider()
        st.write(f"Tạm tính: **{subtotal:,} VNĐ**")
        st.write(f"Thuế VAT (8%): **{vat:,} VNĐ**")
        st.markdown(f"### Tổng cộng: :red[{total:,} VNĐ]")
        
        if st.button("🗑️ Xóa giỏ hàng"):
            st.session_state.cart = []
            st.rerun()

        st.subheader("📝 Thông Tin Giao Hàng")
        with st.form("checkout_form"):
            name = st.text_input("Họ và tên *")
            phone = st.text_input("Số điện thoại / Zalo *")
            address = st.text_area("Địa chỉ giao hàng *")
            payment = st.selectbox("Hình thức thanh toán:", ["Chuyển khoản VietQR", "Tiền mặt (COD)"])
            
            submitted = st.form_submit_button("🚀 ĐẶT MÓN NGAY")
            
            if submitted:
                if name and phone and address:
                    st.success("🎉 Đặt món thành công! Quán sẽ gọi xác nhận đơn ngay.")
                    st.balloons()
                    
                    if payment == "Chuyển khoản VietQR":
                        st.info("Quét mã VietQR bên dưới để thanh toán:")
                        # Thay ngân hàng & STK thật của bạn tại đây:
                        bank_id = "MB"          # MBBank, VCB, ACB, TPB, TCB...
                        account_num = "0987654321" 
                        account_name = "NHA HANG RAMEN UDON"
                        qr_url = f"https://img.vietqr.io/image/{bank_id}-{account_num}-compact.png?amount={total}&addInfo=DATMON%20{phone}&accountName={account_name}"
                        st.image(qr_url, caption="Mã QR Thanh Toán Tự Động", use_container_width=True)
                else:
                    st.error("Vui lòng nhập đầy đủ thông tin (*).")
