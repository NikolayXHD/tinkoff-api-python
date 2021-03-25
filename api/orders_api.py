from __future__ import annotations

from ..api_client import ApiClient
from .. import models


class OrdersApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def orders_cancel_post(self, order_id, **kwargs):
        """Отмена заявки

        :param str order_id: ID заявки (required)
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.orders_cancel_post_with_http_info(order_id, **kwargs)

    def orders_cancel_post_with_http_info(self, order_id, **kwargs):
        """Отмена заявки

        :param str order_id: ID заявки (required)
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: None
        """

        all_params = ['order_id', 'broker_account_id']
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method orders_cancel_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params or
                params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `orders_cancel_post`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order_id' in params:
            query_params.append(('orderId', params['order_id']))
        if 'broker_account_id' in params:
            query_params.append(('brokerAccountId', params['broker_account_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        auth_settings = ['sso_auth']

        return self.api_client.call_api(
            '/orders/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Empty',
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def orders_get(self, **kwargs):
        """Получение списка активных заявок

        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: models.OrdersResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.orders_get_with_http_info(**kwargs)

    def orders_get_with_http_info(self, **kwargs):
        """Получение списка активных заявок

        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: models.OrdersResponse
        """

        all_params = ['broker_account_id']
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method orders_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'broker_account_id' in params:
            query_params.append(('brokerAccountId', params['broker_account_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        auth_settings = ['sso_auth']

        return self.api_client.call_api(
            '/orders', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrdersResponse',
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def orders_limit_order_post(self, body, figi, **kwargs):
        """Создание лимитной заявки

        :param models.LimitOrderRequest body: (required)
        :param str figi: FIGI инструмента (required)
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: models.LimitOrderResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.orders_limit_order_post_with_http_info(body, figi, **kwargs)

    def orders_limit_order_post_with_http_info(self, body, figi, **kwargs):
        """Создание лимитной заявки

        :param models.LimitOrderRequest body: (required)
        :param str figi: FIGI инструмента (required)
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: models.LimitOrderResponse
        """

        all_params = ['body', 'figi', 'broker_account_id']
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method orders_limit_order_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `orders_limit_order_post`")
        # verify the required parameter 'figi' is set
        if ('figi' not in params or
                params['figi'] is None):
            raise ValueError("Missing the required parameter `figi` when calling `orders_limit_order_post`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'figi' in params:
            query_params.append(('figi', params['figi']))
        if 'broker_account_id' in params:
            query_params.append(('brokerAccountId', params['broker_account_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        auth_settings = ['sso_auth']

        return self.api_client.call_api(
            '/orders/limit-order', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LimitOrderResponse',
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def orders_market_order_post(self, body, figi, **kwargs):
        """Создание рыночной заявки

        :param models.MarketOrderRequest body: (required)
        :param str figi: FIGI инструмента (required)
        :param str broker_account_id: Уникальный идентификатор счета (по умолчанию - Тинькофф)
        :rtype: models.MarketOrderResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.orders_market_order_post_with_http_info(body, figi, **kwargs)

    def orders_market_order_post_with_http_info(self, body, figi, **kwargs):
        """Создание рыночной заявки

        :param models.MarketOrderRequest body: (required)
        :param str figi: FIGI инструмента (required)
        :param str broker_account_id: Уникальный идентификатор счета (по умолчанию - Тинькофф)
        :rtype: models.MarketOrderResponse
        """

        all_params = ['body', 'figi', 'broker_account_id']
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method orders_market_order_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `orders_market_order_post`")
        # verify the required parameter 'figi' is set
        if ('figi' not in params or
                params['figi'] is None):
            raise ValueError("Missing the required parameter `figi` when calling `orders_market_order_post`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'figi' in params:
            query_params.append(('figi', params['figi']))
        if 'broker_account_id' in params:
            query_params.append(('brokerAccountId', params['broker_account_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json'])

        auth_settings = ['sso_auth']

        return self.api_client.call_api(
            '/orders/market-order', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MarketOrderResponse',
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
