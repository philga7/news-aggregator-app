import { FeedItem } from '@/types/feedItem';

export async function fetchAllFeeds(): Promise<FeedItem[]> {
    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_BASE_URL}/api/feed`, {
        cache: 'no-store',
      });
  
      if (!res.ok) {
        throw new Error('Failed to fetch feed');
      }
  
      const data = await res.json();
      return data.data as FeedItem[];
    } catch (error) {
      console.error('Error fetching feed:', error);
      return [];
    }
}