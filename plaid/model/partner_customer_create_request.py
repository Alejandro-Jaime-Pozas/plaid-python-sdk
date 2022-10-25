"""
    The Plaid API

    The Plaid REST API. Please see https://plaid.com/docs/api for more details.  # noqa: E501
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
)

def lazy_import():
    from plaid.model.partner_end_customer_address import PartnerEndCustomerAddress
    from plaid.model.partner_end_customer_billing_contact import PartnerEndCustomerBillingContact
    from plaid.model.partner_end_customer_technical_contact import PartnerEndCustomerTechnicalContact
    from plaid.model.products import Products
    globals()['PartnerEndCustomerAddress'] = PartnerEndCustomerAddress
    globals()['PartnerEndCustomerBillingContact'] = PartnerEndCustomerBillingContact
    globals()['PartnerEndCustomerTechnicalContact'] = PartnerEndCustomerTechnicalContact
    globals()['Products'] = Products


class PartnerCustomerCreateRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
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
        lazy_import()
        return {
            'company_name': (str,),  # noqa: E501
            'is_diligence_attested': (bool,),  # noqa: E501
            'products': ([Products],),  # noqa: E501
            'legal_entity_name': (str,),  # noqa: E501
            'website': (str,),  # noqa: E501
            'application_name': (str,),  # noqa: E501
            'address': (PartnerEndCustomerAddress,),  # noqa: E501
            'is_bank_addendum_completed': (bool,),  # noqa: E501
            'client_id': (str,),  # noqa: E501
            'secret': (str,),  # noqa: E501
            'create_link_customization': (bool,),  # noqa: E501
            'logo': (str,),  # noqa: E501
            'technical_contact': (PartnerEndCustomerTechnicalContact,),  # noqa: E501
            'billing_contact': (PartnerEndCustomerBillingContact,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'company_name': 'company_name',  # noqa: E501
        'is_diligence_attested': 'is_diligence_attested',  # noqa: E501
        'products': 'products',  # noqa: E501
        'legal_entity_name': 'legal_entity_name',  # noqa: E501
        'website': 'website',  # noqa: E501
        'application_name': 'application_name',  # noqa: E501
        'address': 'address',  # noqa: E501
        'is_bank_addendum_completed': 'is_bank_addendum_completed',  # noqa: E501
        'client_id': 'client_id',  # noqa: E501
        'secret': 'secret',  # noqa: E501
        'create_link_customization': 'create_link_customization',  # noqa: E501
        'logo': 'logo',  # noqa: E501
        'technical_contact': 'technical_contact',  # noqa: E501
        'billing_contact': 'billing_contact',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, company_name, is_diligence_attested, products, legal_entity_name, website, application_name, address, is_bank_addendum_completed, *args, **kwargs):  # noqa: E501
        """PartnerCustomerCreateRequest - a model defined in OpenAPI

        Args:
            company_name (str): The company name of the end customer being created.
            is_diligence_attested (bool): Denotes whether or not the partner has completed attestation of diligence for the end customer to be created.
            products ([Products]): The products to be enabled for the end customer.
            legal_entity_name (str): The end customer's legal name.
            website (str): The end customer's website.
            application_name (str): The name of the end customer's application.
            address (PartnerEndCustomerAddress):
            is_bank_addendum_completed (bool): Denotes whether the partner has forwarded the Plaid bank addendum to the end customer.

        Keyword Args:
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
            client_id (str): Your Plaid API `client_id`. The `client_id` is required and may be provided either in the `PLAID-CLIENT-ID` header or as part of a request body.. [optional]  # noqa: E501
            secret (str): Your Plaid API `secret`. The `secret` is required and may be provided either in the `PLAID-SECRET` header or as part of a request body.. [optional]  # noqa: E501
            create_link_customization (bool): If true, the end customer's default Link customization will be set to match the partner's.. [optional]  # noqa: E501
            logo (str): Base64-encoded representation of the end customer's logo. Must be a PNG of size 1024x1024 under 4MB. Defaults to the partner's logo if omitted.. [optional]  # noqa: E501
            technical_contact (PartnerEndCustomerTechnicalContact): [optional]  # noqa: E501
            billing_contact (PartnerEndCustomerBillingContact): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
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

        self.company_name = company_name
        self.is_diligence_attested = is_diligence_attested
        self.products = products
        self.legal_entity_name = legal_entity_name
        self.website = website
        self.application_name = application_name
        self.address = address
        self.is_bank_addendum_completed = is_bank_addendum_completed
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
