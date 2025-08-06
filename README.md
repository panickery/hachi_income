# hachi_income

**수입/지출 데이터를 입력하면 연/월/일 단위로 실근무 및 통상임금을 계산해주는 웹 애플리케이션**

---

## 주요 기능

- 수입/지출 내역 입력 및 관리
- 연, 월, 일별 실근무 임금과 통상임금 계산
- 사용자 친화적인 인터페이스 제공
- 동일한 이름의 수입/지출 항목 입력 시 오류 발생 문제 인지
- 기본적인 출퇴근 시간 연동 및 임금산출 기능 구현

---

## 개선 및 수정 예정 사항

- 내용이 길어질 때 버튼이 2줄 이상으로 표시되는 UI 문제 해결
- 페이지 새로고침 시 입력 데이터가 초기화되는 문제 개선 필요
- 출퇴근 시간 적용 방식 명확화 및 기능 보완
- 동일한 이름 입력 시 발생하는 오류 수정
- 기능별 코드 정리 및 리팩토링

---

## 사용 기술

- Python
- Streamlit
- 기타 라이브러리 (requirements.txt 참고)

---

## 설치 및 실행 방법

1. 저장소 클론

    ```
    git clone https://github.com/panickery/hachi_income.git
    cd hachi_income
    ```

2. 의존성 설치

    ```
    pip install -r requirements.txt
    ```

3. 애플리케이션 실행

    ```
    streamlit run app.py
    ```

4. 웹 브라우저에서 `http://localhost:8501` 접속해 사용

---

## 배포 링크

[https://panickery-hachi-income-app-cvzzhv.streamlit.app/](https://panickery-hachi-income-app-cvzzhv.streamlit.app/)

---

## 문의 및 기여

- 기능 개선 및 버그 제보는 GitHub 이슈로 부탁드립니다.
- 추가 기능 제안도 언제든 환영합니다.
