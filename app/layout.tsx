export const metadata = {
    title: 'News Aggregator',
    description: 'A minimalistic news aggregator application.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <header>
          <h1>News Aggregator</h1>
        </header>
        <main>{children}</main>
      </body>
    </html>
  );
}