
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto('file:///app/user_login/code.html')

        password_input = page.locator('#password')
        await password_input.fill('test-password')

        toggle_button = page.locator('[aria-label="Toggle password visibility"]')

        await toggle_button.click()

        await page.screenshot(path='/app/verification/verification.png')

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
