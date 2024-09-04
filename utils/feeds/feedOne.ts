import { fetchFeed, FeedItem } from '../feedFetcher';

const FEED_URL = 'https://citizenfreepress.com/feed/';

export const fetchFeedOne = async (): Promise<FeedItem[]> => {
    const articles = await fetchFeed(FEED_URL);
    
    return articles;
};