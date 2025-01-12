import { fetchAllFeeds } from '@/utils/fetchAllFeeds';
import { FeedItem } from '@/types/feedItem';

export default async function Home() {
    const articles = await fetchAllFeeds();

    return (
        <div className="container mx-auto flex">
          <aside className="hidden md:block w-64 border-r border-gray-200 p-4">
            <nav>
              <ul>
                <li className="mb-2"><a href="#" className="hover:underline">Home</a></li>
                <li className="mb-2"><a href="#" className="hover:underline">Categories</a></li>
                <li><a href="#" className="hover:underline">About</a></li>
              </ul>
            </nav>
          </aside>
    
          <main className="flex-1 p-8">
            {articles.length === 0 ? (
              <p className="text-center text-red-500">Failed to load articles. Please try again.</p>
            ) : (
              <ul className="space-y-4">
                {articles.map((article, index) => (
                  <li key={index} className="p-4 border rounded hover:bg-gray-100">
                    <a data-tid="articleLink" href={article.link} target="_blank" rel="noopener noreferrer" className="text-xl font-bold text-blue-600 hover:underline">
                      {article.title}
                    </a>
                    <p className="text-sm text-gray-500">
                      {article.source} | {article.pubDate ? new Date(article.pubDate).toLocaleDateString() : 'Unknown date'}
                    </p>
                  </li>
                ))}
              </ul>
            )}
          </main>
        </div>
    );
}