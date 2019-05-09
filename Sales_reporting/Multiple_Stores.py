class Store:
    sales_fig = {}

    def __init__(self, store_name):
        self.store_name = store_name


    def salesFigures(self):
        """
            input sales figure
        """
        name = input('Name : ')
        sale = int(input('Sales : '))
        self.sales_fig[name] = sale
        return

    def gen_rpt(self,option=False):

        if not option:
            for line in self.sales_fig.items():
                print(f'{line[0]}\t\t{line[1]}')
            return
        elif option:
            try:
                import csv as csv
                reader = csv.DictReader(self.sales_fig)
                with open(f'{self.store_name}.csv', 'w') as csvfile:
                    fieldnames=['Name', 'Sales']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for line in reader:
                        print(line)
                        writer.writerow(line)
                    print('''
                            --------------------------------
                                Data exported
                            --------------------------------
                          ''')
                return
            except Exception:
                print('Exception : ')
        return

class Multistore:

    def printMenu(store_name=''):
        print('\n--------------------------------')
        print('Current Store: {}'.format(store_name))
        print('1: Enter store')
        print('2: Enter sales figures')
        print('3: Generate report')
        print('4: Export CSV')
        print('Q: Quit')
        print('--------------------------------')
        return input('Enter your choice [1/2/3/4/Q] : ')

    choice = printMenu()
    store = None

    while choice in ("1", "2", "3", "4"):

        if store is None:
            choice = "1"

        if choice == "1":
            cur_store_name = input('Store : ')
            store = Store(cur_store_name)
            choice = printMenu(cur_store_name)

        elif choice == "2":
            store.salesFigures()
            choice = printMenu(cur_store_name)

        elif choice == "3":
            store.gen_rpt()
            choice = printMenu(cur_store_name)

        elif choice == "4":
            store.gen_rpt(option=True)
            choice = printMenu(cur_store_name)
