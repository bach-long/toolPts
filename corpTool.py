import comtypes.client
import json
import os
from datetime import datetime
from datetime import timedelta
import random
# import re
# import string
# import nltk
# from nltk.corpus import stopwords

base_dir = os.getcwd()
data = []
fileData = ""
# nhập file path vào đây(tính từ vị trí folder dự án vd:hanoi/ha-noi-7-7.json)
# Nội dung file tham khảo format trong folder hanoi
#  1 element sẽ gồm các thành phần như thế này, giữ nguyên format ngày tháng:
#  {
#     "Tên công ty": "CÔNG TY CỔ PHẦN CÔNG NGHỆ THỰC PHẨM THIÊN PHÚ",
#     "Tên quốc tế": "THIEN PHU FOOD TECHNOLOGY JOINT STOCK COMPANY",
#     "Mã số thuế": "0110986184",
#     "Tên viết tắt": "......"
#     "Địa chỉ": "Nhà số 45 Ngõ 45, Phố Nguyễn Gia Bồng, Phường Ngọc Thuỵ, Quận Long Biên, Thành phố Hà Nội, Việt Nam",
#     "Người đại diện": "NGUYỄN THỊ THANH HUYỀN",
#     "Điện thoại": "0359 438 309",
#     "Ngày hoạt động": "2025-03-12"
#  }
with open(os.path.abspath(fileData), "r", encoding="utf-8") as file:
    data = json.load(file)  # Chuyển nội dung file thành Python dictionary 
    data = list(filter(lambda element: "cổ phần" in element['Tên công ty'].lower() and element and "Tên quốc tế" in element, data))

def guessGender(name):
    splitName = name.split(' ')
    lastName = splitName[-1].lower()
    middleName = splitName[-2].lower()
    with open("names.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        malePoint = data["male"]["lastName"].get(lastName, 0) + data["male"]["middleName"].get(middleName, 0) * 2
        femalePoint = data["female"]["lastName"].get(lastName, 0) + data["female"]["middleName"].get(middleName, 0) * 2
    return 0 if malePoint >= femalePoint else 1

def fakeReassignDate(year_input: str):
    today = datetime.today().date()
    current_year = today.year
    month_now = today.month

    # Nếu năm nhập vào chỉ mới cách đây <= 2 năm
    if int(year_input) >= current_year - 2:
        return [1, None]

    # Số năm tính đến hiện tại
    diff_year = current_year - year_input

    # Nếu đang ở đầu năm (ví dụ tháng 1-2) thì random năm trước
    target_year = current_year - 1 if month_now <= 2 else current_year

    # Random tháng, ngày
    month = random.randint(1, 12)
    # Tính số ngày hợp lệ trong tháng đó
    _, days_in_month = divmod((datetime.date(target_year + (month == 12), (month % 12) + 1, 1) - datetime.timedelta(days=1)).day, 1000)
    # cách khác dễ hiểu hơn:
    last_day = (datetime.date(target_year if month < 12 else target_year + 1,
                              month % 12 + 1, 1) - datetime.timedelta(days=1)).day
    day = random.randint(1, last_day)

    random_date = f"ngày {day} tháng {month} năm {target_year}"

    return [diff_year, random_date]

def fakeFourthCharacter(gender):
    year = datetime.now().year
    if 1900 <= year <= 1999:
        if gender == 0:
            return "0"
        else:
            return "1"
    if 2000 <= year <= 2099:
        if gender == 0:
            return "2"
        else:
            return "3"
    if 2100 <= year <= 2199:
        if gender == 0:
            return "4"
        else:
            return "5"
    if 2200 <= year <= 2299:
        if gender == 0:
            return "6"
        else:
            return "7"
    if 2300 <= year <= 2399:
        if gender == 0:
            return "8"
        else:
            return "9"

# custom_blacklist = {
#     "co",
#     "co.",
#     "co.,"
#     "company",
#     "ltd",
#     "ltd.",
#     "inc",
#     "inc.",
#     "llc",
#     "group",
#     "&",
# }
# stop_words = set(stopwords.words("english")).union(custom_blacklist)
# def generate_acronym(text):
# # Loại bỏ dấu câu và chuyển về chữ thường
#     clean_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
#     words = clean_text.split()

#     # Loại bỏ các từ nằm trong stop_words
#     filtered = [word for word in words if word not in stop_words]

#     # Tạo chữ cái đầu từ các từ còn lại
#     acronym = "".join(word[0].upper() for word in filtered)
#     return acronym

def randomIdentityDate():
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2021, 12, 31)
    # Tính số ngày giữa ngày bắt đầu và ngày kết thúc
    delta_days = (end_date - start_date).days
    # Random một số ngày trong khoảng này
    random_days = random.randint(0, delta_days)
    # Tính ngày ngẫu nhiên
    random_date = start_date + timedelta(days=random_days)
    # Định dạng lại ngày theo định dạng DD/MM/YYYY
    formatted_date = random_date.strftime("%d/%m/%Y")
    return formatted_date

