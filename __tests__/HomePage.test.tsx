import { render, screen } from '@testing-library/react';
import Home from '@/app/page';
import { fetchAllFeeds } from '@/utils/fetchAllFeeds';
import { FeedItem } from '@/types/feedItem';

// Correctly mock fetchAllFeeds from its actual path
jest.mock('@/utils/fetchAllFeeds', () => ({
  fetchAllFeeds: jest.fn(),
}));

describe('Home Page', () => {
  afterEach(() => {
    jest.clearAllMocks();
  });

  it('displays error message when no articles are loaded', async () => {
    (fetchAllFeeds as jest.Mock).mockResolvedValueOnce([]);

    render(<Home />);

    const errorMsg = await screen.findByText('Failed to load articles. Please try again.');
    expect(errorMsg).toBeInTheDocument();
  });

  it('displays articles when loaded successfully', async () => {
    const mockData: FeedItem[] = [
      {
        title: 'Sample Article',
        link: 'https://example.com/article',
        pubDate: 'Wed, 10 Jan 2024 12:00:00 GMT',
        contentSnippet: 'This is a sample article.',
        source: 'example.com',
      },
    ];

    (fetchAllFeeds as jest.Mock).mockResolvedValueOnce(mockData);

    render(<Home />);

    const articleTitle = await screen.findByText('Sample Article');
    expect(articleTitle).toBeInTheDocument();
  });
});
