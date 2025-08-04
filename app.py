# app.py

import streamlit as st
from hachi_income.income_utils import SalaryCalculator
import hachi_income.income_utils as iu

st.title("그대는 어떻게 살 것 인가?")

# 입력받기
annual_gross = st.number_input("세전 연봉 입력(만원)", min_value=0, step=1000, value=50000000)
st.caption("입력한 금액: {}".format(iu.convert_to_korean_currency_units(annual_gross)))
deduction_rate = st.slider("공제율(% 예상)", min_value=10, max_value=20, value=15) / 100
goal_amount = st.number_input("목표 금액 입력(원)", min_value=0, step=100000, value=5000000)

# 계산
if st.button("계산하기"):
    calc = SalaryCalculator(annual_gross, deduction_rate=deduction_rate)
    st.write(f"**실수령 annual(세후):** {calc.net:,.0f}원")
    hourly, minutely, secondly = calc.calculate_time_earnings()
    st.write(f"**시간당:** {hourly:,.0f}원 / **분당:** {minutely:,.0f}원 / **초당:** {secondly:,.2f}원")
    months = calc.estimate_goal_period(goal_amount)
    st.write(f"**목표 {goal_amount:,.0f}원 달성 예상 기간:** {months:.1f}개월")

# 추가 기능/그래프는 plotly/matplotlib, st.line_chart 등으로 손쉽게 확장 가능
