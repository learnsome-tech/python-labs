# Hands-on Python: Complete Video Course & Book — lesson m13l01 — Conditions And Simple If Statements
# https://learnsome.tech/courses/python-course/watch?lesson=m13l01
# © LearnSome.tech
if balance < 0: 
    transfer = -balance 
    # transfer enough from the backup account: 
    backupAccount = backupAccount - transfer
    balance = balance + transfer
