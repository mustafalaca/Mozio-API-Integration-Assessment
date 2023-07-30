import requests
from requests import Response

from request_parameters import Parameters
from cheapest_vehicle_with_provider import find_cheapest_from_provider


MOZIO_URL = 'Replace with the actual Mozio URL'


class Search:
    @staticmethod
    def search() -> str:
        parameters = Parameters()
        response: Response = requests.post(url=f'{MOZIO_URL}/search/',
                                           headers=parameters.request_header,
                                           json=parameters.search_object)
        return response.json().get('search_id') if response.json()['results'] != [] else False

    @staticmethod
    def search_poll(search_id: str) -> str:
        parameters = Parameters()
        response: Response = requests.get(url=f'{MOZIO_URL}/search/{search_id}/poll/',
                                          headers=parameters.request_header)
        result_id: str = find_cheapest_from_provider(response.json()['results'])
        return result_id


class Reservations:
    @staticmethod
    def reservations(search_id, result_id) -> dict:
        parameters = Parameters()
        customer_contact: dict = parameters.customer_contact

        customer_contact['search_id'] = search_id
        customer_contact['result_id'] = result_id

        response: Response = requests.post(url=f'{MOZIO_URL}/reservations/',
                                           headers=parameters.request_header,
                                           json=customer_contact)
        return response.json()

    @staticmethod
    def reservation_poll(search_id) -> Response:
        parameters = Parameters()
        response: Response = requests.get(url=f'{MOZIO_URL}/reservations/{search_id}/poll/',
                                          headers=parameters.request_header)
        return response.json()


class Cancellation:
    @staticmethod
    def cancel(reservation_id) -> int:
        parameters = Parameters()
        response: Response = requests.delete(url=f'{MOZIO_URL}/reservations/{reservation_id}/',
                                             headers=parameters.request_header)
        return response.status_code


if __name__ == "__main__":
    find_reservation = Search()
    search_id_param = find_reservation.search()
    if search_id_param is not False:
        result_id_param = find_reservation.search_poll(search_id_param)

        make_reservation = Reservations()
        complete_reservation = make_reservation.reservations(search_id_param, result_id_param)
        reservation_id_param = complete_reservation['reservations'][0].get('id')

        make_cancellation = Cancellation()
        cancel_reservation = make_cancellation.cancel(reservation_id_param)
    else:
        print("There is no result with the search object!")
