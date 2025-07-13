import os
import time

# 클릭 함수
def tap(x, y):
    os.system(f"adb shell input tap {x} {y}")
    time.sleep(0.3)

# 슬라이딩 함수
def swipe(x1, y1, x2, y2, duration=300):
    os.system(f"adb shell input swipe {x1} {y1} {x2} {y2} {duration}")
    time.sleep(0.5)

# 클릭 및 슬라이드 좌표
tap_coords = [
    (1260, 2580),  # 1번 클릭 위치
    (717, 1850)   # 2번 클릭 위치
]
swipe_coords = [
    (867, 1328),  # 슬라이드 시작점
    (440, 1326)    # 슬라이드 끝점
]


while True:
    try:
        num_pages = int(input("책은 몇 장인가요오? "))
        if num_pages > 0:
            break
        else:
            print("1 이상의 숫자를 입력하세요.")
    except ValueError:
        print("유효한 숫자를 입력하세요.")


for i in range(num_pages):
    print(f"[{i+1}/{num_pages}] 실행 중...")
    
    # 1번 클릭
    tap(*tap_coords[0])

    # 2번 클릭
    tap(*tap_coords[1])

    # 3번 슬라이드
    swipe(*swipe_coords[0], *swipe_coords[1])

print("작업 완료!")
