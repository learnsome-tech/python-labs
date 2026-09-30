if balance < 0: 
    transfer = -balance 
    # transfer enough from the backup account: 
    backupAccount = backupAccount - transfer
    balance = balance + transfer
