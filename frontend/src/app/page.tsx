import BookList from "../components/BookList";
import styles from "./page.module.css";
import axios from "axios";

const Home = async () => {
  let books = [];

  const fetchBooks = async () => {
    try {
      const response = await axios.get(`${process.env.NEXT_PUBLIC_API_URL}/books`);
      return response.data;
    } catch (error) {
      console.error("Error fetching books:", error);
      throw error;
    }
  };

  try {
    books = await fetchBooks();
  } catch (error) {
    console.error("Erro ao buscar os livros:", error);
  }

  return (
    <div className={styles.container}>
      <h1>Biblioteca Virtual</h1>
      {books.length > 0 ? <BookList books={books} /> : <p>Não há livros disponíveis ou ocorreu um erro ao consultar.</p>}
    </div>
  );
};

export default Home;
