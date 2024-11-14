"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501

    The version of the OpenAPI document: 2020-09-14_1.586.4
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from plaid.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from plaid.exceptions import ApiAttributeError



class InvestmentTransactionSubtype(ModelSimple):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('value',): {
            'ACCOUNT_FEE': "account fee",
            'ADJUSTMENT': "adjustment",
            'ASSIGNMENT': "assignment",
            'BUY': "buy",
            'BUY_TO_COVER': "buy to cover",
            'CONTRIBUTION': "contribution",
            'DEPOSIT': "deposit",
            'DISTRIBUTION': "distribution",
            'DIVIDEND': "dividend",
            'DIVIDEND_REINVESTMENT': "dividend reinvestment",
            'EXERCISE': "exercise",
            'EXPIRE': "expire",
            'FUND_FEE': "fund fee",
            'INTEREST': "interest",
            'INTEREST_RECEIVABLE': "interest receivable",
            'INTEREST_REINVESTMENT': "interest reinvestment",
            'LEGAL_FEE': "legal fee",
            'LOAN_PAYMENT': "loan payment",
            'LONG-TERM_CAPITAL_GAIN': "long-term capital gain",
            'LONG-TERM_CAPITAL_GAIN_REINVESTMENT': "long-term capital gain reinvestment",
            'MANAGEMENT_FEE': "management fee",
            'MARGIN_EXPENSE': "margin expense",
            'MERGER': "merger",
            'MISCELLANEOUS_FEE': "miscellaneous fee",
            'NON-QUALIFIED_DIVIDEND': "non-qualified dividend",
            'NON-RESIDENT_TAX': "non-resident tax",
            'PENDING_CREDIT': "pending credit",
            'PENDING_DEBIT': "pending debit",
            'QUALIFIED_DIVIDEND': "qualified dividend",
            'REBALANCE': "rebalance",
            'RETURN_OF_PRINCIPAL': "return of principal",
            'REQUEST': "request",
            'SELL': "sell",
            'SELL_SHORT': "sell short",
            'SEND': "send",
            'SHORT-TERM_CAPITAL_GAIN': "short-term capital gain",
            'SHORT-TERM_CAPITAL_GAIN_REINVESTMENT': "short-term capital gain reinvestment",
            'SPIN_OFF': "spin off",
            'SPLIT': "split",
            'STOCK_DISTRIBUTION': "stock distribution",
            'TAX': "tax",
            'TAX_WITHHELD': "tax withheld",
            'TRADE': "trade",
            'TRANSFER': "transfer",
            'TRANSFER_FEE': "transfer fee",
            'TRUST_FEE': "trust fee",
            'UNQUALIFIED_GAIN': "unqualified gain",
            'WITHDRAWAL': "withdrawal",
        },
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'value': (str,),
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {}

    read_only_vars = set()

    _composed_schemas = None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):
        """InvestmentTransactionSubtype - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): For descriptions of possible transaction types and subtypes, see the [Investment transaction types schema](https://plaid.com/docs/api/accounts/#investment-transaction-types-schema).., must be one of ["account fee", "adjustment", "assignment", "buy", "buy to cover", "contribution", "deposit", "distribution", "dividend", "dividend reinvestment", "exercise", "expire", "fund fee", "interest", "interest receivable", "interest reinvestment", "legal fee", "loan payment", "long-term capital gain", "long-term capital gain reinvestment", "management fee", "margin expense", "merger", "miscellaneous fee", "non-qualified dividend", "non-resident tax", "pending credit", "pending debit", "qualified dividend", "rebalance", "return of principal", "request", "sell", "sell short", "send", "short-term capital gain", "short-term capital gain reinvestment", "spin off", "split", "stock distribution", "tax", "tax withheld", "trade", "transfer", "transfer fee", "trust fee", "unqualified gain", "withdrawal", ]  # noqa: E501

        Keyword Args:
            value (str): For descriptions of possible transaction types and subtypes, see the [Investment transaction types schema](https://plaid.com/docs/api/accounts/#investment-transaction-types-schema).., must be one of ["account fee", "adjustment", "assignment", "buy", "buy to cover", "contribution", "deposit", "distribution", "dividend", "dividend reinvestment", "exercise", "expire", "fund fee", "interest", "interest receivable", "interest reinvestment", "legal fee", "loan payment", "long-term capital gain", "long-term capital gain reinvestment", "management fee", "margin expense", "merger", "miscellaneous fee", "non-qualified dividend", "non-resident tax", "pending credit", "pending debit", "qualified dividend", "rebalance", "return of principal", "request", "sell", "sell short", "send", "short-term capital gain", "short-term capital gain reinvestment", "spin off", "split", "stock distribution", "tax", "tax withheld", "trade", "transfer", "transfer fee", "trust fee", "unqualified gain", "withdrawal", ]  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):
        """InvestmentTransactionSubtype - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str): For descriptions of possible transaction types and subtypes, see the [Investment transaction types schema](https://plaid.com/docs/api/accounts/#investment-transaction-types-schema).., must be one of ["account fee", "adjustment", "assignment", "buy", "buy to cover", "contribution", "deposit", "distribution", "dividend", "dividend reinvestment", "exercise", "expire", "fund fee", "interest", "interest receivable", "interest reinvestment", "legal fee", "loan payment", "long-term capital gain", "long-term capital gain reinvestment", "management fee", "margin expense", "merger", "miscellaneous fee", "non-qualified dividend", "non-resident tax", "pending credit", "pending debit", "qualified dividend", "rebalance", "return of principal", "request", "sell", "sell short", "send", "short-term capital gain", "short-term capital gain reinvestment", "spin off", "split", "stock distribution", "tax", "tax withheld", "trade", "transfer", "transfer fee", "trust fee", "unqualified gain", "withdrawal", ]  # noqa: E501

        Keyword Args:
            value (str): For descriptions of possible transaction types and subtypes, see the [Investment transaction types schema](https://plaid.com/docs/api/accounts/#investment-transaction-types-schema).., must be one of ["account fee", "adjustment", "assignment", "buy", "buy to cover", "contribution", "deposit", "distribution", "dividend", "dividend reinvestment", "exercise", "expire", "fund fee", "interest", "interest receivable", "interest reinvestment", "legal fee", "loan payment", "long-term capital gain", "long-term capital gain reinvestment", "management fee", "margin expense", "merger", "miscellaneous fee", "non-qualified dividend", "non-resident tax", "pending credit", "pending debit", "qualified dividend", "rebalance", "return of principal", "request", "sell", "sell short", "send", "short-term capital gain", "short-term capital gain reinvestment", "spin off", "split", "stock distribution", "tax", "tax withheld", "trade", "transfer", "transfer fee", "trust fee", "unqualified gain", "withdrawal", ]  # noqa: E501
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        return self
