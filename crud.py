from models import TransactionCreate, TransactionOut, BlockCreate,BlockOut
from storage import transactions
import random
from datetime import datetime
import hashlib

def create_transaction(transantion: TransactionCreate):
    new_t = {
        "id":random.randint(10**4,10**6),
        "timestamp": datetime.now()
        }
    new_t.update(transantion.model_dump())
    
    transactions.append(TransactionOut(**new_t))
    return new_t

def get_transactions():
    return transactions

def create_blocks(block:BlockCreate):
    hash = hashlib.sha256(str(block.model_dump()).encode()).hexdigest()[:8]
    new_b = {
        "id":random.randint(10**7,10**9),
        "hash":f"hash_{hash}",
        "timestamp":datetime.now(),
        "is_mined":False
    }
    new_b.update(block.model_dump())
    return new_b


# b1 = BlockCreate(previous_hash="", transactions_id=[62743478923,34346345,23452346], miner="Майнер тест")
# b1_full = create_blocks(b1)
# b2 = BlockCreate(previous_hash=b1_full["hash"], transactions_id=[62743478923,34346345,23452346], miner="Майнер тест")
# b2_full = create_blocks(b2)
