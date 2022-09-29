import { Card, CardGroup } from "react-bootstrap";
import Video from "./Video";

const Post = ({ post }) => {

  return (
    <CardGroup>
      <Card style={{ width: "18rem" }}>
        <Card.Body>
          <Card.Title>id: {post.id} </Card.Title>
          <Card.Img src={post.image} ></Card.Img>
          {post.video === null ? "" : <Video src={post.video} />}
          <Card.Text>comment: {post.content}</Card.Text>
        </Card.Body>
      </Card>
    </CardGroup>
  );
};

export default Post;
