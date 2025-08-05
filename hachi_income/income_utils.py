# hachisalary/salary_utils.py

class SalaryCalculator:
    def __init__(self, annual_gross, deduction_rate=0.15):
        self.gross = annual_gross
        self.deduction_rate = deduction_rate
        self.net = self.gross * (1 - self.deduction_rate)

    def calculate_time_earnings(self):
        """ 월~금 하루 근무 8시간 가정시 1년 근무 시간."""
        hours_per_year = 2080
        hourly = self.gross / hours_per_year
        minutely = hourly / 60
        secondly = minutely / 60
        return hourly, minutely, secondly

    def estimate_goal_period(self, goal_amount):
        monthly = self.net / 12
        return goal_amount / monthly if monthly > 0 else float('inf')


def convert_to_korean_currency_units(amount):
    """
    숫자(amount)를 '억'과 '만원' 단위로 변환하는 함수
    예: 115430000 -> '1억 1543만원'
    """
    eok = amount // 100_00  # 억 단위
    man = (amount % 100_00)  # 만원 단위
    result = ""
    if eok > 0:
        result += f"{eok}억 "
    if man > 0 or eok == 0:
        result += f"{man}만원"
    return result.strip()


def estimate_gross_salary_auto(net_monthly_income):
    """
    세후 월소득 기준으로 공제율을 추정하여 세전 연봉을 계산합니다.
    공제율은 대략적인 세후 기준에 따라 자동 설정됩니다.

    :param net_monthly_income: 세후 월소득 (원 단위)
    :return: 세전 연봉 추정값 (원 단위)
    """
    # 간단한 공제율 추정 로직 (현실적으로 근사치)
    if net_monthly_income < 2500000:
        rate = 0.10  # 초봉, 공제율 낮음
    elif net_monthly_income < 4000000:
        rate = 0.12  # 중간
    elif net_monthly_income < 6000000:
        rate = 0.15  # 고소득
    else:
        rate = 0.20  # 고연봉

    gross_annual_salary = (net_monthly_income * 12) / (1 - rate)
    return round(gross_annual_salary), rate