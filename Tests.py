from Locators_Page import SearchHelper

def test(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()
    main_page.click_sign_in_section()
    main_page.enter_word_email("seleniumisgood@mail.com")
    main_page.enter_word_pass("123456")
    main_page.click_on_the_auth_button()
    elements = main_page.check_error_message()
    assert len(elements) > 0

