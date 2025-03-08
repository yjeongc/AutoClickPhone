# Minimal ADB and Fastboot 환경 설정 (Android)

## 1. ADB 환경 설정
Minimal ADB and Fastboot가 설치된 상태에서 ADB가 정상적으로 동작하는지 확인합니다.

### 1.1 ADB 활성화 및 장치 연결

#### 스마트폰에서 개발자 옵션 활성화
1. **Android 스마트폰**에서 `설정(Settings)` 앱을 엽니다.
2. `휴대전화 정보(About phone)`로 이동합니다.
3. `소프트웨어 정보(Software information)`에서 `빌드 번호(Build Number)`를 7번 연속 터치합니다.
4. 개발자 모드가 활성화되었다는 메시지가 나타납니다.
5. `설정`으로 돌아가 `개발자 옵션(Developer options)`을 엽니다.
6. `USB 디버깅(USB Debugging)`을 활성화합니다.

#### PC와 스마트폰 연결
1. **USB 케이블**을 사용하여 스마트폰을 PC에 연결합니다.
2. Minimal ADB and Fastboot 실행:
   - Windows에서 `cmd`를 열거나 `adb.exe`가 있는 폴더에서 `Minimal ADB and Fastboot`를 실행합니다.

#### ADB 장치 연결 확인
1. 명령 프롬프트(cmd)에서 아래 명령어를 실행합니다:
   ```sh
   adb devices
   ```
2. 실행 결과가 아래와 같이 나와야 합니다:
   ```
   List of devices attached
   XXXXXXXXXXXX    device
   ```
3. 만약 `unauthorized` 상태가 표시되면, 스마트폰 화면에서 **USB 디버깅 허용** 팝업이 나타납니다. `허용(Allow)`을 선택해주세요.

### 1.2 ADB 연결 문제 해결
- `adb devices` 실행 시 장치가 표시되지 않으면?
  - 스마트폰에서 `USB 디버깅`이 활성화되었는지 확인하세요.

