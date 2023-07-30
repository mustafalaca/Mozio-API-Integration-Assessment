from dataclasses import dataclass


@dataclass
class Parameters:
    request_header = {"API-KEY": "Replace with the validated API KEY",
                      "Content-Type": "application/json",
                      "Accept": "*/*",
                      "Connection": "keep-alive",
                      "Accept-Encoding": "gzip, deflate, br"}

    search_object = {
        "start_address": "44 Tehama Street, San Francisco, CA, USA",
        "end_address": "SFO",
        "mode": "one_way",
        "pickup_datetime": "2023-12-01 15:30",
        "num_passengers": 2,
        "currency": "USD",
        "campaign": "Mustafa Alaca"
    }

    customer_contact = {
        "email": "mustafalaca@hotmail.com",
        "phone_number": "+905068303587",
        "country_code_name": "US",
        "first_name": "Mustafa",
        "last_name": "Alaca",
        "airline": "AA",
        "flight_number": "123"
    }
