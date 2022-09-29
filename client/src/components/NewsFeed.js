import { useEffect, useState } from "react";
import { CardGroup, Container, Form, Pagination } from "react-bootstrap";
import { BsSearch } from "react-icons/bs";
import InfiniteScroll from "react-infinite-scroll-component";
import NewsItem from "./NewsItem";
import Loader from "./Loader";
import EndMessage from "./EndMessage";

const NewsFeed = () => {
  const [items, setItems] = useState([]);
  const [activePage, setActivePage] = useState(1);

  useEffect(() => {
    const getItems = async () => {
      const res = await fetch(
        // `https://newsapi.org/v2/everything?q=surf-wsl&page=1&pageSize=20&sortBy=relevancy&language=en&apiKey=60dcae65b56641808aafbd67b95306c8`
      );
      const data = await res.json();
      setItems(data.articles);
    };

    getItems();
  }, []);

   useEffect(() => {
    const fetchItems = async () => {
      const res = await fetch(
        // `https://newsapi.org/v2/everything?q=surf-wsl&page=${activePage}&pageSize=20&sortBy=relevancy&language=en&apiKey=60dcae65b56641808aafbd67b95306c8`
      );
      const data = await res.json();
      setItems(data.articles);
    };

    fetchItems()

    },[activePage]);

  let handlePageKeyClick = (number) => {
    setActivePage(number);
    // fetchItems()
    // // console.log(number)
    // // fetch next page with page=number
    // // update state that renders boxes
  };
  let pageKeys = [];
  for (let number = 1; number <= 5; number++) {
    pageKeys.push(
      <Pagination.Item
        key={number}
        activePage={number === activePage}
        // onClick={() => handlePageKeyClick(number)}
        onClick={() => setActivePage(number)}
      >
        {number}
      </Pagination.Item>
    );
  }

  return (
    <>
      <Container>
        <Form className="news-search">
          <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>
              <BsSearch />
            </Form.Label>
            <Form.Control type="text" placeholder="Search" />
          </Form.Group>

          <Form.Group>
            <Form.Label>Filter</Form.Label>
            <Form.Select>
              <option>Select</option>
              <option>Option</option>
              <option>Option</option>
            </Form.Select>
          </Form.Group>
        </Form>
      </Container>

      <Container>
        <CardGroup>
          {items.map((item) => (
            <NewsItem key={item.id} item={item} />
          ))}
        </CardGroup>
        <Pagination>{pageKeys}</Pagination>
      </Container>
    </>
  );
};

export default NewsFeed;
