import styles from "./styles/styles.module.css";

export default function Card({ book }) {
  return (
    <div className={styles.card}>
      <h3>{book.title}</h3>
      <p>Autor: {book.author}</p>
      <p>Ano: {book.year}</p>
      <p>Gênero: {book.genre}</p>
    </div>
  );
}
