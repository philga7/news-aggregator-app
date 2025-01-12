import { test, expect, devices } from '@playwright/test';

// Test on iPhone 12
test.use({ ...devices['iPhone 12'] });

test('mobile view displays correctly', async ({ page }) => {
  await page.goto('http://localhost:3000');

  // Sidebar should be hidden on mobile
  await expect(page.locator('aside')).toBeHidden();

  // Hamburger menu should exist (if implemented later)
  // await expect(page.locator('[data-tid="hamburgerMenu"]')).toBeVisible();
});
