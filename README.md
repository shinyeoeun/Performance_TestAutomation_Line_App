# performance Test Lab
Android App의 성능데이터(Memory)를 수집하여 Raw Data취득 및 시각화하는 스크립트 

## About Test
메모리 변동추이 확인을 위해, 메모리 소요가 심한 In-App 카메라 촬영 시나리오로 구성

### Scenario
LINE 앱 기동 > 프로필사진 변경 > 카메라촬영 > 필터적용 > 30초간 대기 > 카메라종료 > 앱 종료

### Demo

![demo](https://user-images.githubusercontent.com/25470405/75669744-e5f80600-5cbe-11ea-8b98-4fe3069840e7.gif)


## Test Result
### Memory 사용량 그래프
카메라 실행부터 종료(18:13:05~18:13:35)까지 메모리 사용량이 증가함을 확인할수 있음

![2020-03-02_18h14_58](https://user-images.githubusercontent.com/25470405/75662022-c0b0cb00-5cb1-11ea-9a2e-c11e7329027a.png)

###  Memory 사용량 Raw Data (csv)
csv 형식으로 Raw 데이터 출력

![2020-03-02_19h20_13](https://user-images.githubusercontent.com/25470405/75667679-67e63000-5cbb-11ea-8660-c0482ae2386f.png)


* 측정값 상세

![2020-03-02_18h51_11](https://user-images.githubusercontent.com/25470405/75665046-de346380-5cb6-11ea-8823-732dfc083236.png)

※ Pss Total: 프로세스의 실제 RAM값과 다른 프로세스의 RAM사용량 및 사용가능한 전체 RAM값을 비교하기 위한 지표


## Description
1. PSS Total값을 1초간격으로 취득하는 메소드 작성
```python
def getPerformanceValue_memory(driver, sec):
    for i in range(sec):
        TIME_SEC.append(time.strftime("%H:%M:%S"))
        MEMORY_LIST = driver.get_performance_data(PACKAGE, "memoryinfo", TIME_OUT)
        MEMORY_PSS_TOTAL_VALUE = MEMORY_LIST[1]
        MEMORY_PSS_TOTAL_VALUE_LIST.append(int(MEMORY_PSS_TOTAL_VALUE[5]))
        time.sleep(1)
```
2. LINE기동 직후부터 위 메소드를 Thread로 호출한뒤 측정시간(초)을 인수로 넘김
```python
    thread_memory = Thread(target=getPerformanceValue_memory, args=(driver, 35))
    thread_memory.start()
```
3. 테스트 시나리오 수행 
4. 지정한 시간이 초과하면 Thread 종료
```python
    thread_memory.join()
```
5. 테스트 시나리오 수행 도중 수집한 RAM 값들로 그래프 작성(matplotlib pylab)
```python
    def generateGraph_memory():
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.plot(TIME_SEC, MEMORY_PSS_TOTAL_VALUE_LIST)
        ax.set_title('LINE Chat Room Memory Check(Build Ver:' + BUILD_VERSION + ')')
        ax.set_ylabel('Total PSS(KB)')
        ax.set_xlabel('TIME(sec)')
        ax.grid(True)
        plt.xticks(TIME_SEC, rotation='vertical')
        plt.show()
```
6. 마찬가지로 수집한 값으로 Raw Data작성(pandas dataframe)
```python
    def getRawDataMemory():
        raw_data = pd.DataFrame({'Time': TIME_SEC,'RAM Usage(Total PSS(KB))': MEMORY_PSS_TOTAL_VALUE_LIST}, columns=['Time', 'RAM Usage(Total PSS(KB))'])
        raw_data.to_csv("LINE_ChatRoom_memory_raw_data_" + BUILD_VERSION + ".csv", index=False)
```

※ 같은 방식으로 디바이스 배터리정보(배터리 잔량/온도)도 취득할 수 있음 <br/>


![addBattery](https://user-images.githubusercontent.com/25470405/77624041-8cfd5400-6f84-11ea-9201-2bab155abbf7.png)


## Trouble Shooting

* 데이터 시각화 관련
matplotlib 라이브러리에서 유용하게 쓴 API 정리

|API|Usage|Parameter|
|------|------|------|
|subplot|그래프 표시 위치 정의|int/int/int|행/열/인덱스|
|grid|그리드 표시|boolean|표시여부:true/false|
|legend|범례 표시|string|표시위치:upper right/upper center ...|

```python
        plt.figure(figsize=(10, 7)) # 캔버스 크기 정의
        plt.style.use(['seaborn-dark']) # 테마

        # 메모리 측정 데이터 그래프
        plt.subplot(2, 1, 1) # 그래프 표시 위치
        plt.grid() # 그리드 표시
        plt.plot(self.X_Time, self.Y_Memory, color='b', marker='o', label='memory(MB)')
        plt.ylabel("Memory")

        # 배터리 측정 데이터 그래프
        plt.subplot(2, 1, 2)
        plt.plot(self.X_Time, self.Y_Battery, color='g', marker='o', label='Device Battery')
        plt.plot(self.X_Time, self.Y_Temperature, color='y', marker='s', label='Device Temperature')
        plt.grid(False) # 그리드 표시 안함
        plt.legend(loc='upper right') # 범례 표시
        plt.xlabel("Time")
        plt.ylabel("Value")
```


## Directory Structure
![2020-03-02_18h40_59](https://user-images.githubusercontent.com/25470405/75667991-e93dc280-5cbb-11ea-83b2-c6ac683c4efd.png)

## Usage
1. Appium 서버 기동
2. 스크립트 실행 
```sh
pytest -n 1 LINE_PerformanceCheck_Android.py
```
* 테스트 디바이스가 복수개일 경우 -n 뒤의 Argument를 수정
3. 자동으로 생성되는 그래프 확인
4. 필요할 경우 Raw Data(.csv) 확인(프로젝트 디렉토리에 생성)


## Reference

* Performance Testing of Android Apps
> https://appiumpro.com/editions/5

* Capturing Performance Data for Native iOS Apps
> https://appiumpro.com/editions/12

* Android 'dumpsys'도구를 이용한 모바일 앱 성능 테스트
> https://blog.naver.com/wisestone2007/221321329618

* 파이썬 멀티 쓰레드(thread)와 멀티 프로세스(process)
> https://monkey3199.github.io/develop/python/2018/12/04/python-pararrel.html
