import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def delete_expense(self):
        if not self.expenses:
            print("삭제할 지출 내역이 없습니다.\n")
            return
        self.list_expenses()
        try:
            choice = int(input("삭제할 지출의 번호를 입력하세요: "))
            if 0 < choice <= len(self.expenses): #1에서 최대까지.
                deleted_expense = self.expenses.pop(choice - 1) #1을 입력하면 리스트에서 0인덱스 삭제해야함.
                print(f"'{deleted_expense.description}' 지출이 삭제되었습니다.\n")
            else:
                print("잘못된 번호입니다. 지출 목록에 있는 번호를 입력해주세요.\n")
        except ValueError:
            print("유효하지 않은 입력입니다. 숫자를 입력해주세요.\n")
        except Exception as e:
            print(f"오류 발생: {e}\n")


    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")


