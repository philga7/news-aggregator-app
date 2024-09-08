import axios from 'axios';
import * as cheerio from 'cheerio';
import { FeedItem } from '@/types/feedItem';

export async function feedScraper(
    feedURL: string, 
    feedTitle: string, 
    mainSelector: string, 
    titleText: string
    ): Promise<FeedItem[]> {
    const articles: FeedItem[] = [];

    try {
        const { data } = await axios.get(feedURL);
        const $ = cheerio.load(data);

        $(mainSelector).each((index, element) => {
            const title = $(element).find(titleText).text();
            const link = $(element).find('a').attr('href');

            articles.push({
                title: title,
                link: link as string,
                source: feedTitle,
            });
        })
    } catch (error) {
        console.error(`Error scraping ${feedURL}:`, error);
    }
    return articles;
}