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