def fakeName():
    with open("names.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        firstName = random.choice(data["firstName"])
        gender = random.choice(["male", "female"])
        middleName = random.choice(data[gender]["middleName"]).keys()[0]
        lastName = random.choice(data[gender]["lastName"]).keys()[0]
    return {"name": f"{firstName} {middleName} {lastName}".upper(), "gender": "Nam" if gender == "male" else "Nữ"}

def randomDate():
    today = datetime.today()
    # 15 năm trước
    fifteen_years_ago = today - timedelta(days=15*365)
    # 10 năm trước
    ten_years_ago = today - timedelta(days=10*365)

    # Random số ngày trong khoảng từ 15 năm đến 10 năm trước
    random_days = random.randint(0, (ten_years_ago - fifteen_years_ago).days)

    # Tính toán ngày ngẫu nhiên
    random_date = fifteen_years_ago + timedelta(days=random_days)

    # Định dạng lại ngày theo DD/MM/YYYY
    formatted_date = random_date.strftime("%d/%m/%Y").split('/')
    return formatted_date

def randomBirthDay():
    start_date = datetime(1980, 1, 1)
    end_date = datetime(2000, 12, 31)
    # Tính số ngày giữa ngày bắt đầu và ngày kết thúc
    delta_days = (end_date - start_date).days
    # Random một số ngày trong khoảng này
    random_days = random.randint(0, delta_days)
    # Tính ngày ngẫu nhiên
    random_date = start_date + timedelta(days=random_days)
    # Định dạng lại ngày theo định dạng DD/MM/YYYY
    formatted_date = random_date.strftime("%d/%m/%Y")
    return formatted_date


def edit_text_layer(psd_file, part, dataIndex):
    global name
    global gender
    global birthDay
    global identityNum
    global identityDate
    global homeAddress
    # domains = ['electricstock.io.vn', 'giaydepnhanh.io.vn', 'noithat3d.io.vn', 'smartrent.id.vn', 'thoitrangnhanh.io.vn']
    input = {}
    capitals = [
        { "value": "542.207.610.000", "text": "Năm trăm bốn mươi hai tỷ hai trăm linh bảy triệu sáu trăm mười nghìn đồng" },
        { "value": "564.028.826.000", "text": "Năm trăm sáu mươi bốn tỷ hai mươi tám triệu tám trăm hai mươi sáu nghìn đồng" },
        { "value": "493.612.533.000", "text": "Bốn trăm chín mươi ba tỷ sáu trăm mười hai triệu năm trăm ba mươi ba nghìn đồng" },
        { "value": "433.938.449.000", "text": "Bốn trăm ba mươi ba tỷ chín trăm ba mươi tám triệu bốn trăm bốn mươi chín nghìn đồng" },
        { "value": "560.657.872.000", "text": "Năm trăm sáu mươi tỷ sáu trăm năm mươi bảy triệu tám trăm bảy mươi hai nghìn đồng" },
        { "value": "467.035.402.000", "text": "Bốn trăm sáu mươi bảy tỷ ba mươi lăm triệu bốn trăm linh hai nghìn đồng" },
        { "value": "400.155.954.000", "text": "Bốn trăm tỷ một trăm năm mươi lăm triệu chín trăm năm mươi bốn nghìn đồng" },
        { "value": "515.696.650.000", "text": "Năm trăm mười lăm tỷ sáu trăm chín mươi sáu triệu sáu trăm năm mươi nghìn đồng" },
        { "value": "503.529.120.000", "text": "Năm trăm linh ba tỷ năm trăm hai mươi chín triệu một trăm hai mươi nghìn đồng" },
        { "value": "543.233.760.000", "text": "Năm trăm bốn mươi ba tỷ hai trăm ba mươi ba triệu bảy trăm sáu mươi nghìn đồng" },
        { "value": "573.910.873.000", "text": "Năm trăm bảy mươi ba tỷ chín trăm mười triệu tám trăm bảy mươi ba nghìn đồng" },
        { "value": "485.809.287.000", "text": "Bốn trăm tám mươi lăm tỷ tám trăm linh chín triệu hai trăm tám mươi bảy nghìn đồng" },
        { "value": "503.290.090.000", "text": "Năm trăm linh ba tỷ hai trăm chín mươi triệu chín mươi nghìn đồng" },
        { "value": "488.498.148.000", "text": "Bốn trăm tám mươi tám tỷ bốn trăm chín mươi tám triệu một trăm bốn mươi tám nghìn đồng" },
        { "value": "527.222.407.000", "text": "Năm trăm hai mươi bảy tỷ hai trăm hai mươi hai triệu bốn trăm linh bảy nghìn đồng" },
        { "value": "512.958.992.000", "text": "Năm trăm mười hai tỷ chín trăm năm mươi tám triệu chín trăm chín mươi hai nghìn đồng" },
        { "value": "582.842.240.000", "text": "Năm trăm tám mươi hai tỷ tám trăm bốn mươi hai triệu hai trăm bốn mươi nghìn đồng" },
        { "value": "513.850.237.000", "text": "Năm trăm mười ba tỷ tám trăm năm mươi triệu hai trăm ba mươi bảy nghìn đồng" },
        { "value": "515.507.416.000", "text": "Năm trăm mười lăm tỷ năm trăm linh bảy triệu bốn trăm mười sáu nghìn đồng" },
        { "value": "572.294.625.000", "text": "Năm trăm bảy mươi hai tỷ hai trăm chín mươi bốn triệu sáu trăm hai mươi lăm nghìn đồng" }
    ]
    input["*business_code"] = data[dataIndex]["Mã số thuế"]
    input["*share_value"] = random.choice(["10000", "12000"])
    print(data[dataIndex]["Mã số thuế"])
    ownedCompanyAddress = ''
    with open("vn_addresses.json", "r", encoding="utf-8") as file:
        addresses = json.load(file)
        ownedCompanyAddress = random.choice([item for item in addresses if "Hà Nội" in item.get("full_address", "")])['full_address']
    if "Người đại diện" in data[dataIndex]:
        input["*owned_company_name"] = data[dataIndex]["Người đại diện"].upper()
        if gender is None:
            gender = "Nam" if guessGender(input["*owned_company_name"]) == 0 else "Nữ"
    else:
        fake = fakeName()
        input["*owned_company_name"] = fake.get("name")
        gender = fake.get("gender")
    input["*owned_company_gender"] = gender
    input["*owned_company_nationality"] = "Việt Nam"
    input["*owned_company_ethnicity"] = "Kinh"
    if homeAddress is None:
        homeAddress = ownedCompanyAddress
    input["*owned_company_contact_address_line1"] = homeAddress
    input["*owned_company_contact_address_line2"] = homeAddress

    registrationDate = data[dataIndex]["Ngày hoạt động"].split('/') if "Ngày hoạt động" in data[dataIndex] else None
    reassignData = fakeReassignDate(data[dataIndex]["Ngày hoạt động"].split('-')[0])
    if registrationDate is not None:
        input["*registration_date"] = f'{data[dataIndex]["Ngày hoạt động"].split('-')[2]} tháng {data[dataIndex]["Ngày hoạt động"].split('-')[1]} năm {data[dataIndex]["Ngày hoạt động"].split('-')[0]}'
    else:
        formatted_date = randomDate()
        input["*registration_date"] = f"{formatted_date[0]} tháng {formatted_date[1]} năm {formatted_date[2]}"
    if reassignData[1] is None:
        input["*reassign_date"] = f'Đăng ký thay đổi lần thứ {reassignData[0]}, ngày {input["*registration_date"]}'
    else:
        input["*reassign_date"] = f'Đăng ký thay đổi lần thứ {reassignData[0]}, {reassignData[1]}'
    if identityDate is None:
        identityDate = randomIdentityDate()
    input["*owned_company_id_issue_date"] = identityDate
    companyOwnerBirthDay = randomBirthDay()
    if birthDay is None:
        birthDay = f'Sinh ngày: {companyOwnerBirthDay}'
    input["**owned_company_birth_date"] = birthDay
    with open("place.json", "r", encoding="utf-8") as placeCode:
        places = list(filter(lambda element: element['name'].lower() == "hà nội", json.load(placeCode)))
        if identityNum is None:
            identityNum = places[0]["code"] + fakeFourthCharacter(0 if gender == "Nam" else 1) + companyOwnerBirthDay.split('/')[-1][2:-1] + ''.join(str(random.randint(0, 9)) for _ in range(6))
        input["*cccd"] = identityNum
        input["*legal_company_id_number"] = identityNum
    capitalInfo = capitals[random.randint(0, len(capitals) - 1)]
    input["*capital"] = capitalInfo["value"] + " đồng"
    input["*total_share"] = ("{:,}".format(int(capitalInfo["value"].replace(".", "")) / int(input["*share_value"]))).replace(",", ".")
    input["*share_value"] = f'{input["*share_value"]} đồng'
    input["*capital_by_text"] = capitalInfo["text"]
    input["*abbreviation_name"] = f'{data[dataIndex]["Tên viết tắt"].strip().upper() if "Tên viết tắt" in data[dataIndex] else "fake tên viết tắt"}'
    input["*name_en_line1"] = f'{data[dataIndex]["Tên quốc tế"].strip().upper() if "Tên quốc tế" in data[dataIndex] else "fake tên quốc tế"}'
    # input["*website"] = f'https://{generate_acronym(input["*abbreviation"]).lower()}.{random.choice(domains)}/'
    input["*email"] = ""
    input["**phonenumber"] = data[dataIndex]["Điện thoại"] if "Điện thoại" in data[dataIndex] else "đang tìm cách fake"
    input["*address_line"] = data[dataIndex]["Địa chỉ"]
    input["*name_vi"] = f'{data[dataIndex]["Tên công ty"].strip().upper()}'
    # Kết nối với Photoshop
    app = comtypes.client.CreateObject("Photoshop.Application", dynamic = True)
    app.Visible = True  # Hiển thị Photoshop
    # Mở file PSD
    doc = app.Open(psd_file)
    totalMarginTop = []
    position = {}

    # Lấy danh sách text layer
    for i, layer in enumerate(doc.ArtLayers):
        if layer.kind == 2:  # chỉ xử lý text layer
            totalMarginTop.append({'name': layer.Name, 'index': i, 'y': layer.Bounds[1], 'margin': 0})

    # Sắp xếp từ trên xuống (theo tọa độ Y)
    totalMarginTop.sort(key=lambda x: x['y'])
    # print(totalMarginTop)
    for order, x in enumerate(totalMarginTop):
        position[x['index']] = order

    for i, layer in enumerate(doc.ArtLayers):
        if layer.kind == 2:
            limit = 72 if 'name' in layer.Name else 78

            if layer.Name in input and layer.Name.startswith('*'):
                old_text = layer.TextItem.Contents
                old_height = layer.Bounds[3] - layer.Bounds[1]  # chiều cao cũ
                new_text = ""
                # Sinh text mới
                if layer.Name == "website":
                    new_text = f"Website: {input['*website']}"
                else:
                    if ':' in old_text:
                        prefix = old_text.split(':')[0] + ': '
                        new_text = prefix + input[layer.Name]
                    else:
                        new_text = input[layer.Name]
                print(layer.Name, new_text)
                # Nếu quá limit → xuống dòng
                if len(new_text) > limit:
                    space = None
                    if ',' in new_text:
                        space_positions = [j for j, ch in enumerate(new_text) if ch == "," and j <= limit]
                        if space_positions:
                            if new_text[space_positions[-1] + 1] == " ":
                                space = space_positions[-1] + 2
                            else:
                                space = space_positions[-1] + 1
                    else:
                        space_positions = [j for j, ch in enumerate(new_text) if ch == " " and j <= limit]
                        space = space_positions[-1] + 1 if space_positions else None

                    if space:
                        new_text = new_text[:space] + "\r" + new_text[space:]
                    
                    # Update text
                    layer.TextItem.Contents = new_text
                    new_height = layer.Bounds[3] - layer.Bounds[1]  # chiều cao mới
                    # Tính chênh lệch
                    offset = new_height - old_height
                    print(layer.Name, offset)

                    if offset != 0:
                        # Dồn offset xuống tất cả layer bên dưới
                        for j in range(position[i] + 1, len(totalMarginTop)):
                            totalMarginTop[j]['margin'] += offset + 1
                    # print([{'margin': x['margin'], 'layer': x['name']} for x in totalMarginTop])
                else:
                    layer.TextItem.Contents = new_text

    # Tạo đối tượng lưu file
    options = comtypes.client.CreateObject("Photoshop.PhotoshopSaveOptions")
    for i, layer in enumerate(doc.ArtLayers):
        if layer.kind  == 2:
            sumMargin = 0.0
            for index, x in enumerate(totalMarginTop):
                if x['index'] == i:
                    sumMargin += x['margin']
            if sumMargin != 0:
                layer.TextItem.Position = [
                layer.TextItem.Position[0],  # Giữ nguyên X
                layer.TextItem.Position[1] + sumMargin  # Dịch chuyển Y
            ]
    target_dir = os.path.join(base_dir, "corp", "hanoi")
    if not os.path.exists(target_dir):
        os.makedirs(target_dir, exist_ok=True)
    doc.saveAs(
        os.path.join(f"{target_dir}, {input['*business_code']}_{part}.psd"),
        options,
        True
    )
    if part == 2:
        name = None
        gender = None
        birthDay = None
        identityNum = None
        identityDate = None
        homeAddress = None
    doc.Close(2)

name = None
gender = None
birthDay = None
identityNum = None
identityDate = None
homeAddress = None
# Sử dụng
psd_path1 = os.path.abspath(r"D:\coding\toolPsd\20250828_Hà Nội_main.psd")

if len(data) == 0:
    print("No data")
else:
    for i in range(1):
        edit_text_layer(psd_path1, 1, i)