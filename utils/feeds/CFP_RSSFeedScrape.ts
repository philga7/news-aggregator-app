import { feedScraper } from '../feedScraper';
import { FeedItem } from '@/types/feedItem';

export const FEED_URL = 'https://citizenfreepress.com';

export const fetchCFP_RSSFeed = async (): Promise<FeedItem[]> => {
    const articles = await feedScraper(FEED_URL);
    
    return articles;
};