from dataclasses import dataclass
@dataclass(frozen=False, order=True)
class Invoice:

    
       
    invoice_id: int
    user_id:int
    amount:float
    paid:bool
    def get_info(self):
         return f"{self.invoice_id} {self.user_id} {self.amount} {self.paid}"
    