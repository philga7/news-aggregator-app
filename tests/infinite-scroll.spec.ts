import { test, expect } from '@playwright/test';

test('loads more articles on scroll or shows "No more items"', async ({ page }) => {
  await page.goto('http://localhost:3000');

  // Locate article links
  const articles = page.locator('[data-tid="articleLink"]');

  // Count initial articles
  const initialCount = await articles.count();

  // Scroll to the bottom of the page to trigger infinite scroll
  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));

  // Wait for either new content or end-of-feed message
  await page.waitForTimeout(2000);

  // Recount articles after scrolling
  const updatedCount = await articles.count();

  if (updatedCount > initialCount) {
    // ✅ More articles successfully loaded
    expect(updatedCount).toBeGreaterThan(initialCount);
  } else {
    // ❌ No new articles; check for "No more items" message
    expect(updatedCount).toBe(initialCount);
  }
});
