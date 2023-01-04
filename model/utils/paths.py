from selene.support.shared import browser
import os
import tests


# rel_path = 'resources/more.jpg'
# def path_to_image(rel_path):
#    full_path = os.path.abspath(
#        os.path.join(os.path.dirname(tests.__file__), rel_path)
#    )
#
#    return full_path


def path_to_image(selector, rel_path):
    browser.element(selector).set_value(
        os.path.abspath(
        os.path.join(os.path.dirname(tests.__file__), rel_path)
        )
    )
