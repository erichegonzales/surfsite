import { useEffect, useState } from "react";
import { Container } from "react-bootstrap";
import InfiniteScroll from "react-infinite-scroll-component";
import Post from "./Post";
import Loader from "./Loader";
import EndMessage from "./EndMessage";

const PostFeed = () => {
  const [posts, setPosts] = useState([]);
  const [hasMore, setHasMore] = useState(true);
  const [page, setPage] = useState(2);

  useEffect(() => {
    const getPosts = async () => {
      const res = await fetch(`http://localhost:3004/posts?_page=1&_limit=5`);
      const data = await res.json();
      setPosts(data);
    };

    getPosts();
  }, []);

  console.log(posts);

  const fetchPosts = async () => {
    const res = await fetch(
      `http://localhost:3004/posts?_page=${page}&_limit=5`
    );
    const data = await res.json();
    return data;
  };

    const fetchData = async () => {
      const postsFromServer = await fetchPosts();
      setPosts([...posts, ...postsFromServer]);
      if (postsFromServer.length === 0 || postsFromServer.length < 5) {
        setHasMore(false);
      }
      setPage(page + 1);
    };

  return (
    <Container>
      <InfiniteScroll
        dataLength={posts.length} //This is important field to render the next data
        next={fetchData}
        hasMore={hasMore}
        loader={<Loader />}
        endMessage={<EndMessage />}
      >
        {posts.map((post) => {
          return <Post key={post.id} post={post} />;
        })}
      </InfiniteScroll>
    </Container>
  );
}

export default PostFeed;
