from __future__ import annotations

from ..api_client import ApiClient
from .. import models


class SandboxApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def sandbox_clear_post(self, **kwargs):
        """Удаление всех позиций

        Удаление всех позиций клиента
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.sandbox_clear_post_with_http_info(**kwargs)

    def sandbox_clear_post_with_http_info(self, **kwargs):
        """Удаление всех позиций

        Удаление всех позиций клиента
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: None
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
                    " to method sandbox_clear_post" % key
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
            '/sandbox/clear', 'POST',
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

    def sandbox_currencies_balance_post(self, body, **kwargs):
        """Выставление баланса по валютным позициям

        :param models.SandboxSetCurrencyBalanceRequest body: Запрос на выставление баланса по валютным позициям (required)
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.sandbox_currencies_balance_post_with_http_info(body, **kwargs)

    def sandbox_currencies_balance_post_with_http_info(self, body, **kwargs):
        """Выставление баланса по валютным позициям

        :param models.SandboxSetCurrencyBalanceRequest body: Запрос на выставление баланса по валютным позициям (required)
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: None
        """

        all_params = ['body', 'broker_account_id']
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sandbox_currencies_balance_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `sandbox_currencies_balance_post`")

        collection_formats = {}

        path_params = {}

        query_params = []
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
            '/sandbox/currencies/balance', 'POST',
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

    def sandbox_positions_balance_post(self, body, **kwargs):
        """Выставление баланса по инструментным позициям

        :param models.SandboxSetPositionBalanceRequest body: Запрос на выставление
               баланса по инструментным позициям (required)
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.sandbox_positions_balance_post_with_http_info(body, **kwargs)

    def sandbox_positions_balance_post_with_http_info(self, body, **kwargs):
        """Выставление баланса по инструментным позициям

        :param models.SandboxSetPositionBalanceRequest body: Запрос на выставление
               баланса по инструментным позициям (required)
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: None
        """

        all_params = ['body', 'broker_account_id']
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sandbox_positions_balance_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `sandbox_positions_balance_post`")

        collection_formats = {}

        path_params = {}

        query_params = []
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
            '/sandbox/positions/balance', 'POST',
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

    def sandbox_register_post(self, **kwargs):
        """Регистрация клиента в sandbox

        Создание счета и валютных позиций для клиента
        :param models.SandboxRegisterRequest body: Запрос на создание счета и
               выставление баланса по валютным позициям
        :rtype: models.SandboxRegisterResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.sandbox_register_post_with_http_info(**kwargs)

    def sandbox_register_post_with_http_info(self, **kwargs):
        """Регистрация клиента в sandbox

        Создание счета и валютных позиций для клиента
        :param models.SandboxRegisterRequest body: Запрос на создание счета и
               выставление баланса по валютным позициям
        :rtype: models.SandboxRegisterResponse
        """

        all_params = ['body']
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sandbox_register_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/sandbox/register', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SandboxRegisterResponse',
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sandbox_remove_post(self, **kwargs):
        """Удаление счета

        Удаление счета клиента
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.sandbox_remove_post_with_http_info(**kwargs)

    def sandbox_remove_post_with_http_info(self, **kwargs):
        """Удаление счета

        Удаление счета клиента
        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: None
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
                    " to method sandbox_remove_post" % key
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
            '/sandbox/remove', 'POST',
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
