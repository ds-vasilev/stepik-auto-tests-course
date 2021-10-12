import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('page', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_correct_in_answer(browser, page):
    link = "https://stepik.org/lesson/{}/step/1".format(page)
    browser.get(link)
    
    #неявное ожидание
    browser.implicitly_wait(5)

    answer = math.log(int(time.time()))
    browser.find_element_by_css_selector("[class='ember-text-area ember-view textarea string-quiz__textarea']").send_keys(str(answer))

    browser.implicitly_wait(5)

    browser.find_element_by_class_name("submit-submission").click()

    browser.implicitly_wait(5)

    corr_text = browser.find_element_by_class_name('smart-hints__hint').text
    assert corr_text == "Correct!", "Fail: {}".format(corr_text	)