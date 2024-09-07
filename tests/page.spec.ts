// tests/homepage.spec.ts
import { test, expect } from '@playwright/test';

test('homepage has expected title and news articles', async ({ page }) => {
    // Go to the homepage
    await page.goto('http://localhost:3000');

    // Check if the title contains 'News'
    await expect(page).toHaveTitle(/News/);

    // Check if at least one article is displayed
    const article = page.locator('[data-tid="articleLink"]');
    const sourceLink = page.locator('[data-tid="sourceLink"]');
    const count = await article.count();
    const sourceCount = await sourceLink.count();
    
    expect(count).toBeGreaterThan(0);
    expect(sourceCount).toBeGreaterThan(0);
});
