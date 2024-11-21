import os
import subprocess

def run_behave_tests():
    result = subprocess.run(["behave"], cwd=os.path.join(os.path.dirname(__file__), "..", "features"))
    return result.returncode

if __name__ == "__main__":
    exit_code = run_behave_tests()
    exit(exit_code)


# allure serve allure-results
