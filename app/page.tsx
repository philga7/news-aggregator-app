import { fetchAllFeeds } from '@/utils/fetchAllFeeds';

export const dynamic = 'force-dynamic'; // ✅ Explicitly allow dynamic fetch

export default async function Home() {
    const articles = await fetchAllFeeds();

    return (
        <div className="flex min-h-screen">

          {/* Sidebar (Hidden on Mobile, Visible on md and up) */}
          <aside className="hidden md:flex flex-col bg-black text-white p-6 relative">
            <nav className="relative">
              <ul className="space-y-2">
                <li><a href="#" className="sidebar-link block text-base font-medium text-white hover:text-gray-400 transition-colors pr-4">Home</a></li>
                <li><a href="#" className="sidebar-link block text-base font-medium text-white hover:text-gray-400 transition-colors pr-4">Categories</a></li>
                <li><a href="#" className="sidebar-link block text-base font-medium text-white hover:text-gray-400 transition-colors pr-4">About</a></li>
              </ul>
            </nav>

            {/* Dynamic Vertical Divider */}
            <div className="absolute top-0 bottom-0 left-full ml-2 bg-gray-700" id="dynamic-divider"></div>
          </aside>
        
          {/* Main content */}  
          <main className="flex-1 p-8">
            {articles.length === 0 ? (
              <p className="text-center text-red-400">Failed to load articles. Please try again.</p>
            ) : (
              <ul className="space-y-3">
                {articles.map((article, index) => (
                  <li key={index}>
                    <a data-tid="articleLink" href={article.link} target="_blank" rel="noopener noreferrer" className="block text-lg font-semibold text-blue-400 hover:text-blue-300 transition-colors">
                      {article.title}
                    </a>
                    <p className="text-xs text-gray-500">
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