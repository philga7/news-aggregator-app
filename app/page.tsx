import { fetchFeedOne } from './utils/feeds/feedOne';
import { FeedItem } from './utils/feedFetcher';


export default async function Home() {
    // Fetch the feed directly in the server component
    let articles: FeedItem[] = await fetchFeedOne();

    return (
      <div>
        <ul>
          {articles.map((article, index) => (
            <li key={index}>
              <a href={article.link} target="_blank" rel="noopener noreferrer" data-tid="articleLink">
                {article.title}
              </a> - {article.source}
            </li>
          ))}
        </ul>
      </div>
    );
}