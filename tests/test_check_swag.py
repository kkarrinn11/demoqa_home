from pages.swag_labs import SwagLabs


def test_check_icon(browser):
    saucedemo = SwagLabs(browser)
    saucedemo.visit()
    assert saucedemo.exist_name_box ()
    assert saucedemo.exist_icon()
    assert saucedemo.exist_password_box ()