# # from random import sample, randint, choice
# from faker import Faker
#
# from showtimes.models import Cinema
#
# faker = Faker("pl_PL")
#
#
# def fake_cinema_data():
#     """Generate a dict of cineman data"""
#     cinema_data = {
#         "name": f"{faker.user_name()}",
#         "city": faker.city(),
#     }
#     return cinema_data
#
# def create_fake_cinema():
#     """Generate new fake movie and save to database."""
#     cinema_data = fake_cinema_data()
#     Cinema.objects.create(**cinema_data)
