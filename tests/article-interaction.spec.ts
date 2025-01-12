import { test, expect } from '@playwright/test';

test('clicking an article opens it in a new tab', async ({ page, context }) => {
  await page.goto('http://localhost:3000');

  // Listen for a new tab to open
  const [newPage] = await Promise.all([
    context.waitForEvent('page'),
    page.locator('[data-tid="articleLink"]').first().click(),
  ]);

  // Verify the new page URL is correct
  await expect(newPage).toHaveURL(/http/);
});
