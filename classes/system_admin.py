class SystemAdmin:
    tota_transactions=0
    @classmethod
    def update_transactions_count(cls,amount:int=1) -> None:
        cls.tota_transactions+=1
    @classmethod
    def report_stats(cls)->None:
        print(cls.tota_transactions)
        print(Library.max_borrow_days)

