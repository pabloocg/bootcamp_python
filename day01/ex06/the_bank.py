class Account(object):
    ID_COUNT = 1
    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if not hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

    def fixBattribute(self):
        for attr in self.__dict__:
            if attr.startswith('b'):
                val = self.__dict__[attr]
                del self.__dict__[attr]
                setattr(self, attr.lstrip('b'), val)

    def fixZipAttribute(self):
        correct = False
        for attr in self.__dict__:
            if attr.startswith('zip') or attr.startswith('addr'):
                correct = True
        if not correct:
            self.zip = None

    def fixEvenAttribute(self):
        if not hasattr(self, 'zip'):
            self.zip = None
        elif not hasattr(self, 'addr'):
            self.addr = None

    def __str__(self):
        return f"Accound id -> {self.id}\nAccount name -> {self.name}\nAccount value -> {self.value}"

class Bank(object):
    """The bank"""

    def __init__(self):
        self.account = []

    def add(self, account: Account):
        if isinstance(account, Account):
            self.account.append(account)
        else:
            exit("add argument must be Account object.")

    def isCorrupted(self, acc: Account) -> bool:
        '''Return True if the accound argument pass is corrupted.'''
        if (len(acc.__dict__) % 2) == 0 or not hasattr(acc, 'name') or not hasattr(acc, 'id') or not hasattr(acc, 'value'):
            return True
        for attr in acc.__dict__:
            if attr.startswith('b'):
                return True
        correct = False
        for attr in acc.__dict__:
            if attr.startswith('zip') or attr.startswith('addr'):
                correct = True
        if not correct:
            return True
        return False

    def getAccountById(self, idAcc: int) -> Account:
        for acc in self.account:
            if acc.id == idAcc:
                return acc
        return None

    def getAccountByName(self, nameAcc: str) -> Account:
        for acc in self.account:
            if acc.name == nameAcc:
                return acc
        return None

    def withdrawAccount(self, acc: Account, amount: float) -> bool:
        if acc.value - amount < 0:
            return False
        acc.value -= amount
        return True

    def DepositAccount(self, acc: Account, amount: float) -> bool:
        acc.value += amount
        return True

    def transfer(self, origin: int or str, dest: int or str, amount: float) -> bool:
        """
            @origin: int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return         True if success, False if an error occured
        """
        if isinstance(origin, int):
            originAcc = self.getAccountById(origin)
        elif isinstance(origin, str):
            originAcc = self.getAccountByName(origin)
        if isinstance(dest, int):
            destAcc = self.getAccountById(dest)
        elif isinstance(dest, str):
            destAcc = self.getAccountByName(dest)
        print(originAcc)
        print(destAcc)
        if not originAcc or not destAcc or self.isCorrupted(originAcc) or self.isCorrupted(destAcc) or not self.withdrawAccount(originAcc, amount):
            return False
        self.DepositAccount(destAcc, amount)
        print(originAcc)
        print(destAcc)
        return True


    def fix_account(self, account: int or str) -> bool:
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        """
        if isinstance(account, int):
            acc = self.getAccountById(account)
        elif isinstance(account, str):
            acc = self.getAccountByName(account)
        if self.isCorrupted(acc):
            if not hasattr(acc, 'name'):
                acc.name = None
            elif not hasattr(acc, 'id'):
                acc.id = acc.ID_COUNT
            elif not hasattr(acc, 'value'):
                acc.value = 0
            acc.fixBattribute()
            acc.fixZipAttribute()
            if (len(acc.__dict__) % 2) == 0:
                acc.fixEvenAttribute()
            return (True if self.isCorrupted(acc) else False)
        else:
            return True