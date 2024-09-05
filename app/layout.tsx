import '../styles/globals.css';
import Header from '@/components/Header';
import Footer from '@/components/Footer';

export const metadata = {
    title: 'News Aggregator',
    description: 'A minimalistic news aggregator application.',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-white text-black font-mono">
        <Header />
        <main className="container mx-auto py-8">{children}</main>
        <Footer />
      </body>
    </html>
  );
}