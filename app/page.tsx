'use client';

import { useState, useEffect } from 'react';

export default function Home() {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    async function fetchArticles() {
      const res = await fetch('/api/articles');
      const data = await res.json();
      setArticles(data);
    }
    fetchArticles();
  }, []);

  return (
    <div className="container mx-auto">
      <h1 className="text-3xl font-bold mb-5">Latest News</h1>
      <ul>
        {articles.map((article) => (
          <li key={article.id} className="mb-5">
            <h2 className="text-xl font-semibold">{article.title}</h2>
            <p>{article.body.slice(0, 200)}...</p>
          </li>
        ))}
      </ul>
    </div>
  );
}


// import { fetchAllFeeds } from '@/utils/fetchAllFeeds';
// import { FeedItem } from '@/types/feedItem';

// export default async function Home() {
//     // Fetch the feed directly in the server component
//     let articles: FeedItem[] = await fetchAllFeeds();

//     return (
//         <div className="container mx-auto py-8">
//             <ul className="space-y-2">
//                 {articles.map((article, index) => (
//                     <li key={index} className="font-mono">
//                         <a href={article.link} className="font-bold hover:underline" target="_blank" rel="noopener noreferrer" data-tid="articleLink">
//                             {article.title}</a>
//                         <p className="text-sm text-accent">
//                             {article.source}
//                         </p>
//                     </li>
//                 ))}
//             </ul>
//         </div>
//     );
// }