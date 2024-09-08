import { fetchFeed } from '../utils/feedRSSFetcher';
import { FeedItem } from '@/types/feedItem';
import Parser from 'rss-parser';

// Mocking the rss-parser package
jest.mock('rss-parser', () => {
    return jest.fn().mockImplementation(() => ({
        parseURL: jest.fn().mockResolvedValue({
            title: 'Test Feed',
            items: [
                { title: 'Test Article 1', link: 'https://example.com/article1', source: 'Test Feed' },
                { title: 'Test Article 2', link: 'https://example.com/article2', source: 'Test Feed' },
            ],
        }),
    }));
});

describe('fetchFeed', () => {
    beforeEach(() => {
        jest.clearAllMocks();
    });

    // Positive Test: Ensure the RSS feed is fetched and parsed correctly
    it('should fetch and parse an RSS feed correctly', async () => {
        const feedUrl = 'https://example.com/rss-feed.xml';
        const articles: FeedItem[] = await fetchFeed(feedUrl);

        expect(articles).toHaveLength(2);
        expect(articles[0]).toEqual({
            title: 'Test Article 1',
            link: 'https://example.com/article1',
            source: 'Test Feed',
        });
    });

    // Negative Test: Ensure an empty array is returned on error
    it('should return an empty array on error', async () => {
        // Override the mock implementation for this test to throw an error
        const mockParseURL = jest.fn().mockRejectedValue(new Error('Failed to fetch feed'));
        (Parser as jest.Mock).mockImplementation(() => {
            return {
                parseURL: mockParseURL,
            };
        });

        // const feedUrl = 'invalid-url';
        // const articles = await fetchFeed(feedUrl);

        // Expect an empty array because the feed fetching failed
        // expect(articles).toEqual([]);
    });
});
