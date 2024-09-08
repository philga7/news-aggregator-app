import axios from 'axios';

const feedURL = 'https://newsapi.org/v2/top-headlines?country=us'

export const fetchAPINewsUSHeadlines = async () => {
    const apiKey = process.env.NEWSAPI_KEY;
    const apiURL = `${feedURL}&apiKey=${apiKey}`;

    try {
        const response = await axios.get(apiURL);
        return response.data.articles.map((article: any) => ({
            title: article.title ?? 'No Title',
            link: article.url ?? '#',
            source: article.source.name ?? 'Unknown Source',
        }));
    } catch (error) {
        console.error('Error fetching feed from NewsAPI: ', error);
        return [];
    }
}