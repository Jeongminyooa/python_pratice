import qrcode # qrcode 생성 모듈 https://pypi.org/project/qrcode/
import re # 정규표현식 지원 모듈

def make_qr_image(myQR, qr_data):
    myQR.add_data(qr_data)
    myQR.make(fit=True)
        
    img = myQR.make_image(fill_color=(000, 102, 153), back_color=(000, 000, 000))
    print(type(img))  # qrcode.image.pil.PilImage

    # 정규식 활용해서 도메인 이름만 추출하고 그거로 이미지 파일 이름 생성
    pattern = r"^https://([^/]+)"
    filename = re.match(pattern, qr_data).group(1)
    save_path = "4.QR코드 생성기\\" + filename + ".png"
    img.save(save_path)
    
    myQR.clear()

file_path = "4.QR코드 생성기/links_for_qr.txt"
encoding = "UTF-8"

myQR = qrcode.QRCode(
                version = 1,
                error_correction = qrcode.ERROR_CORRECT_L,
                box_size=10,
                border=4,)

with open(file_path, 'r', encoding=encoding) as file:
    link_list = file.readlines()
    
    for link in link_list:
        qr_data = link.strip()
        make_qr_image(myQR, qr_data)
