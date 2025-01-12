"use client";

import { FormEvent, useState } from "react";
import axios from "axios";
import { useRouter } from "next/navigation";
import styles from "./styles.module.css";

const RegisterBookPage = () => {
  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");
  const [year, setYear] = useState("");
  const [gender, setGender] = useState("");
  const [error, setError] = useState("");

  const router = useRouter();

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();

    const bookData = {
      title,
      author,
      year,
    };

    try {
      await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/books`, bookData);
      router.push("/");
    } catch (err) {
      setError("Erro ao registrar o livro");
      console.error(err);
    }
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Cadastrar um novo livro</h1>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="title">Título:</label>
          <input type="text" id="title" value={title} onChange={(e) => setTitle(e.target.value)} required />
        </div>
        <div>
          <label htmlFor="author">Autor:</label>
          <input type="text" id="author" value={author} onChange={(e) => setAuthor(e.target.value)} required />
        </div>
        <div>
          <label htmlFor="year">Ano:</label>
          <input type="number" id="year" value={year} onChange={(e) => setYear(e.target.value)} required />
        </div>
        <div>
          <label htmlFor="gender">Gênero:</label>
          <input type="text" id="gender" value={gender} onChange={(e) => setGender(e.target.value)} required />
        </div>
        <div>
          <button type="submit">Cadastrar</button>
        </div>
      </form>
    </div>
  );
};

export default RegisterBookPage;
