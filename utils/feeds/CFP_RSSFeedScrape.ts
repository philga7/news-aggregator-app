import { feedScraper } from '../feedRSSScraper';
import { FeedItem } from '@/types/feedItem';

const feedURL = 'https://citizenfreepress.com';
const feedTitle = 'Citizen Free Press';
const mainSelector = '.wpd-top-links li';
const titleText = '.headline-link';

export const fetchCFP_RSSFeed = async (): Promise<FeedItem[]> => {
    const articles = await feedScraper(feedURL, feedTitle, mainSelector, titleText);
    
    return articles;
};