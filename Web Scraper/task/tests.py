import requests
from hstest.check_result import CheckResult
from hstest.stage_test import StageTest
from hstest.test_case import TestCase


class WebScraperTest(StageTest):
    def generate(self):
        return [TestCase(stdin="https://www.ikea.com/404",
                         check_function=self.check_not_200,
                         attach="https://www.ikea.com/404", time_limit=0),
                TestCase(stdin="http://httpstat.us/403",
                         check_function=self.check_not_200,
                         attach="http://httpstat.us/403", time_limit=0),
                TestCase(
                    stdin='http://www.pythonchallenge.com/pc/def/0.html',
                    check_function=self.check_200,
                    attach="http://www.pythonchallenge.com/pc/def/0.html", time_limit=0)]

    def check_200(self, reply, attach):
        try:
            test_content = requests.get(attach).content
        except Exception:
            return CheckResult.wrong("An error occurred when tests tried to connect to the Internet page.\n"
                                     "Please, try again.")
        try:
            with open("source.html", "rb") as f:
                file_content = f.read()
                if file_content == test_content:
                    return CheckResult.correct() if "Content saved" in reply and "The URL returned" not in reply \
                        else CheckResult.wrong("Did you notify the user you've saved the content?")
                else:
                    return CheckResult.wrong("The content of the file is not correct!")
        except FileNotFoundError:
            return CheckResult.wrong("Couldn't find the source.html file")

    def check_not_200(self, reply, attach):
        try:
            status_code = requests.get(attach).status_code
        except Exception:
            return CheckResult.wrong("An error occurred when tests tried to connect to the Internet page.\n"
                                     "Please, try again.")
        if f"The URL returned" in reply and "Content saved" not in reply:
            if str(status_code) in reply:
                return CheckResult.correct()
            else:
                return CheckResult.wrong("The returned error doesn't match with the output message.")
        else:
            return CheckResult.wrong("The link returned an error, but your program didn't.")


if __name__ == '__main__':
    WebScraperTest().run_tests()
