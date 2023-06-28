<script>
import GenerosApi from "@/api/generos";
const generosApi = new GenerosApi();
export default {
  data() {
    return {
      generos: [],
      genero: {},
    };
  },
  async created() {
    this.generos = await generosApi.buscarGeneros();
  },
  methods: {
    async salvar() {
      if (this.genero.id) {
        await generosApi.atualizarGenero(this.genero);
      } else {
        await generosApi.adicionarGenero(this.genero);
      }
      this.genero = {};
      this.generos = await generosApi.buscarGeneros();
    },
    editar(genero) {
      Object.assign(this,genero, genero);
    },
    async excluir(genero) {
      await generosApi.excluirGenero(genero.id);
      this.generos = await generosApi.buscarGeneros();
    },
  },
};
</script>

<template>
  <h1>Generos</h1>
  <hr />
  <div class="form">
    <input type="text" v-model="genero.descricao" placeholder="Descrição" />
    <button @click="salvar">Salvar</button>
  </div>
  <hr />
  <ul>
    <li v-for="genero in generos" :key="genero.id">
      <span @click="editar(genero)">
        ({{ genero.id }}) - {{ genero.nome }} -
      </span>
      <button @click="excluir(genero)">X</button>
    </li>
  </ul>
</template>

<style></style>
