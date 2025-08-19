# app.py
# python -m streamlit run app.py

import streamlit as st
from hachi_income.income_utils import SalaryCalculator
import hachi_income.income_utils as iu

st.title("그대는 어떻게 살 것 인가?")

st.sidebar.title("어떻게 한달을 살 것인가?")
st.sidebar.header("나는 얼마만큼 여유로운가?")
st.sidebar.subheader("월급/수입/지출을 반영하여 하루/이번 주/이번 달 얼만큼의 금액을 사용 가능한지 알아보자.")
st.sidebar.write('상세 노동 조건 :', "주당 출근 날짜, 평균 노동시간, 평균 점심 시간, 평균 출퇴근 시간 등 조정 가능")
st.sidebar.write('상세 노동 조건 :', "기본 값 하루 노동 시간 8시간, 점심시간 1시간, 주 5일 노동.")
st.sidebar.write('수입/지출 관리:', "수입/지출 내용을 추가할 수 있고, 통계 부분의 지출/사용 가능한 돈에 영향을 미침.")

# 세션 스테이트 초기화
if "income" not in st.session_state:
    st.session_state.income = 0.0
if 'additional_incomes' not in st.session_state:
    st.session_state.additional_incomes = []
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# 입력받기
income_input = st.number_input("그대의 세후 월급/소득(만원)", min_value=0, step=10, value=300)
st.caption("그대의 한달 월급 : {}".format(iu.convert_to_korean_currency_units(income_input)))
if income_input != st.session_state.income:
    st.session_state.income = income_input

# 숨겨진 상세 정보 (expander 사용)
with st.expander("상세 노동 조건", expanded=False):
    choice = st.radio(
        "주당 출근 날짜",
        ("1일", "2일", "3일", "4일", "5일", "6일", "7일"),
        horizontal=True, # 가로 정렬 옵션
        index = 4
    )

    avg_work_time = st.number_input("평균 노동 시간(시간)", value=8, min_value=0, step=1, max_value=24)
    avg_lunch_time = st.number_input("평균 점심 시간(분)", value=60, min_value=0, step=1, max_value=600)
    avg_commute_time = st.number_input("평균 츨퇴근 시간(분)", value=60, min_value=0, step=1, max_value=600)


with st.expander("수입/지출 관리", expanded=False):
    # st.header("항목별 입력")
    with st.form('add_transaction', clear_on_submit=True):
        trans_type = st.radio('이 항목은?', ['지출', '수입'])
        name = st.text_input('항목명 (예: 알바, 월세, 용돈 등)')
        amount = st.number_input('금액 (만원)', min_value=0.0, step=1.0)
        submitted = st.form_submit_button('항목 추가')
        if submitted and name:
            if trans_type == '수입':
                st.session_state.additional_incomes.append({'id' : iu.get_random_id(), 'name': name, 'amount': amount})
                st.success(f'수입 항목 추가됨: {name} - {amount:,.1f} 만원')
            else:
                st.session_state.expenses.append({'id' : iu.get_random_id(), 'name': name, 'amount': amount})
                st.success(f'지출 항목 추가됨: {name} - {amount:,.1f} 만원')

# 수입내역 보여주기(+삭제 버튼)
st.header("수입 내역")
add_income_sum = sum(item['amount'] for item in st.session_state.additional_incomes)
st.write(f"- 세후 월급 : {st.session_state.income:,.1f} 만원")

for i, item in enumerate(st.session_state.additional_incomes):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write(f"- {item['name']}: {item['amount']:,.1f} 만원")
    with col2:
        print(i, item)
        if st.button(f"삭제 - {item.get('name', '')}", key=item.get('id')):
            del st.session_state.additional_incomes[i]
            st.rerun()

# 지출내역 보여주기(+삭제 버튼)
st.header("지출 내역")
expense_sum = sum(item['amount'] for item in st.session_state.expenses)

for i, item in enumerate(st.session_state.expenses):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write(f"- {item['name']}: {item['amount']:,.1f} 만원")
    with col2:
        print(i, item)
        if st.button(f"삭제 - {item.get('name', '')}", key=item.get('id')):
            del st.session_state.expenses[i]
            st.rerun()

st.header("이번 달 남은 금액")
total_income = st.session_state.income + add_income_sum
leftover = total_income - expense_sum
st.metric("남은 금액", f"{leftover:,.1f} 만원")

st.header("통계")
salary, rate = iu.estimate_gross_salary_auto(income_input * 10000)
st.write(f"- 추정 연봉(세전) : {salary :,.0f}원 (공제율: {rate*100:.1f}%)")
st.write(f"- 주급(세후) : {income_input * 10000/4.345 :,.0f}원 (한달 약 {4.345}주)")

# 한달에 4.345주임.

# 일주일에 일하는 날짜
work_day_per_week = int(choice.replace("일", ""))
work_day_per_month = work_day_per_week * 4.345
print("work_day_per_week ::", work_day_per_week)
print("work_day_per_month ::", work_day_per_month)

real_day_income = income_input * 10000 / work_day_per_month
# 365/12 = 30.4166666667
comm_day_income = income_input * 10000 / 30.416

real_hour_income = real_day_income / avg_work_time
comm_hour_income = comm_day_income / 24

real_minute_income = real_day_income / avg_work_time / 60
comm_minute_income = comm_day_income / 24 / 60

real_second_income = real_day_income / avg_work_time / 60 / 60
comm_second_income = comm_day_income / 24 / 60 / 60

comm_day_expense = expense_sum * 10000 / 30.416

leftover_day = leftover * 10000 / 30.416

st.write(f"- 실 근무일 일당(세후) : {real_day_income :,.0f}원 (한달 약 {work_day_per_month:,.1f}일)")
st.write(f"- 통상 일당(세후) : {comm_day_income :,.0f}원(한달 약 {30:,.0f}일)")

st.write(f"- 실 근무일 시급(세후) : {real_hour_income :,.0f}원 (한달 약 {work_day_per_month * avg_work_time:,.0f}시간)")
st.write(f"- 통상 시급(세후) : {comm_hour_income :,.0f}원(한달 약 {30*24:,.0f}시간)")

st.write(f"- 실 근무일 분급(세후) : {real_minute_income :,.0f}원 (한달 약 {work_day_per_month * avg_work_time * 60:,.0f}분)")
st.write(f"- 통상 분급(세후) : {comm_minute_income :,.0f}원(한달 약 {30*24*60:,.0f}분)")

st.write(f"- 실 근무일 초급(세후) : {real_second_income :,.1f}원 (한달 약 {work_day_per_month * avg_work_time * 60*60:,.0f}초)")
st.write(f"- 통상 초급(세후) : {comm_second_income :,.2f}원(한달 약 {30*24*60*60:,.0f}초)")

st.write(f"- 숨만 쉬어도 하루 지출 : {comm_day_expense :,.2f}원")
st.write(f"- 하루에 써도 되는 돈 : {leftover_day :,.2f}원")



