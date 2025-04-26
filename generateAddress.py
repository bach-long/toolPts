import json
import random

# ----------- DỮ LIỆU MẪU CHO 5 THÀNH PHỐ LỚN -----------
# Tương ứng với "city" -> "district" -> "wards"
# Mỗi district mình thêm một ít phường ví dụ
CITY_DATA = {
    "Hà Nội": {
        "districts": {
            "Ba Đình": [
                "Phường Cống Vị",
                "Phường Điện Biên",
                "Phường Đội Cấn",
                "Phường Giảng Võ",
                "Phường Kim Mã",
            ],
            "Hoàn Kiếm": [
                "Phường Chương Dương",
                "Phường Cửa Đông",
                "Phường Hàng Bạc",
                "Phường Hàng Bồ",
                "Phường Hàng Bông",
            ],
            "Tây Hồ": [
                "Phường Bưởi",
                "Phường Quảng An",
                "Phường Thụy Khuê",
                "Phường Xuân La",
            ],
            "Long Biên": [
                "Phường Bồ Đề",
                "Phường Cự Khối",
                "Phường Đức Giang",
                "Phường Thạch Bàn",
            ],
            "Cầu Giấy": [
                "Phường Dịch Vọng",
                "Phường Nghĩa Đô",
                "Phường Nghĩa Tân",
                "Phường Quan Hoa",
            ],
            # ... bạn bổ sung thêm nếu cần ...
        },
        "roads": [
            "Kim Mã",
            "Liễu Giai",
            "Đê La Thành",
            "Xuân Thủy",
            "Cầu Giấy",
            "Giải Phóng",
            "Lê Duẩn",
            "Nguyễn Trãi",
            "Trường Chinh",
            "Phạm Văn Đồng",
            "Lạc Long Quân",
            "Thụy Khuê",
            "Hoàng Hoa Thám",
            "Nguyễn Khánh Toàn",
            "Hoàng Cầu",
            "Chùa Láng",
            "Phạm Hùng",
            "Nguyễn Chí Thanh",
            "Phố Huế",
            "Hàng Bài",
        ],
    },
    "Hồ Chí Minh": {
        "districts": {
            "Quận 1": [
                "Phường Cầu Kho",
                "Phường Cầu Ông Lãnh",
                "Phường Bến Nghé",
                "Phường Bến Thành",
            ],
            "Quận 3": ["Phường 1", "Phường 2", "Phường 6", "Phường 7"],
            "Quận 5": ["Phường 1", "Phường 2", "Phường 6", "Phường 8"],
            "Quận 10": ["Phường 1", "Phường 2", "Phường 9", "Phường 10"],
            "Thành phố Thủ Đức": [
                "Phường An Khánh",
                "Phường Thảo Điền",
                "Phường Linh Trung",
                "Phường Hiệp Bình Chánh",
            ],
            # ... bổ sung thêm nếu cần ...
        },
        "roads": [
            "Trần Hưng Đạo",
            "Nguyễn Trãi",
            "Cách Mạng Tháng 8",
            "Lý Tự Trọng",
            "Lê Lợi",
            "Nam Kỳ Khởi Nghĩa",
            "Điện Biên Phủ",
            "Xô Viết Nghệ Tĩnh",
            "Phan Đăng Lưu",
            "Hoàng Văn Thụ",
            "Phạm Văn Đồng",
            "Võ Văn Kiệt",
            "Hải Thượng Lãn Ông",
            "An Dương Vương",
            "Hồng Bàng",
            "Nguyễn Thị Minh Khai",
            "Đinh Tiên Hoàng",
            "Phan Xích Long",
            "Nguyễn Oanh",
            "Quang Trung",
        ],
    },
    "Đà Nẵng": {
        "districts": {
            "Hải Châu": [
                "Phường Bình Hiên",
                "Phường Hòa Thuận Tây",
                "Phường Phước Ninh",
                "Phường Thạch Thang",
            ],
            "Thanh Khê": [
                "Phường An Khê",
                "Phường Chính Gián",
                "Phường Hòa Khê",
                "Phường Thanh Khê Đông",
            ],
            "Sơn Trà": ["Phường An Hải Bắc", "Phường An Hải Tây", "Phường Mân Thái"],
            "Ngũ Hành Sơn": ["Phường Hòa Hải", "Phường Khuê Mỹ", "Phường Mỹ An"],
        },
        "roads": [
            "Điện Biên Phủ",
            "Lê Duẩn",
            "Trần Phú",
            "Nguyễn Văn Linh",
            "Ngô Quyền",
            "Trường Sa",
            "Hoàng Sa",
            "Xô Viết Nghệ Tĩnh",
            "Âu Cơ",
            "Lê Lợi",
        ],
    },
    "Hải Phòng": {
        "districts": {
            "Hồng Bàng": [
                "Phường Hạ Lý",
                "Phường Minh Khai",
                "Phường Sở Dầu",
                "Phường Trại Chuối",
            ],
            "Lê Chân": [
                "Phường An Biên",
                "Phường Dư Hàng",
                "Phường Hàng Kênh",
                "Phường Lam Sơn",
            ],
            "Ngô Quyền": [
                "Phường Cầu Đất",
                "Phường Cầu Tre",
                "Phường Đằng Giang",
                "Phường Gia Viên",
            ],
            "Kiến An": ["Phường Bắc Sơn", "Phường Đồng Hòa", "Phường Quán Trữ"],
        },
        "roads": [
            "Tôn Đức Thắng",
            "Trần Nguyên Hãn",
            "Lạch Tray",
            "Ngô Gia Tự",
            "Cát Dài",
            "Cầu Đất",
            "Hoàng Diệu",
            "Phan Bội Châu",
            "Trần Hưng Đạo",
            "Máy Tơ",
        ],
    },
    "Cần Thơ": {
        "districts": {
            "Ninh Kiều": [
                "Phường An Cư",
                "Phường An Bình",
                "Phường Tân An",
                "Phường Xuân Khánh",
            ],
            "Bình Thủy": ["Phường An Thới", "Phường Bùi Hữu Nghĩa", "Phường Long Hòa"],
            "Cái Răng": ["Phường Ba Láng", "Phường Lê Bình", "Phường Phú Thứ"],
            "Ô Môn": ["Phường Châu Văn Liêm", "Phường Thới An", "Phường Trường Lạc"],
        },
        "roads": [
            "30 Tháng 4",
            "Hòa Bình",
            "Trần Văn Khéo",
            "Nguyễn Văn Linh",
            "Cách Mạng Tháng 8",
            "Mậu Thân",
            "Trần Quang Diệu",
            "Phan Đình Phùng",
            "Lý Tự Trọng",
            "Ngô Quyền",
        ],
    },
}


