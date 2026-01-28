
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("file:///app/user_login/code.html")

        # Type into the password field to have something to see
        await page.locator("#password").type("mysecretpassword")

        # Click the toggle button
        await page.locator("#toggle-password-visibility").click()

        # Take a screenshot
        await page.screenshot(path="verification/verification.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
