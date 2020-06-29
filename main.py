import salary
import people
import datetime


if __name__ == '__main__':
    accouting = salary.salary * people.people
    print(f'На {people.people} сотрудников начислено {accouting} рублей, {datetime.datetime.today()}.')


