from __future__ import annotations

import enum


class OperationTypeWithCommission(enum.Enum):
    BUY = "Buy"
    BUYCARD = "BuyCard"
    SELL = "Sell"
    BROKERCOMMISSION = "BrokerCommission"
    EXCHANGECOMMISSION = "ExchangeCommission"
    SERVICECOMMISSION = "ServiceCommission"
    MARGINCOMMISSION = "MarginCommission"
    OTHERCOMMISSION = "OtherCommission"
    PAYIN = "PayIn"
    PAYOUT = "PayOut"
    TAX = "Tax"
    TAXLUCRE = "TaxLucre"
    TAXDIVIDEND = "TaxDividend"
    TAXCOUPON = "TaxCoupon"
    TAXBACK = "TaxBack"
    REPAYMENT = "Repayment"
    PARTREPAYMENT = "PartRepayment"
    COUPON = "Coupon"
    DIVIDEND = "Dividend"
    SECURITYIN = "SecurityIn"
    SECURITYOUT = "SecurityOut"
