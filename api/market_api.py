from __future__ import annotations

from ..api_client import ApiClient
from .. import models


class MarketApi(object):
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def market_bonds_get(self, **kwargs):
        """Получение списка облигаций

        :rtype: models.MarketInstrumentListResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.market_bonds_get_with_http_info(**kwargs)

    def market_bonds_get_with_http_info(self, **kwargs):
        """Получение списка облигаций

        :rtype: models.MarketInstrumentListResponse
        """

        all_params = []
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method market_bonds_get" % key
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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        auth_settings = ['sso_auth']

        return self.api_client.call_api(
            '/market/bonds', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MarketInstrumentListResponse',
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def market_candles_get(self, figi, _from, to, interval, **kwargs):
        """Получение исторических свечей по FIGI

        :param str figi: FIGI (required)
        :param datetime.datetime _from: Начало временного промежутка (required)
        :param datetime.datetime to: Конец временного промежутка (required)
        :param models.CandleResolution interval: Интервал свечи (required)
        :rtype: models.CandlesResponse
        """
        kwargs['_return_http_data_only'] = True
        data = self.market_candles_get_with_http_info(figi, _from, to, interval, **kwargs)
        return data

    def market_candles_get_with_http_info(self, figi, _from, to, interval, **kwargs):
        """Получение исторических свечей по FIGI

        :param str figi: FIGI (required)
        :param datetime.datetime _from: Начало временного промежутка (required)
        :param datetime.datetime to: Конец временного промежутка (required)
        :param CandleResolution interval: Интервал свечи (required)
        :rtype: models.CandlesResponse
        """

        all_params = ['figi', '_from', 'to', 'interval']
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method market_candles_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'figi' is set
        if ('figi' not in params or
                params['figi'] is None):
            raise ValueError("Missing the required parameter `figi` when calling `market_candles_get`")
        # verify the required parameter '_from' is set
        if ('_from' not in params or
                params['_from'] is None):
            raise ValueError("Missing the required parameter `_from` when calling `market_candles_get`")
        # verify the required parameter 'to' is set
        if ('to' not in params or
                params['to'] is None):
            raise ValueError("Missing the required parameter `to` when calling `market_candles_get`")
        # verify the required parameter 'interval' is set
        if ('interval' not in params or
                params['interval'] is None):
            raise ValueError("Missing the required parameter `interval` when calling `market_candles_get`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'figi' in params:
            query_params.append(('figi', params['figi']))
        if '_from' in params:
            query_params.append(('from', params['_from']))
        if 'to' in params:
            query_params.append(('to', params['to']))
        if 'interval' in params:
            query_params.append(('interval', params['interval']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        auth_settings = ['sso_auth']

        return self.api_client.call_api(
            '/market/candles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CandlesResponse',
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def market_currencies_get(self, **kwargs):
        """Получение списка валютных пар

        :rtype: models.MarketInstrumentListResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.market_currencies_get_with_http_info(**kwargs)

    def market_currencies_get_with_http_info(self, **kwargs):
        """Получение списка валютных пар

        :rtype: models.MarketInstrumentListResponse
        """

        all_params = []
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method market_currencies_get" % key
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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        auth_settings = ['sso_auth']

        return self.api_client.call_api(
            '/market/currencies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MarketInstrumentListResponse',
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def market_etfs_get(self, **kwargs):
        """Получение списка ETF

        :rtype: models.MarketInstrumentListResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.market_etfs_get_with_http_info(**kwargs)

    def market_etfs_get_with_http_info(self, **kwargs):
        """Получение списка ETF

        :rtype: models.MarketInstrumentListResponse
        """

        all_params = []
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method market_etfs_get" % key
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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        auth_settings = ['sso_auth']

        return self.api_client.call_api(
            '/market/etfs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MarketInstrumentListResponse',
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def market_orderbook_get(self, figi, depth, **kwargs):
        """Получение стакана по FIGI

        :param str figi: FIGI (required)
        :param int depth: Глубина стакана [1..20] (required)
        :rtype: models.OrderbookResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.market_orderbook_get_with_http_info(figi, depth, **kwargs)

    def market_orderbook_get_with_http_info(self, figi, depth, **kwargs):
        """Получение стакана по FIGI

        :param str figi: FIGI (required)
        :param int depth: Глубина стакана [1..20] (required)
        :rtype: models.OrderbookResponse
        """

        all_params = ['figi', 'depth']
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method market_orderbook_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'figi' is set
        if ('figi' not in params or
                params['figi'] is None):
            raise ValueError("Missing the required parameter `figi` when calling `market_orderbook_get`")
        # verify the required parameter 'depth' is set
        if ('depth' not in params or
                params['depth'] is None):
            raise ValueError("Missing the required parameter `depth` when calling `market_orderbook_get`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'figi' in params:
            query_params.append(('figi', params['figi']))
        if 'depth' in params:
            query_params.append(('depth', params['depth']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        auth_settings = ['sso_auth']

        return self.api_client.call_api(
            '/market/orderbook', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OrderbookResponse',
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def market_search_by_figi_get(self, figi, **kwargs):
        """Получение инструмента по FIGI

        :param str figi: FIGI (required)
        :rtype: models.SearchMarketInstrumentResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.market_search_by_figi_get_with_http_info(figi, **kwargs)

    def market_search_by_figi_get_with_http_info(self, figi, **kwargs):
        """Получение инструмента по FIGI

        :param str figi: FIGI (required)
        :rtype: models.SearchMarketInstrumentResponse
        """

        all_params = ['figi']
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method market_search_by_figi_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'figi' is set
        if ('figi' not in params or
                params['figi'] is None):
            raise ValueError("Missing the required parameter `figi` when calling `market_search_by_figi_get`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'figi' in params:
            query_params.append(('figi', params['figi']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        auth_settings = ['sso_auth']

        return self.api_client.call_api(
            '/market/search/by-figi', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchMarketInstrumentResponse',
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def market_search_by_ticker_get(self, ticker, **kwargs):
        """Получение инструмента по тикеру

        :param str ticker: Тикер инструмента (required)
        :rtype: models.MarketInstrumentListResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.market_search_by_ticker_get_with_http_info(ticker, **kwargs)

    def market_search_by_ticker_get_with_http_info(self, ticker, **kwargs):
        """Получение инструмента по тикеру

        :param str ticker: Тикер инструмента (required)
        :rtype: models.MarketInstrumentListResponse
        """

        all_params = ['ticker']
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method market_search_by_ticker_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ticker' is set
        if ('ticker' not in params or
                params['ticker'] is None):
            raise ValueError("Missing the required parameter `ticker` when calling `market_search_by_ticker_get`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ticker' in params:
            query_params.append(('ticker', params['ticker']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        auth_settings = ['sso_auth']

        return self.api_client.call_api(
            '/market/search/by-ticker', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MarketInstrumentListResponse',
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def market_stocks_get(self, **kwargs):
        """Получение списка акций

        :rtype: models.MarketInstrumentListResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.market_stocks_get_with_http_info(**kwargs)

    def market_stocks_get_with_http_info(self, **kwargs):
        """Получение списка акций

        :rtype: models.MarketInstrumentListResponse
        """

        all_params = []
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in params['kwargs'].items():
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method market_stocks_get" % key
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
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])

        auth_settings = ['sso_auth']

        return self.api_client.call_api(
            '/market/stocks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MarketInstrumentListResponse',
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
