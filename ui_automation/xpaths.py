paths = {
    'login_paths' : {
        'username' : '//*[@id="username"]',
        'password' : '//*[@id="password"]',
        'button' : '//*[@data-test="LoginForm-log-in-button"]'
    },
    'navigation_paths' : {
        "product_cards" : '//*[@data-test="ProductCard-product-content"]',
        "account" : "//*[@aria-label='Account'][@class='pointer link darkness db-m dn']",
        "profile_name" : "//*[@data-test='ProfileForm-name']",
        "address_tab" : "//*[@href='/account/addresses']",
        "address_card" : "//*[@data-test='AddressesContainer-addressCard']",
        "add_address" : "//*[@data-test='plus-icon']",
        "address_autocomplete" : "//*[@id='AddressForm-autocomplete']",
        "auto_complete_option" : "//*[@class='pac-item'][1]",
        "street" : "//*[@id='adr-street1']",
        "city" : "//*[@id='adr-city']",
        "state" : "//*[@id='adr-state']",
        "zip" : "//*[@id='adr-zip']",
        "address_save" : "//*[@data-test='AddressForm-submit-button']",
        "new_address_card" : "//*[@data-test='StreetAddress-street'][text()='4832 Keith Dr']",
        "delete_address" : '//*[@aria-label="Delete Address: 4832 Keith Dr, Birmingham, AL 35242"]',
        "modal_delete" : "//*[@class='tr']//*[text()='Delete']"
    }
}
