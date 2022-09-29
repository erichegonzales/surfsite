import { Card, CardGroup, Row, Col } from "react-bootstrap";

const Lesson = ({ lesson }) => {
  return (
    <CardGroup>
      <Card style={{ width: "38rem" }}>
        <Card.Body>
          <Card.Title>id: {lesson.id} </Card.Title>
          <Card.Img src={lesson.image}></Card.Img>
          {/* {post.video === null ? "" : <Video src={post.video} />} */}
          <Card.Text>comment: {lesson.content}</Card.Text>
        </Card.Body>
      </Card>
    </CardGroup>
  );
};

export default Lesson;
