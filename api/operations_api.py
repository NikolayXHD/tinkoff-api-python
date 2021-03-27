from __future__ import annotations

from ..api_client import ApiClient
from .. import models


class OperationsApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def operations_get(self, _from, to, **kwargs):
        """Получение списка операций

        :param datetime.datetime _from: Начало временного промежутка (required)
        :param datetime.datetime to: Конец временного промежутка (required)
        :param str figi: Figi инструмента для фильтрации
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: models.OperationsResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.operations_get_with_http_info(_from, to, **kwargs)

    def operations_get_with_http_info(self, _from, to, **kwargs):
        """Получение списка операций

        :param datetime.datetime _from: Начало временного промежутка (required)
        :param datetime.datetime to: Конец временного промежутка (required)
        :param str figi: Figi инструмента для фильтрации
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: models.OperationsResponse
        """

        all_params = ['_from', 'to', 'figi', 'broker_account_id']
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    ' to method operations_get' % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter '_from' is set
        if '_from' not in params or params['_from'] is None:
            raise ValueError(
                'Missing the required parameter `_from` when calling `operations_get`'
            )
        # verify the required parameter 'to' is set
        if 'to' not in params or params['to'] is None:
            raise ValueError(
                'Missing the required parameter `to` when calling `operations_get`'
            )

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))
        if 'to' in params:
            query_params.append(('to', params['to']))
        if 'figi' in params:
            query_params.append(('figi', params['figi']))
        if 'broker_account_id' in params:
            query_params.append(
                ('brokerAccountId', params['broker_account_id'])
            )

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json']
        )

        auth_settings = ['sso_auth']

        return self.api_client.call_api(
            '/operations',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OperationsResponse',
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
        )
