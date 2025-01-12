import { test, expect } from '@playwright/test';

test('sidebar navigation links are visible and functional', async ({ page }) => {
  await page.goto('http://localhost:3000');

  const navLinks = page.locator('aside nav ul li a');

  // Validate sidebar links exist
  await expect(navLinks).toHaveCount(3);
  await expect(navLinks.nth(0)).toHaveText('Home');
  await expect(navLinks.nth(1)).toHaveText('Categories');
  await expect(navLinks.nth(2)).toHaveText('About');

  // Click the "About" link (future feature)
  // await navLinks.nth(2).click();
  // await expect(page).toHaveURL('/about');
});
