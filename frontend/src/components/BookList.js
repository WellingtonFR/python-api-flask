import styles from "./styles/styles.module.css";
import Card from "./BookCard";

const BookList = ({ books }) => {
  return (
    <div className={styles.container}>
      <h2>Livros cadastrados</h2>
      <div className={styles.bookContainer}>
        {books.map((book) => (
          <Card key={book.id} book={book} />
        ))}
      </div>
    </div>
  );
};

export default BookList;
