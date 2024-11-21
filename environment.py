import os
import subprocess

def after_all(context):
    # Quit the driver if it exists
    if hasattr(context, 'driver'):
        context.driver.quit()

    # Directory where allure results are stored
    allure_results_dir = os.path.join(os.getcwd(), 'allure-results')

    # Command to generate allure report
    generate_command = f'allure generate {allure_results_dir} -o allure-report --clean'
    serve_command = f'allure serve {allure_results_dir}'

    try:
        # Execute the command to generate the report
        generate_result = subprocess.run(generate_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Allure report generated successfully.")
        print(generate_result.stdout.decode())

        # Execute the command to serve the report
        serve_result = subprocess.run(serve_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Allure report served successfully.")
        print(serve_result.stdout.decode())

    except subprocess.CalledProcessError as e:
        print(f"Failed to generate or serve Allure report: {e}")
        print(e.stdout.decode())
        print(e.stderr.decode())
