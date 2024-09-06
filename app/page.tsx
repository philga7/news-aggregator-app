import { fetchFeedOne } from '../utils/feeds/feedOne';
import { FeedItem } from '@/types/feedItem';

export default async function Home() {
    // Fetch the feed directly in the server component
    let articles: FeedItem[] = await fetchFeedOne();

    return (
        <div className="container mx-auto py-8">
            <ul className="space-y-2">
                {articles.map((article, index) => (
                    <li key={index} className="font-mono">
                        <a href={article.link} className="font-bold hover:underline" target="_blank" rel="noopener noreferrer" data-tid="articleLink">
                            {article.title}</a>
                        <p className="text-sm text-accent">
                            {article.source}
                        </p>
                    </li>
                ))}
            </ul>
        </div>
    );
}