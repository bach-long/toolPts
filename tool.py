import comtypes.client
import json
import os
from datetime import datetime
from datetime import timedelta
import random
import re
import string
import nltk
from nltk.corpus import stopwords

data = []
with open(os.path.abspath("hanoi/ha-noi-7-7.json"), "r", encoding="utf-8") as file:
    data = json.load(file)  # Chuyển nội dung file thành Python dictionary 
    data = list(filter(lambda element: "tnhh" in element['Tên công ty'].lower() and "Điện thoại" in element and "Tên viết tắt" in element and "Tên quốc tế" in element, data))

def guessGender(name):
    splitName = name.split(' ')
    lastName = splitName[-1].lower()
    middleName = splitName[-2].lower()
    with open("names.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        malePoint = data["male"]["lastName"].get(lastName, 0) + data["male"]["middleName"].get(middleName, 0) * 2
        femalePoint = data["female"]["lastName"].get(lastName, 0) + data["female"]["middleName"].get(middleName, 0) * 2
    return 0 if malePoint >= femalePoint else 1

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

custom_blacklist = {
    "co",
    "co.",
    "co.,"
    "company",
    "ltd",
    "ltd.",
    "inc",
    "inc.",
    "llc",
    "group",
    "&",
}
stop_words = set(stopwords.words("english")).union(custom_blacklist)
def generate_acronym(text):
# Loại bỏ dấu câu và chuyển về chữ thường
    clean_text = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = clean_text.split()

    # Loại bỏ các từ nằm trong stop_words
    filtered = [word for word in words if word not in stop_words]

    # Tạo chữ cái đầu từ các từ còn lại
    acronym = "".join(word[0].upper() for word in filtered)
    return acronym

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
    # Ngày 6 tháng trước
    six_months_ago = today - timedelta(days=6*30)
    # Ngày 2 năm trước
    two_years_ago = today - timedelta(days=2*365)
    # Random số ngày trong khoảng từ 6 tháng đến 2 năm
    random_days = random.randint(0, (six_months_ago - two_years_ago).days)
    # Tính toán ngày ngẫu nhiên
    random_date = two_years_ago + timedelta(days=random_days)
    # Định dạng lại ngày theo định dạng DD/MM/YYYY
    formatted_date = random_date.strftime("%d/%m/%Y").split('/')
    return f"ngày {formatted_date[0]} tháng {formatted_date[1]} năm {formatted_date[2]}"

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
    domains = ['electricstock.io.vn', 'giaydepnhanh.io.vn', 'noithat3d.io.vn', 'smartrent.id.vn', 'thoitrangnhanh.io.vn']
    input = {}
    capitals = [
        [
  { "value": "542.207.610.000", "text": "542 tỷ 207 triệu 610 nghìn đồng" },
  { "value": "564.028.826.000", "text": "564 tỷ 28 triệu 826 nghìn đồng" },
  { "value": "493.612.533.000", "text": "493 tỷ 612 triệu 533 nghìn đồng" },
  { "value": "433.938.449.000", "text": "433 tỷ 938 triệu 449 nghìn đồng" },
  { "value": "560.657.872.000", "text": "560 tỷ 657 triệu 872 nghìn đồng" },
  { "value": "467.035.402.000", "text": "467 tỷ 35 triệu 402 nghìn đồng" },
  { "value": "400.155.954.000", "text": "400 tỷ 155 triệu 954 nghìn đồng" },
  { "value": "515.696.650.000", "text": "515 tỷ 696 triệu 650 nghìn đồng" },
  { "value": "503.529.120.000", "text": "503 tỷ 529 triệu 120 nghìn đồng" },
  { "value": "543.233.760.000", "text": "543 tỷ 233 triệu 760 nghìn đồng" },
  { "value": "573.910.873.000", "text": "573 tỷ 910 triệu 873 nghìn đồng" },
  { "value": "485.809.287.000", "text": "485 tỷ 809 triệu 287 nghìn đồng" },
  { "value": "503.290.090.000", "text": "503 tỷ 290 triệu 90 nghìn đồng" },
  { "value": "488.498.148.000", "text": "488 tỷ 498 triệu 148 nghìn đồng" },
  { "value": "527.222.407.000", "text": "527 tỷ 222 triệu 407 nghìn đồng" },
  { "value": "512.958.992.000", "text": "512 tỷ 958 triệu 992 nghìn đồng" },
  { "value": "582.842.240.000", "text": "582 tỷ 842 triệu 240 nghìn đồng" },
  { "value": "513.850.237.000", "text": "513 tỷ 850 triệu 237 nghìn đồng" },
  { "value": "515.507.416.000", "text": "515 tỷ 507 triệu 416 nghìn đồng" },
  { "value": "572.294.625.000", "text": "572 tỷ 294 triệu 625 nghìn đồng" }
]

    ]
    input["business_code"] = data[dataIndex]["Mã số thuế"]
    print(data[dataIndex]["Mã số thuế"])
    ownedCompanyAddress = ''
    with open("vn_addresses.json", "r", encoding="utf-8") as file:
        addresses = json.load(file)
        ownedCompanyAddress = random.choice([item for item in addresses if "Hà Nội" in item.get("full_address", "")])['full_address']
    if "Người đại diện" in data[dataIndex]:
        input["owned_company_name"] = data[dataIndex]["Người đại diện"].upper()
        if gender is None:
            gender = "Nam" if guessGender(input["owned_company_name"]) == 0 else "Nữ"
    else:
        fake = fakeName()
        input["owned_company_name"] = fake.get("name")
        gender = fake.get("gender")
    input["owned_company_gender"] = gender
    input["owned_company_nationality"] = "Việt Nam"
    input["owned_company_ethnicity"] = "Kinh"
    if homeAddress is None:
        homeAddress = ownedCompanyAddress
    input["owned_company_contact_address_line1"] = homeAddress
    input["owned_company_contact_address_line2"] = homeAddress
    registrationDate = data[dataIndex]["Ngày hoạt động"].split('/') if "Ngày hoạt động" in data[dataIndex] else None
    input["registration_date"] = f'ngày {data[dataIndex]["Ngày hoạt động"].split('-')[2]} tháng {data[dataIndex]["Ngày hoạt động"].split('-')[1]} năm {data[dataIndex]["Ngày hoạt động"].split('-')[0]}'if registrationDate is not None else randomDate()
    if identityDate is None:
        identityDate = randomIdentityDate()
    input["owned_company_id_issue_date"] = identityDate
    companyOwnerBirthDay = randomBirthDay()
    if birthDay is None:
        birthDay = companyOwnerBirthDay
    input["owned_company_birth_date"] = birthDay if part == 1 else "     " + birthDay
    with open("place.json", "r", encoding="utf-8") as placeCode:
        places = list(filter(lambda element: element['name'].lower() == "hà nội", json.load(placeCode)))
        if identityNum is None:
            identityNum = places[0]["code"] + fakeFourthCharacter(0 if gender == "Nam" else 1) + companyOwnerBirthDay.split('/')[-1][2:-1] + ''.join(str(random.randint(0, 9)) for _ in range(6))
        input["cccd"] = identityNum
        input["legal_company_id_number"] = identityNum
    capitalInfo = capitals[random.randint(0, len(capitals) - 1)]
    input["capital"] = capitalInfo["value"] + " đồng"
    input["capital_by_text"] = capitalInfo["text"]
    input["abbreviation"] = data[dataIndex]["Tên viết tắt"].strip().upper() if "Tên viết tắt" in data[dataIndex] else "fake tên viết tắt"
    input["name_en_line1"] = data[dataIndex]["Tên quốc tế"].strip().upper() if "Tên quốc tế" in data[dataIndex] else "fake tên quốc tế"
    input["website"] = f'https://{generate_acronym(input["abbreviation"]).lower()}.{random.choice(domains)}/'
    input["email"] = ""
    input["phone"] = data[dataIndex]["Điện thoại"] if "Điện thoại" in data[dataIndex] else "đang tìm cách fake"
    input["address_line"] = data[dataIndex]["Địa chỉ"]
    input["name_vi"] = data[dataIndex]["Tên công ty"].strip().upper()
    
    # Kết nối với Photoshop
    app = comtypes.client.CreateObject("Photoshop.Application", dynamic = True)
    app.Visible = True  # Hiển thị Photoshop

    # Mở file PSD
    doc = app.Open(psd_file)
    totalMarginTop = []
    position = {}
    for i, layer in enumerate(doc.LayerSets["Group 1"].ArtLayers):
        if layer.kind  == 2:
            totalMarginTop.append({'index': i, 'y': layer.Bounds[1], 'margin': 0})
    
    totalMarginTop.sort(key=lambda x: x['y'])
    for i, x in enumerate(totalMarginTop):
        position[x['index']] = i

    for i, layer in enumerate(doc.LayerSets["Group 1"].ArtLayers):
        if layer.kind  == 2:
            #print(f"🔹 Layer Name: {layer.Name} | {layer.TextItem.Contents}")
            limit = 72 if 'name' in layer.Name or layer.Name == 'abbreviation' else 78
            if layer.Name in input:
                if layer.Name == "website":
                    layer.TextItem.Contents = f"Website: {input["website"]}"
                else:
                    notOneLine = '\r' in layer.TextItem.Contents
                    layer.TextItem.Contents = layer.TextItem.Contents.split(':')[0] + ': ' + input[layer.Name] if ': ' in layer.TextItem.Contents else input[layer.Name]
                    if len(layer.TextItem.Contents) > limit:
                        space = None
                        space_positions = []
                        if ',' in layer.TextItem.Contents and limit != 72:
                            space_positions = [i for i, char in enumerate(layer.TextItem.Contents) if char == "," and i <= limit]
                            space = space_positions[-1]
                        else:
                            space_positions = [i for i, char in enumerate(layer.TextItem.Contents) if char == " " and i <= limit]
                            space = space_positions[-1] + 1
                        layer.TextItem.Contents = layer.TextItem.Contents[0:space] + "\r" + layer.TextItem.Contents[space:]
                         # Tính toán tổng margin top (cập nhật lại sau khi chỉnh sửa nội dung)
                        if not notOneLine:
                            totalMarginTop[position[i]]['margin'] = (layer.Bounds[3] - layer.Bounds[1]) / 2
                        #print("total margin", layer.Bounds)
                    else:
                        if notOneLine and '\r' not in layer.TextItem.Contents:
                            totalMarginTop[position[i]]['margin'] = -1 * (layer.Bounds[3] - layer.Bounds[1])
    # Tạo đối tượng lưu file
    options = comtypes.client.CreateObject("Photoshop.PhotoshopSaveOptions")
    for i, layer in enumerate(doc.LayerSets["Group 1"].ArtLayers):
        if layer.kind  == 2:
            sumMargin = 0.0
            for index, x in enumerate(totalMarginTop):
                if x['index'] == i:
                    break
                else:
                    sumMargin += x['margin']
            if sumMargin != 0:
                layer.TextItem.Position = [
                layer.TextItem.Position[0],  # Giữ nguyên X
                layer.TextItem.Position[1] + sumMargin  # Dịch chuyển Y
            ]
    if not os.path.exists(f"D://coding//toolPsd//fake//hanoi//{input["business_code"]}"):
        os.makedirs(f"D://coding//toolPsd//fake//hanoi//{input["business_code"]}", exist_ok=True)
    doc.saveAs(f"D://coding//toolPsd//fake//hanoi//{input["business_code"]}//{input["business_code"]}_{part}.psd", options, True)
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
psd_path1 = os.path.abspath("sample//reg_hn_1.psd")
psd_path2 = os.path.abspath("sample//reg_hn_2.psd")  # Đổi thành đường dẫn file PSD của bạn

if len(data) == 0:
    print("No data")
else:
    for i in range(len(data)):
        edit_text_layer(psd_path1, 1, i)
        edit_text_layer(psd_path2, 2, i)