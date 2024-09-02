import Parser from 'rss-parser';

export interface FeedItem {
    title: string;
    link: string;
    source: string;
}

const parser = new Parser();

export const fetchFeed = async (feedUrl: string): Promise<FeedItem[]> => {
    try {
        const feed = await parser.parseURL(feedUrl);
        return feed.items.map(item => ({
        title: item.title ?? 'No Title',
        link: item.link ?? '#',
        source: feed.title ?? 'Unknown Source',
        }));
    } catch (error) {
        console.error(`Error fetching feed from ${feedUrl}:`, error);
        return [];
    }
};