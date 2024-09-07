import axios from 'axios';
import * as cheerio from 'cheerio';
import { FeedItem } from '@/types/feedItem';

export async function feedScraper(url: string): Promise<FeedItem[]> {
    const articles: FeedItem[] = [];

    try {
        const { data } = await axios.get(url);
        const $ = cheerio.load(data);

        $('.wpd-top-links li').each((index, element) => {
            const title = $(element).find('.headline-link').text();
            const link = $(element).find('a').attr('href');

            articles.push({
                title: title,
                link: link as string,
                source: 'Citizen Free Press',
            });
        })
    } catch (error) {
        console.error(`Error scraping ${url}:`, error);
    }
    return articles;
}