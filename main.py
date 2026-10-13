from playwright.sync_api import sync_playwright

def get_temp_mail():
    with sync_playwright() as p:
        # headless=False hilft beim Debuggen, falls Sie den Browser live sehen wollen
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        print("Öffne temp-mail.org...")
        page.goto("https://temp-mail.org/de/")
        
        # Warten, bis die Adresse generiert wurde (enthält ein @)
        print("Warte auf E-Mail-Adresse...")
        page.wait_for_function('document.querySelector("#mail").value && document.querySelector("#mail").value.includes("@")', timeout=15000)
        
        # Wert auslesen
        email_address = page.locator("#mail").get_attribute("value")
        print(f"Erfolgreich ausgelesen! E-Mail: {email_address}")
        
        browser.close()
        return email_address

if __name__ == "__main__":
    get_temp_mail()
