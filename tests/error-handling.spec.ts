import { test, expect } from '@playwright/test';

test('displays articles or shows error if feed fails', async ({ page }) => {
  // Visit the homepage under normal conditions
  await page.goto('http://localhost:3000');

  // Locate the article links
  const articles = page.locator('[data-tid="articleLink"]');

  // Check if articles are loaded or an error message is shown
  if (await articles.count() > 0) {
    // ✅ Articles loaded successfully
    await expect(articles.first()).toBeVisible();
  } else {
    // ❌ Articles failed to load, check for the error message
    await expect(page.locator('text=Failed to load articles. Please try again.')).toBeVisible();
  }
});
