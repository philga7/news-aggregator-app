import axios from 'axios';
import * as cheerio from 'cheerio';

/**
 * Scrapes the actual third-party URL from Citizen Free Press article pages.
 * @param {string} pageURL - URL of the CFP article page.
 * @returns {Promise<string>} - Resolved original article URL.
 */
export async function scrapeOriginalURL(pageURL: string): Promise<string> {
    try {
      const { data } = await axios.get(pageURL, {
        headers: { 'User-Agent': 'News Aggregator Bot' },
        timeout: 5000,  // Prevent hanging requests
      });
  
      const $ = cheerio.load(data);
  
      // Find the first external link in the article, assuming CFP links out this way
      const externalLink = $('a').filter((_, el) => {
        const href = $(el).attr('href');
        return !!href && !href.includes('citizenfreepress.com');
      }).first().attr('href');
  
      return externalLink || pageURL; // Fallback to original link if scraping fails
    } catch (error) {
      if (axios.isAxiosError(error)) {
        console.error(`Axios Error while scraping ${pageURL}:`, error.message);
      } else if (error instanceof AggregateError) {
        console.error(`AggregateError while scraping ${pageURL}:`, error.errors);
      } else {
        console.error(`Unexpected Error while scraping ${pageURL}:`, error);
      }

      return pageURL;
    }
}