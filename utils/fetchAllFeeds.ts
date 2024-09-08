import { fetchCFP_RSSFeed } from "./feeds/cfp_RSSFeedScrape";
import { fetchAPINewsUSHeadlines } from "./feeds/apiNews_us_headlines_APIFeed";

export const fetchAllFeeds = async () => {
    const rssArticles = await Promise.all([
        fetchCFP_RSSFeed()
    ]);
    const apiArticles = await Promise.all([
        fetchAPINewsUSHeadlines()
    ]);

    return[...rssArticles.flat(), ...apiArticles.flat()];
};