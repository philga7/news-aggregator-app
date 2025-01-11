import { NextResponse } from 'next/server';
import Parser from 'rss-parser';
import NodeCache from 'node-cache';
import axios from 'axios';
import { scrapeOriginalURL } from '@/utils/scrapeOriginalURL';
import { FeedItem } from '@/types/feedItem';

const RSS_FEED_URL = process.env.CITIZEN_FREE_PRESS_URL || 'https://citizenfreepress.com/feed/';
const cache = new NodeCache({ stdTTL: 300 }); // Cache for 5 minutes
const parser = new Parser();

// Helper to resolve the actual third-party URL
function resolveOriginalURL(url: string): string {
    try {
      const urlObj = new URL(url);
      const redirectedURL = urlObj.searchParams.get('url');
      return redirectedURL ? decodeURIComponent(redirectedURL) : url;
    } catch {
      return url;
    }
}

/**
 * Extracts the domain from a URL.
 * @param {string} url - The URL to extract the source from.
 * @returns {string} - The domain name.
 */
function extractSource(url: string): string {
    try {
      const hostname = new URL(url).hostname.replace('www.', '');
      return hostname;
    } catch {
      return 'Unknown Source';
    }
}

export async function GET() {
    try {
        // Check cache first
        const cachedData = cache.get<FeedItem[]>('feedData');
        if (cachedData) {
        return NextResponse.json({ success: true, data: cachedData });
        }

        // Fetch RSS feed
        const { data: xmlData } = await axios.get(RSS_FEED_URL);

        // Parse the RSS feed
        const feed = await parser.parseString(xmlData);

        // Process feed items with scraping for original URLs
        const items: FeedItem[] = await Promise.all(
            feed.items?.map(async (item) => {
            const originalURL = await scrapeOriginalURL(item.link || '');
            return {
                title: item.title || 'No Title',
                link: originalURL || item.link || '',
                pubDate: item.pubDate || 'No Date',
                contentSnippet: item.contentSnippet || 'No Summary',
                source: extractSource(originalURL || item.link || ''),
            };
            }) || []
        );

        // Cache the result
        cache.set('feedData', items);

        return NextResponse.json({ success: true, data: items });
    } catch (error) {
        console.error('Error fetching RSS feed:', error);
        return NextResponse.json(
            { success: false, message: 'Failed to load feed. Please try again.' },
            { status: 500 }
        );
    }
}