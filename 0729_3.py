from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    # 추상 매서드
    @abstractmethod
    def authenticate(self):
        pass

    # 추상 매서드
    @abstractmethod
    def process_payment(self, amount):
        pass

    def payment_summary(self, amount):
        print(f"{amount} 원 결제가 완료 되었습니다.")

class CreditCard(PaymentSystem):
    def authenticate(self):
        print(f"신용카드 인증 완료")
    def process_payment(self, amount):
        print(f"신용카드로 {amount}원 결제 합니다.")

print("=============== abstractmethod ================")
creit_card = CreditCard()
creit_card.authenticate()
creit_card.process_payment(3000)
creit_card.payment_summary(5000) 