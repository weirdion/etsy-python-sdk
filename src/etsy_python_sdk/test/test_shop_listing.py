# coding: utf-8

"""
    Etsy Open API v3

    <div class=\"wt-text-body-01\"><p class=\"wt-pt-xs-2 wt-pb-xs-2\">Etsy's Open API provides a simple RESTful interface for various Etsy.com features. The API endpoints are meant to replace Etsy's Open API v2, which is scheduled to end service in 2022.</p><p class=\"wt-pb-xs-2\">All of the endpoints are callable and the majority of the API endpoints are now in a beta phase. This means we do not expect to make any breaking changes before our general release. A handful of endpoints are currently interface stubs (labeled “Feedback Only”) and returns a \"501 Not Implemented\" response code when called.</p><p class=\"wt-pb-xs-2\">If you'd like to report an issue or provide feedback on the API design, <a target=\"_blank\" class=\"wt-text-link wt-p-xs-0\" href=\"https://github.com/etsy/open-api/discussions\">please add an issue in Github</a>.</p></div>&copy; 2021-2025 Etsy, Inc. All Rights Reserved. Use of this code is subject to Etsy's <a class='wt-text-link wt-p-xs-0' target='_blank' href='https://www.etsy.com/legal/api'>API Developer Terms of Use</a>.

    The version of the OpenAPI document: 3.0.0
    Contact: developers@etsy.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from etsy_python_sdk.models.shop_listing import ShopListing

class TestShopListing(unittest.TestCase):
    """ShopListing unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ShopListing:
        """Test ShopListing
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ShopListing`
        """
        model = ShopListing()
        if include_optional:
            return ShopListing(
                listing_id = 1,
                user_id = 1,
                shop_id = 1,
                title = '',
                description = '',
                state = 'active',
                creation_timestamp = 946684800,
                created_timestamp = 946684800,
                ending_timestamp = 946684800,
                original_creation_timestamp = 946684800,
                last_modified_timestamp = 946684800,
                updated_timestamp = 946684800,
                state_timestamp = 946684800,
                quantity = 0,
                shop_section_id = 1,
                featured_rank = 56,
                url = '',
                num_favorers = 0,
                non_taxable = True,
                is_taxable = True,
                is_customizable = True,
                is_personalizable = True,
                personalization_is_required = True,
                personalization_char_count_max = 56,
                personalization_instructions = '',
                listing_type = 'physical',
                tags = [
                    ''
                    ],
                materials = [
                    ''
                    ],
                shipping_profile_id = 1,
                return_policy_id = 1,
                processing_min = 0,
                processing_max = 0,
                who_made = 'i_did',
                when_made = 'made_to_order',
                is_supply = True,
                item_weight = 1.337,
                item_weight_unit = 'oz',
                item_length = 1.337,
                item_width = 1.337,
                item_height = 1.337,
                item_dimensions_unit = 'in',
                is_private = True,
                style = [
                    ''
                    ],
                file_data = '',
                has_variations = True,
                should_auto_renew = True,
                language = '',
                price = etsy_python_sdk.models.money.Money(
                    amount = 56, 
                    divisor = 0, 
                    currency_code = '', ),
                taxonomy_id = 56
            )
        else:
            return ShopListing(
        )
        """

    def testShopListing(self):
        """Test ShopListing"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
