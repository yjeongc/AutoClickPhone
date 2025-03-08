from PIL import Image
import os

# 이미지 폴더 경로
image_folder = r"C:\Workspace\Pictures"

# 사용자에게 PDF 파일명 입력받기 (기본값: output.pdf)
pdf_filename = input("저장할 PDF 파일명을 입력하세요 (확장자 제외, 입력 안 할 시 기본값: output): ").strip()
if not pdf_filename:
    pdf_filename = "output"  # 기본 파일명 설정
output_pdf_path = os.path.join(image_folder, f"{pdf_filename}.pdf")

# 이미지 파일 목록 가져오기 (시간순 정렬)
image_files = sorted(
    [f for f in os.listdir(image_folder) if f.lower().endswith(("png", "jpg", "jpeg"))],
    key=lambda f: os.path.getmtime(os.path.join(image_folder, f))
)

# 이미지 파일 로드
images = [Image.open(os.path.join(image_folder, file)).convert("RGB") for file in image_files]

# PDF로 저장
if images:
    images[0].save(output_pdf_path, save_all=True, append_images=images[1:])
    print(f"PDF 저장 완료: {output_pdf_path}")
else:
    print("변환할 이미지가 없습니다.")
