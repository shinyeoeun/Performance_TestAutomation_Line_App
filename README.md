# performance Test Lab
Android App의 성능데이터(Memory)를 수집하여 Raw Data 취득 및 시각화하는 스크립트 

## 테스트 시나리오
* 메모리 변동추이를 확인하기 위해, 메모리 소요가 심한 카메라 촬영 + 스티커 적용시의 시나리오로 구성함
* 상세 시나리오는 아래 참조

1. LINE App launch
2. Home탭에서 프로필 탭
3. 프로필 사진 변경버튼 탭
4. 카메라 메뉴 탭
5. 임의의 스티커 적용
6. 20초 대기
7. Back버튼으로 카메라 종료
8. 5초 대기

## 테스트 결과
![2020-03-02_18h14_58](https://user-images.githubusercontent.com/25470405/75662022-c0b0cb00-5cb1-11ea-9a2e-c11e7329027a.png)
* 카메라 기동후 20초간 메모리가 증가하였다가 카메라가 종료된 뒤 5초간 다시 정상화 

## 파일 구조
![2020-03-02_18h40_59](https://user-images.githubusercontent.com/25470405/75664463-dd4f0200-5cb5-11ea-9df8-61e57508c27a.png)

## 사용 예제
1. Appium 서버 기동
2. 스크립트 실행 
```sh
pytest -n 1 LINE_PerformanceCheck_Android.py
```
* 테스트 디바이스가 복수개일 경우 -n 뒤의 Argument를 수정
3. 자동으로 생성되는 그래프 확인
4. 필요할 경우 Raw Data(.csv) 확인(프로젝트 디렉토리에 생성)


## 참고자료
https://appiumpro.com/editions/5
