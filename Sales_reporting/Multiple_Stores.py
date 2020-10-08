import os
clear = lambda: os.system('cls')
class Store:
    sales_fig = {"romik": 10}

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
            a = 0
            for line in self.sales_fig.items():
                print(f'{a}\t{line[0]}\t\t{line[1]}')
                a = a + 1
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

    def deleteFigure(self, num):
        a = 0
        print(f'{num}')
        for line in self.sales_fig.items():
            if(str(a) == num):
                del self.sales_fig[line[0]]
                print('Figure Deleted Successfully.')
                return
            a = a + 1
        print('Index is invalid !!')
        return


class RemoveSalesRecored:
    store = None
    def __init__(self, store):
        self.store = store

class Multistore:

    def printMenu(store_name=''):
        print('\n--------------------------------')
        print('Current Store: {}'.format(store_name))
        print('\n--------------------------------')
        print('1: Enter store')
        print('2: Enter sales figures')
        print('3: Generate report')
        print('4: Export CSV')
        print('5: Delete sales figure')
        print('Q: Quit')
        print('--------------------------------')
        return input('Enter your choice [1/2/3/4/5/Q] : ')

    choice = printMenu()
    store = None

    while choice in ("1", "2", "3", "4", "5"):

        if store is None:
            choice = "1"

        if choice == "1":
            cur_store_name = input('Store : ')
            store = Store(cur_store_name)
            clear()

        elif choice == "2":
            store.salesFigures()

        elif choice == "3":
            store.gen_rpt()

        elif choice == "4":
            store.gen_rpt(option=True)

        elif choice == "5":
            store.gen_rpt()
            b = input('Enter your choice delete from given index : ')
            store.deleteFigure(b)

        choice = printMenu(cur_store_name)
