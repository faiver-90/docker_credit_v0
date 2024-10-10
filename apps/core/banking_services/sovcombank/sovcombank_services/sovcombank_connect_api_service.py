import json


class SovcombankConnectionsService:
    def connect_api(self):
        connect = ''
        print('Connect with api')
        return connect


class SovcombankRequestService:
    def __init__(self):
        self.sovcombank_connections_service = SovcombankConnectionsService()

    def send_request(self, request):
        connect_api = self.sovcombank_connections_service.connect_api()
        print('send request', json.dumps(request, indent=4, ensure_ascii=False))
        response = {'status': 'ok', 'status_code': 200, 'id': 1234}
        print('response', json.dumps(response, indent=4, ensure_ascii=False))

        return response
