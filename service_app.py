from nosql import mongo_setup as mongo_setup
from nosql.cvi import Cvi
from nosql.job import Job

# from nosql.engine import Engine
# from nosql.servicehistory import ServiceHistory



def main():
    print_header()
    config_mongo()
    # update_doc_versions()
    user_loop()


# noinspection PyProtectedMember
# def update_doc_versions():
#     for car in Car.objects():
#         car._mark_as_changed('vi_number')
#         car.save()


def print_header():
    print('----------------------------------------------')
    print('|                                             |')
    print('|       GOODWOOD CV MANAGER v.02              |')
    print('|             demo edition                    |')
    print('|                                             |')
    print('----------------------------------------------')
    print()


def config_mongo():
    mongo_setup.global_init()


def user_loop():
    while True:
        print("Available actions:")
        print(" * [a]dd cvi")
        print(" * [l]ist cvis")
        print(" * add [j]ob")
        print(" * e[x]it")
        print()

        choices = input("> ").strip().lower()
        if choices == 'a':
            add_cvi()
        elif choices == 'l':
            list_cvis()
        elif choices == 'j':
            add_job()

        elif not choices or choices == 'x':
            print("Goodbye")
            break


def add_cvi():
    title = input("What is the model? ")
    ref =   input("What is the make? ")

    cvi = Cvi()
    cvi.title = title
    cvi.ref = ref

    # engine = Engine()
    # engine.horsepower = 590
    # engine.mpg = 22
    # engine.liters = 4.0

    # car.engine = engine

    cvi.save()


def list_cvis():
    cvis = Cvi.objects().order_by("title")
    for cvi in cvis:
        print("{} (Ref: {})".format(cvi.title, cvi.ref))
        print("Jobs listed for ".format(len(cvi.jobs)))
        for j in cvi.jobs:
            print("All jobs for this Cvi".format(j.job, j.line))
    print()

def find_car():
    print("TODO: find_car")
    print()


def add_job():
    ref = input("What is the REF of the car to service? ")
    cvi = Cvi.objects(ref=ref).first()
    if not cvi:
        print("Cvi with REF {} not found!".format(ref))
        return

    task = Job()
    task.job = input("Job Description")
    task.line = input("what line number? ")


    cvi.jobs.append(task)
    cvi.save()

    # vin = input("What is the VIN of the car to service? ")
    # service = ServiceHistory()
    # service.price = float(input("What is the price? "))
    # service.description = input("What type of service is this? ")
    # service.customer_rating = int(input("How happy is our customer? [1-5] "))
    #
    # updated = Car.objects(vi_number=vin).update_one(push__service_history=service)
    # if updated == 0:
    #     print("Car with VIN {} not found!".format(vin))
    #     return


def show_poorly_serviced_cars():
    level = int(input("What max level of satisfaction are we looking for? [1-5] "))
    # { "service_history.customer_rating": {$lte: level} }
    cars = Car.objects(service_history__customer_rating__lte=level)
    for car in cars:
        print("{} -- {} with vin {} (year {})".format(
            car.make, car.model, car.vi_number, car.year))
        print("{} of service records".format(len(car.service_history)))
        for s in car.service_history:
            print("  * Satisfaction: {} ${:,.0f} {}".format(
                s.customer_rating, s.price, s.description))
    print()


if __name__ == '__main__':
    main()
