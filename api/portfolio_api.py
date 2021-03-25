from __future__ import annotations

from ..api_client import ApiClient
from .. import models


class PortfolioApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def portfolio_currencies_get(self, **kwargs):
        """Получение валютных активов клиента

        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: models.PortfolioCurrenciesResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.portfolio_currencies_get_with_http_info(**kwargs)

    def portfolio_currencies_get_with_http_info(self, **kwargs):
        """Получение валютных активов клиента

        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: models.PortfolioCurrenciesResponse
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
                    " to method portfolio_currencies_get" % key
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
            '/portfolio/currencies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PortfolioCurrenciesResponse',
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def portfolio_get(self, **kwargs):
        """Получение портфеля клиента

        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: models.PortfolioResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.portfolio_get_with_http_info(**kwargs)

    def portfolio_get_with_http_info(self, **kwargs):
        """Получение портфеля клиента

        :param str broker_account_id: Номер счета (по умолчанию - Тинькофф)
        :rtype: models.PortfolioResponse
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
                    " to method portfolio_get" % key
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
            '/portfolio', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PortfolioResponse',
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
