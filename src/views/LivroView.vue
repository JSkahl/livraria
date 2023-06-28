<script>
import LivrosApi from "@/api/livros.js";
import GenerosApi from "@/api/generos.js"
import EditorasApi from "@/api/editoras.js"

const livrosApi = new LivrosApi();
const generosApi = new GenerosApi();
const editorasApi = new EditorasApi();

export default {
  data() {
    return {
      livros: [],
      livro: {
        titulo: "",
        isbn: "",
        quantidade: "",
        preco: "",
        genero: {},
        editora: {},
      },
      generos: [],
      editoras: [],
    };
  },
  async created() {
    this.livros = await livrosApi.buscarLivros();
    this.generos = await generosApi.buscarGeneros();
    this.editoras = await editorasApi.buscarEditoras();
  },
  methods: {
    async salvar() {
      this.livro.genero = this.livro.genero.id
      this.livro.editora = this.livro.editora.id
      if (this.livro.id) {
        await livrosApi.atualizarLivro(this.livro);
      } else {
        console.log(this.livro)
        await livrosApi.adicionarLivro(this.livro);
      }
      this.livro = {
        titulo: "",
        isbn: "",
        quantidade: "",
        preco: "",
        genero: {},
        editora: {},
      }
      this.livros = await livrosApi.buscarLivros();
    },
    editar(livro) {
      console.log(livro)
      Object.assign(this.livro, livro);
    },
    async excluir(livro) {
      await livrosApi.excluirLivro(livro.id);
      this.livros = await livrosApi.buscarLivros();
    },
  },
};
</script>

<template>
  <h1>Livros</h1>
  <hr />
  <div class="form">
    <input type="text" v-model="livro.titulo" placeholder="Descrição" />
      <div></div>
    <input type="text" v-model="livro.isbn" placeholder="ISBN">
      <div></div>
    <input type="number" v-model="livro.quantidade" placeholder="Quantidade">
      <div></div>
    <input type="number" v-model="livro.preco" placeholder="Preço">
      <div></div>
    <select v-model="livro.genero">
      <option v-for="genero in generos" :key="genero.id" :value="genero" :selected="genero.id === livro.genero.id ? true : false">{{ genero.nome }}</option></select>
      <div></div>
    <select v-model="livro.editora">
      <option v-for="editora in editoras" :key="editora.id" :value="editora" :selected="editora.id === livro.editora.id ? true : false">{{ editora.nome }}</option></select>
      <div></div>

    <button @click="salvar">Salvar</button>
  </div>
  <hr />
  <ul>
    <li v-for="livro in livros" :key="livro.id">
      <span @click="editar(livro)">
        ({{ livro.id }}) - {{ livro.titulo }}
      </span>
      <button @click="excluir(livro)">X</button>
    </li>
  </ul>
</template>

<style></style>
