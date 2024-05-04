from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
 
URL = "https://hq.qashier.com/#/login?redirect=/customer-management"
 
def main():
    print("APP START")
    # browser = webdriver.Firefox()
    # options = webdriver.ChromeOptions()
    
    
    download_dir = "/tmp/selenium"  # Specify your download path here
    
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,  # To automatically save files without asking
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
        
    })
 



    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

    driver.get(URL)
    driver.implicitly_wait(20)
    inputs = driver.find_elements(By.TAG_NAME,"input")
    user_name = inputs[0]
    password = inputs[1]
    print("Input log/pass")
    time.sleep(2)

    user_name.send_keys("")
    password.send_keys("")

    button = driver.find_element(By.TAG_NAME,"button")
    button.click()
    print("Click submit done")
    # Wait until the specific element is available and clickable
    element = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))
    button2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='block' and contains(text(), 'Export')]")))


    # inside
    all_button = driver.find_elements(By.TAG_NAME,"button")
    print (f"LEN all_button {len(all_button)}")

    button_export = [i for i in all_button if i.accessible_name == 'EXPORT'][0]
    button_export.click()

    print("Click export DONE")
    # confirm
    all_button_confirm = driver.find_elements(By.TAG_NAME,"button")
    confirm_export = [i for i in all_button_confirm if i.accessible_name == 'CONFIRM'][0]
    confirm_export.click()

    time.sleep(5)
    print("Click Confirm DONE ")
    print("APP END")


if __name__=="__main__":
    main()
