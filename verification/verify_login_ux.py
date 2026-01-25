
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto('file:///app/user_login/code.html')
            password_input = page.locator('#password')
            toggle_button = page.locator('#toggle-password-visibility')

            await password_input.fill('s3cuReP@ssw0rd!')

            # Screenshot before toggle
            await page.screenshot(path='user_login/password_hidden.png')

            await toggle_button.click()

            # Screenshot after toggle
            await page.screenshot(path='user_login/password_visible.png')

            print("Verification script ran successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
