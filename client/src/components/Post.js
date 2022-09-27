import { Card, CardGroup } from "react-bootstrap";

const Post = ({ post }) => {
  return (
    <CardGroup>
      <Card style={{ width: "18rem" }}>
        <Card.Body>
          <Card.Title>id: {post.id} </Card.Title>
          <Card.Img src={post.image}></Card.Img>
          <Card.Text>comment: {post.content}</Card.Text>
        </Card.Body>
      </Card>
    </CardGroup>
  );
};

export default Post;