def generate_1000_addresses(output_file="vn_addresses.json", quantity=1000):
    """
    Sinh ra 1000 địa chỉ thực tế (đúng city, district, ward, road)
    nhưng chỉ random số nhà, ngõ, ngách.
    """
    results = []

    # Gom thành danh sách (city, district, ward, road) có thật
    # Ta sẽ duyệt CITY_DATA, rồi district, wards => roads
    combos = []
    for city, city_info in CITY_DATA.items():
        # city_info: { 'districts': { ... }, 'roads': [...] }
        district_dict = city_info["districts"]  # dict: district_name -> list_of_wards
        roads = city_info["roads"]  # list_of_roads

        for district, ward_list in district_dict.items():
            for ward in ward_list:
                for road in roads:
                    combos.append((city, district, ward, road))

    # Nếu combos < 1000, ta sẽ random sampling with replacement
    # Bởi 1 city-district-ward-road ta có thể dùng nhiều lần
    # Mỗi lần random house, alley, sub_alley.
    for _ in range(quantity):
        city, district, ward, road = random.choice(combos)

        house_num = random.randint(1, 999)
        alley_num = random.randint(1, 99)
        branch_num = random.randint(1, 50)

        full_address = (
            f"Số {house_num}, Ngõ {alley_num}, Ngách {branch_num}, Đường {road}, {ward}, {district}, Thành Phố {city}, Việt Nam"
        )

        results.append(
            {
                "full_address": full_address,
                "city": city,
                "district": district,
                "ward": ward,
                "road": road,
                "house_num": house_num,
                "alley_num": alley_num,
                "branch_num": branch_num,
            }
        )

    # Xuất ra file JSON
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"Đã tạo {quantity} địa chỉ trong file {output_file}.")


# Chạy thử
if __name__ == "__main__":
    generate_1000_addresses()