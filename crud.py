from models import TransactionCreate, TransactionOut
from storage import transactions
import random
from datetime import datetime

def create_transaction(transantion: TransactionCreate):
    new_t = {
        "id":random.randint(10**4,10**6),
        "timestamp": datetime.now().isoformat()
        }
    new_t.update(transantion.model_dump())
    
    transactions.append(TransactionOut(**new_t))
    return new_t
