import { Card, CardGroup } from "react-bootstrap";

const NewsItem = ({ item }) => {
  return (
    <CardGroup >
      <Card style={{ width: "38rem" }}>
        <Card.Body>
          <Card.Title>title: {item.title} </Card.Title>
          <Card.Img src={item.urlToImage}></Card.Img>
          {/* {post.video === null ? "" : <Video src={post.video} />} */}
          <Card.Text>comment: {item.content}</Card.Text>
        </Card.Body>
      </Card>
    </CardGroup>
  );
}

export default NewsItem